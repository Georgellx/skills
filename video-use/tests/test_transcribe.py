from __future__ import annotations

import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch


HELPERS_DIR = Path(__file__).resolve().parents[1] / "helpers"
sys.path.insert(0, str(HELPERS_DIR))

import pack_transcripts  # noqa: E402
import transcribe  # noqa: E402


SAMPLE_RESPONSE = {
    "audio_info": {"duration": 3100},
    "result": {
        "text": "你好，world!",
        "utterances": [
            {
                "start_time": 100,
                "end_time": 550,
                "text": "你好，",
                "additions": {"speaker": "0"},
                "words": [
                    {"start_time": 100, "end_time": 250, "text": "你", "confidence": 0.9},
                    {"start_time": 250, "end_time": 500, "text": "好", "confidence": 0.8},
                    {"start_time": 500, "end_time": 550, "text": "，", "confidence": 0.7},
                ],
            },
            {
                "start_time": 1200,
                "end_time": 1700,
                "text": "world!",
                "additions": '{"speaker": "1"}',
                "words": [
                    {"start_time": 1200, "end_time": 1600, "text": "world"},
                    {"start_time": 1600, "end_time": 1700, "text": "!"},
                ],
            },
        ],
    },
}


class FakeResponse:
    def __init__(
        self,
        payload: dict,
        code: str = "20000000",
        message: str = "OK",
    ) -> None:
        self.status_code = 200
        self.headers = {
            "X-Api-Status-Code": code,
            "X-Api-Message": message,
            "X-Tt-Logid": "test-log-id",
        }
        self._payload = payload

    def json(self) -> dict:
        return self._payload


class NormalizeDoubaoResponseTests(unittest.TestCase):
    def test_normalizes_timestamps_speakers_and_duration(self) -> None:
        normalized = transcribe.normalize_doubao_response(SAMPLE_RESPONSE)

        self.assertEqual(normalized["provider"], "doubao")
        self.assertEqual(normalized["metadata"]["audio_duration"], 3.1)
        self.assertEqual(normalized["words"][0]["start"], 0.1)
        self.assertEqual(normalized["words"][0]["speaker_id"], "speaker_0")
        self.assertEqual(normalized["words"][3]["speaker_id"], "speaker_1")

    def test_rejects_text_without_word_timestamps(self) -> None:
        payload = {
            "result": {
                "text": "有内容",
                "utterances": [{"text": "有内容", "words": []}],
            }
        }

        with self.assertRaisesRegex(ValueError, "without word timestamps"):
            transcribe.normalize_doubao_response(payload)

    def test_normalized_output_packs_chinese_and_splits_speakers(self) -> None:
        words = transcribe.normalize_doubao_response(SAMPLE_RESPONSE)["words"]
        phrases = pack_transcripts.group_into_phrases(words, silence_threshold=0.5)

        self.assertEqual(len(phrases), 2)
        self.assertEqual(phrases[0]["text"], "你好，")
        self.assertEqual(phrases[1]["text"], "world!")
        self.assertEqual(phrases[1]["speaker_id"], "speaker_1")


class DoubaoRequestTests(unittest.TestCase):
    @patch.object(transcribe.requests, "post")
    def test_call_uses_new_console_auth_and_verbatim_options(self, post) -> None:
        post.return_value = FakeResponse(SAMPLE_RESPONSE)
        with tempfile.TemporaryDirectory() as tmp:
            audio = Path(tmp) / "sample.mp3"
            audio.write_bytes(b"test audio")
            result = transcribe.call_doubao(audio, "test-key", language="zh-CN")

        kwargs = post.call_args.kwargs
        self.assertEqual(kwargs["headers"]["X-Api-Key"], "test-key")
        self.assertEqual(kwargs["headers"]["X-Api-Resource-Id"], "volc.bigasr.auc_turbo")
        options = kwargs["json"]["request"]
        self.assertFalse(options["enable_itn"])
        self.assertFalse(options["enable_ddc"])
        self.assertTrue(options["enable_speaker_info"])
        self.assertEqual(options["language"], "zh-CN")
        self.assertEqual(result["words"][0]["text"], "你")

    @patch.object(transcribe.requests, "post")
    def test_empty_audio_response_accepts_key_check(self, post) -> None:
        post.return_value = FakeResponse(
            {},
            code="45000000",
            message="code: 11105 message: invalid argument,empty audio",
        )

        ok, message = transcribe.check_api_key("test-key")

        self.assertTrue(ok)
        self.assertIn("45000000", message)


if __name__ == "__main__":
    unittest.main()

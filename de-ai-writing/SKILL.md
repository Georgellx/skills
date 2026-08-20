---
name: de-ai-writing
description: >
  给中英文文本做去 AI 味、活人感审读和改写。Use when Codex needs to review, diagnose, humanize, de-AI, or rewrite Chinese or English drafts that sound AI-generated, robotic, too polished, too generic, too corporate, too much like ChatGPT/Claude/Gemini, or "not like a real person wrote it"; triggers include 去 AI 味、降 AI 感、活人感、写得像真人、别像 AI、AI 腔、机翻腔、humanize this, de-AI this, sounds like AI, too robotic, make it sound human, make it natural, sounds like ChatGPT, blog/email/essay/speech/social/media/product copy polishing.
---

# 双语去 AI 味写作

## Overview

把一段中英文文本从「模型在顺滑输出」改成「一个具体的人在认真表达」。核心任务不是骗检测器，也不是随手加口语词，而是定位机械感来源，保留事实边界，补上真实语境、判断过程、节奏变化和属于作者的取舍。

默认保持原文语言：中文进中文出，英文进英文出，中英混排就保留必要的混排。除非用户明确要求，不翻译、不新增经历、不编造数据、人物、引用、案例或信源。

## 工作流 / Workflow

### 1. 明确改写边界

先判断用户要哪一种结果：

- **只审读 / audit only**：指出 AI 味、逻辑、节奏和事实风险，不改全文。
- **轻度润色 / light edit**：保留原结构，只改句子、转折、语气和段落节奏。
- **深度重写 / deep rewrite**：重组表达顺序，但不新增未经确认的事实。
- **指定语气 / voice or platform fit**：优先服从用户给出的作者人设、平台、读者、学术/商务/口语边界和禁忌。
- **样本拟合 / voice calibration**：如果用户给了自己的写作样本，先分析句长、词汇层级、段落开头、转折方式、标点习惯、口头偏好，再把这些特征迁移到改写稿里。

如果缺少目标读者或发布场景但文本本身足够判断，直接处理。只有当这个信息会显著改变改写方向时，才问一个最关键的问题。

### 2. 先看叠加信号，不做词语迷信

不要因为一个词、一条破折号或一个三项并列就判定 AI 味。优先看 **pattern stacking**：多个弱信号是否集中在同一句、同一段或同一种结构里。诊断时合并重叠问题，不要把同一个短语重复算成三四个问题。

通用高频信号：

- **结构太工整**：每节都是同样的引入、解释、总结；每个列表长度一致；每段都收成一句 takeaway。
- **信息堆叠**：连续解释概念、优点、方法，但没有人的观察、选择、代价或判断过程。
- **意义拔高**：把普通事实写成重要转折、深远影响、时代趋势或战略意义。
- **空泛判断**：出现没有承载物的评价，如「显著提升」「极大改善」「值得关注」或 "transformative", "valuable", "crucial"。
- **泛泛归因**：使用「业内人士认为」「研究表明」或 "experts argue", "industry reports suggest" 但没有具体来源。
- **事实被抹平**：具体、罕见、有边界的事实被写成普遍正确的套话。
- **转折靠连接词硬推**：中文反复用「然而/因此/此外」，英文反复用 "Moreover/Furthermore/Additionally/That said"。
- **总结腔过重**：段尾频繁复述、拔高、升华，读者还没感受到就被要求认同。
- **人称和距离漂移**：在「我/我们/你/用户」或 "I/we/you/users" 之间无理由切换。
- **安全但无聊**：每句话都正确、礼貌、均衡，但没有偏好、犹豫、锋利判断、经验痕迹或具体场景。

### 3. 英文 AI 味重点检查

英文稿额外检查这些模式，尤其是多个模式同时出现时：

- **AI vocabulary clusters**：delve, landscape, tapestry, pivotal, crucial, robust, seamless, comprehensive, nuanced, transformative, underscore, foster, leverage, harness, navigate, realm, myriad, plethora, groundbreaking, ecosystem（非技术语境）等词密集出现。
- **Copula avoidance**：能用 "is/are/has" 的地方反复写成 "serves as", "stands as", "features", "boasts", "represents"。
- **Superficial -ing phrases**：句尾用 "highlighting/underscoring/showcasing/reflecting/contributing to..." 假装加深分析。
- **Negative parallelisms**："not just X, but Y", "not merely..., but..." 反复作为结构拐杖。
- **Rule of three**：三项并列里第三项明显凑数，如 "innovation, inspiration, and insights"。
- **Synonym cycling**：为了避免重复而不断换同义词，反而让指代变糊。
- **False ranges**："from X to Y" 里的 X/Y 不是实际尺度，只是在制造宏大感。
- **Rhythm too smooth**：大量 15-25 词中等长度句，几乎没有短句、片段、自然重复、收缩形式或停顿。
- **Style tells**：过量 em dash、机械加粗、emoji 装饰、plain-text 场景下异常使用 curly quotes、每个列表项都是粗体小标题。
- **Chatbot artifacts**："Great question", "I hope this helps", "Let's dive in", "Here's what you need to know", "Would you like me to..."。

英文改法不是同义词替换。通常要删掉膨胀句，换成具体事实、直接动词、自然重复、真实限制和更有节奏的段落。

### 4. 中文 AI 味重点检查

中文稿额外检查这些模式：

- **教科书开头**：从时代背景、行业趋势、抽象定义开场，而不是具体问题、操作瞬间或真实处境。
- **公文/报告腔泛化**：「具有重要意义」「提供有力支撑」「不断推动」「赋能」「构建生态」密集出现。
- **排比过满**：三四字词连续堆叠，读起来顺但没有信息增量。
- **伪客观**：为了稳妥把所有判断都写成「可能」「一定程度上」「具有潜力」，导致观点没有力度。
- **机翻腔**：不自然的中英空格、抽象名词堆叠、英文句法硬套中文。
- **假活人感**：为了不像 AI 加入口水、自嘲或故事，但这些细节并不来自用户素材。

中文改法要把抽象论题落回具体处境、选择和代价。可以更自然，但不要为了「口语」牺牲准确性。

### 5. 改写原则

- **保留事实边界**：只使用原文、用户素材、公开可验证信息，或用户明确声明的个人经历。缺失细节标成「待确认 / to confirm」。
- **先删膨胀，再补承载物**：删除意义拔高、空泛形容和模板段，再用来源内已有的事实、动作、限制、例子承接观点。
- **增加判断过程**：写出为什么这样看、哪里有取舍、曾经怎么误判、证据让想法发生了什么变化。
- **保持作者语言**：有写作样本时，匹配样本的句长、词汇、段落节奏和怪味道；没有样本时，选择自然、具体、不过度表演的声音。
- **让转折长在内容里**：用问题、行动、失败、证据推动下一段，少靠通用连接词硬转。
- **允许不完全对称**：段落长短可以不均；有些段落可以直接停下；列表不是越整齐越好。
- **英语可适度使用 contractions/fragments**：在博客、邮件、演讲稿、社媒里可以用 "don't", "it's", "And/But/So" 开头或短句；学术/法律/正式报告中要更克制。
- **中文可保留专业密度**：考试答案、论文说明、技术报告不必强行口语化，重点是去掉模板拔高和虚假完整性。
- **不要伪造缺陷**：不要通过故意错别字、语法错误、低俗俚语或随机口水来制造「真人感」。

### 6. 建议编辑轮次

复杂文本按轮次处理，短文本可以合并：

1. **结构轮**：打破重复 section shape、模板列表和整齐 takeaway。
2. **事实轮**：检查数据、引用、专名、来源、时间边界和无法追溯的判断。
3. **语言轮**：处理 AI vocabulary、中文套话、copula avoidance、-ing 假分析、泛泛归因、过度连接词。
4. **节奏轮**：调整句长、段落长短、停顿、重复、口语/正式程度。
5. **复检轮**：问自己：这篇还哪里「一眼模型」？列出剩余 1-3 个问题，再改最后一版。

如果声称某个量化信号存在，先数一下，例如 em dash 次数、同一连接词次数、每节列表项数。不要靠感觉夸大问题。

### 7. 事实和伦理保护

去 AI 味不是编故事，也不是承诺绕过 AI 检测。遇到事实性内容时：

- 不新增具体数据、人物、用户评价、市场结论、历史事实、亲身经历或引用，除非用户给出素材。
- 原文中无法追溯的具体事实，保留时标注「待确认 / to confirm」，或改成更谨慎的表达。
- 产品名、公司名、技术名保留官方拼写。无法确认时标注「待核对 / check spelling」。
- 不把「可能 / may / seems」改成确定结论。
- 不为了显得有故事而制造时间、地点、对话、截图、读者反馈。
- 如果用户明确要求绕过检测器、掩盖代写、伪装学术原创，只做诚实编辑和署名/披露建议，不优化检测规避。

## 输出格式

根据任务规模选择最有用的格式。输出语言默认跟随原文。

只审读时：

```markdown
**AI 味诊断 / AI-Sounding Diagnosis**
- [位置] 问题，为什么像 AI，建议怎么改

**事实风险 / Fact Risks**
- [位置] 待确认内容，建议处理方式

**优先修改顺序 / Edit Priority**
1. ...
```

改写短文本时：

```markdown
**改写版 / Rewrite**
[直接给完整改写]

**主要改动 / Changes**
- ...
```

改写长文时：

```markdown
**整体判断 / Overall Judgment**
[一句话说明最大 AI 味来源]

**逐段诊断 / Section Notes**
- [段落或标题] 问题和处理策略

**改写版 / Rewrite**
[完整改写或按章节改写]

**待确认 / To Confirm**
- [不能擅自补全的事实、案例、数据或经历]
```

如果用户只要最终稿，不要附长诊断；最多给一小段「主要改动」。

## 活人感复检 / Human Voice Check

提交前用读者视角通读一遍：

**读完这段文字，我感觉是一个有具体经历、判断和取舍的人在说话，还是一个模型在把正确的话顺序排出来？**

英文稿也问：

**Would a knowledgeable person in this context plausibly write this, with this rhythm, these claims, and this level of certainty?**

如果仍然后者，继续检查：

- 有没有段落只在解释，没有观察、行动、证据或判断。
- 有没有连续三段都用同一种句式推进。
- 有没有把普通结论说成重大洞察。
- 有没有为了完整而保留废话。
- 有没有新增但无法证实的细节。
- 有没有只是换词、加 contractions、删 em dash，却没有修掉结构和事实空洞。

只有在事实边界清楚、读感明显更像具体作者表达时，才交付最终稿。

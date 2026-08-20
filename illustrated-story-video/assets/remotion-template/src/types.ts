export type ProjectScene = {
  id: string;
  image: string;
  durationSeconds: number;
  imageFit: 'contain' | 'cover';
  imagePosition: string;
  chinese?: string;
  english?: string;
};

export type ProjectConfig = {
  title: string;
  canvas: {
    width: number;
    height: number;
    fps: number;
    background: string;
  };
  reveal: {
    blankSeconds: number;
    grayscaleEndSeconds: number;
    colorEndSeconds: number;
    featherPercent: number;
    zoomEnd: number;
  };
  subtitles: {
    insetStartSeconds: number;
    insetEndSeconds: number;
  };
  scenes: ProjectScene[];
};

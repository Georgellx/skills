# 生图提示词模板

每张图单独生成。先根据正文内容提炼一个认知锚点，再替换变量。不要把多张图拼在一起。

```text
Generate one standalone 16:9 horizontal Chinese article illustration.

Article idea:
{用 1-2 句说明这张图来自文章里的哪个判断、流程、结构或隐喻}

Visual DNA:
Flat 2D illustration with a loose hand-drawn feeling. Clean pale cream-green or very light warm green solid background. Dark forest-green hand-drawn outlines. Bold simple color blocks. Generous empty space. Coral orange and vivid purple-blue accent props. Sparse handwritten Chinese annotations. Playful brand mascot article illustration style. No shadows, no gradients, no texture, no realistic rendering, no 3D, no complex background, no PPT infographic look.

Recurring IP character required:
Perry, a cute anthropomorphic pear character with a bright lime-yellow green pear-shaped body, rounded irregular pear silhouette, narrow top and wider bottom. Perry must have a short curved dark forest-green stem on top and one small bright green leaf attached near the stem. Use simple dark forest-green hand-drawn line arms and legs, long flexible limbs, simple four-finger hands, simple line feet. Face is minimal and friendly: white round eyes with dark green pupils or simple closed-eye expressions, tiny mouth, and two round coral-pink cheek blush dots. Perry must perform the core conceptual action, not decorate the scene.

Theme:
{正文配图主题}

Structure type:
{结构类型：Workflow / 系统局部 / 前后对比 / 角色状态 / 概念隐喻 / 方法分层 / 地图路线 / 小漫画分镜}

Core idea:
{这张图要表达的核心意思}

Composition:
{具体画面：Perry 在哪里、正在做什么、主要物件是什么、信息如何流动}

Suggested elements:
{元素1} / {元素2} / {元素3} / {元素4}

Chinese handwritten labels:
{标注词1} / {标注词2} / {标注词3} / {标注词4} / {可选标注词5}

Color use:
Bright lime-green for Perry's pear body. Dark forest-green for outlines, limbs, arrows, and handwritten labels. Coral orange for key warnings, results, boxes, and action highlights. Vivid purple-blue for AI, systems, procedure modules, and secondary props. Coral-pink cheek blush on Perry.

Constraints:
One image explains only one core structure. Keep the main subject around 40%-60% of the canvas. Preserve generous blank space. Use only 3-5 short handwritten Chinese labels when possible, at most 5-8 labels. Do not write a title in the top-left corner. Do not write the structure type on the image. Do not make it a formal diagram, course slide, dense explainer, or realistic scene. Do not copy prior examples or reuse known case compositions unless explicitly requested; invent a fresh visual metaphor for this specific article. Never omit Perry's curved stem, single leaf, coral cheek blush, pear-shaped body, or dark green line limbs.
```

## 图像编辑提示

去掉左上角标题：

```text
Edit the provided image. Remove only the handwritten title "{要删除的文字}" and its underline from the top-left corner. Fill that area with the same clean background, matching the surrounding blank space. Preserve everything else exactly: Perry, labels, paths, line style, composition, aspect ratio, and image quality. Do not add any new text or objects.
```

增强 Perry 参与感：

```text
Regenerate this illustration with the same core meaning and simple layout, but make Perry more central to the conceptual action. Perry should be doing the work that explains the idea, not standing beside the diagram. Keep the pear-shaped body, curved stem, single leaf, coral cheek blush, and dark green line limbs clearly visible. Keep it clean, sparse, flat 2D, and readable.
```

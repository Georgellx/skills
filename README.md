# skills

我的 Codex / Claude Agent **技能收藏**。

每个子目录是一个独立的技能，至少包含一个 `SKILL.md`，可选 `references/`（按需加载的参考资料）、`scripts/`（可执行脚本）、`assets/`（输出用的模板等）。Agent 会根据每个技能的 `description` 自动判断何时调用，也可以手动 `/<skill-name>` 触发。目录名与触发名可能不同，以各目录中的 `SKILL.md` 为准。

---

## ⭐ 精选技能

| 技能 | 一句话说明 |
|---|---|
| [**self-understanding-coach**](./self-understanding-coach) | 引导式"自我认知法"教练，源自八木仁平《如何找到想做的事》——按"重要的事(价值观)→擅长的事(才能)→喜欢的事(热情)"一步步提问，帮你组合出"真正想做的事"。 |
| [**life-reset-coach**](./life-reset-coach) | 引导式"人生重启"教练，源自 Dan Koe《How to fix your entire life in 1 day》——先用"反愿景"逼出改变的能量，挖出行为背后的隐藏目标，再把目标落成一张"人生游戏地图"，用"只相信行动"逼你每天产出。 |
| [**content-digest**](./content-digest) | 内容消化官——读博主文章时一次产出三类资产：知识（按价值分诊进「文章笔记」）、提示词（进「提示词目录」）、想法/需求（可复刻的打法或被激发的点子进「产品想法」，自动抽「已验证样本证据」）。双模式：发来文章走完整消化、甩一句想法走低摩擦速记。由 `knowledge-ingest` + `capture-idea` 合并而来。 |
| [**obsidian-markdown**](./obsidian-markdown) | 写正确的 Obsidian 风格 Markdown——wikilink、嵌入(embed)、callout、properties(frontmatter)、注释等 Obsidian 专属语法，编辑 vault 里的 `.md` 文件时自动触发。第三方来源：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)（Obsidian 官方 CEO Steph Ango，MIT）。 |
| [**obsidian-bases**](./obsidian-bases) | 创建/编辑 Obsidian Bases（`.base`）——给笔记做数据库式视图：表格/卡片视图、按 tag/文件夹/属性/日期过滤、公式与汇总。第三方来源：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)。 |
| [**json-canvas**](./json-canvas) | 创建/编辑 JSON Canvas（`.canvas`）——节点、连线、分组，用来做思维导图、流程图、可视化画布，遵循 [JSON Canvas 1.0](https://jsoncanvas.org/spec/1.0/) 规范。第三方来源：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)。 |

## 📦 全部技能（77 个公开技能）

每个公开技能都在这里列出一句中文用途说明；说明来自对应目录 `SKILL.md` 的 `description`，点击名称可查看完整规则和参考资料。

| 技能 | 一句话说明 |
|---|---|
| [agent-reach](./agent-reach) | 互联网调研与搜索路由技能，用户要求查资料、搜索网页、了解平台讨论或核查链接时使用。 |
| [aihot](./aihot) | 查询 AI HOT 中文资讯，获取当天 AI 圈动态、模型发布、产品发布、论文和行业观点。 |
| [aihot-weekly](./aihot-weekly) | 生成并复盘“AI 退烧贴”微信公众号内容，覆盖选题、事实核查、文章、标题、封面、配图、排版和数据复盘。 |
| [brandalf](./brandalf) | 创建、修改和审查 Warp 或 Oz 品牌资产，包括发布页、文档、界面、提示词、社交素材、文案和演示稿。 |
| [brandkit](./brandkit) | 生成高端品牌规范板、标志系统、品牌身份展示稿和视觉世界提案。 |
| [brutalist-skill](./brutalist-skill) | 设计融合瑞士排版与军事终端美学的原始机械感界面，适合数据看板、作品集和编辑型网站。 |
| [check-impl-against-spec](./check-impl-against-spec) | 将 PR 实现与规格上下文对照，找出实质性偏差并写入 review.json。 |
| [competitive-analysis](./competitive-analysis) | 为个体创业者开展深度竞品分析，覆盖竞品地图、策略、机会、基准比较和定位。 |
| [composition-patterns](./composition-patterns) | 提供可扩展的 React 组合模式，用于组件库、复合组件、渲染属性、上下文提供者和可复用 API。 |
| [content-digest](./content-digest) | 消化外部文章并产出知识、可复用提示词、产品想法与已验证样本证据，保存到本地 Obsidian 知识库。 |
| [council](./council) | 组织多个模型或子智能体从不同角度调查同一问题，比较结论并形成最终建议。 |
| [create-pr](./create-pr) | 为当前分支在 Warp 仓库创建拉取请求。 |
| [de-ai-writing](./de-ai-writing) | 给中英文文本去 AI 味，进行活人感审读和改写，处理机械、过度润色、空泛或营销腔。 |
| [deep-competitor-analysis](./deep-competitor-analysis) | 深度竞品分析与应对方案工作流，适用于竞品调研、对标分析、产品对比和可直接上交的竞品报告。 |
| [defuddle](./defuddle) | 使用 Defuddle CLI 提取干净的网页 Markdown，去除导航和杂乱内容以节省上下文。 |
| [deploy-to-vercel](./deploy-to-vercel) | 将应用和网站部署到 Vercel，支持预览部署和正式发布。 |
| [design-md-first-ui](./design-md-first-ui) | 用设计优先、审美导向的流程构建、重设计和打磨高视觉要求的网页界面。 |
| [diagnose-ci-failures](./diagnose-ci-failures) | 使用 GitHub CLI 诊断 PR 的 CI 失败，提取日志并生成修复方案。 |
| [edit-talking-head-video](./edit-talking-head-video) | 从本地素材和参考视频规划、剪辑、加字幕、打包并验收中文 9:16 真人原声口播视频。 |
| [fix-errors](./fix-errors) | 修复 Warp Rust 代码库中的编译错误、代码检查问题和测试失败。 |
| [frontend-design](./frontend-design) | 创建具有高设计质量、区别于模板化 AI 风格的生产级前端界面。 |
| [gpt-tasteskill](./gpt-tasteskill) | 提供高级 UX/UI 与 GSAP 动效设计，强调布局变化、AIDA 结构、编辑型排版、Bento 网格和滚动触发器。 |
| [gsap-core](./gsap-core) | 提供 GSAP 核心 API 指南，覆盖补间、缓动、交错、响应式行为和减少动效。 |
| [gsap-frameworks](./gsap-frameworks) | 提供 Vue、Svelte 等非 React 框架中的 GSAP 使用指南，覆盖生命周期和清理。 |
| [gsap-performance](./gsap-performance) | 提供 GSAP 性能优化指南，覆盖变换、布局抖动、批处理和流畅的 60 帧动画。 |
| [gsap-plugins](./gsap-plugins) | 提供 GSAP 插件指南，覆盖 ScrollTo、ScrollSmoother、Flip、Draggable、SplitText、SVG 和物理插件。 |
| [gsap-react](./gsap-react) | 提供 React 和 Next.js 中的 GSAP 指南，覆盖 useGSAP、gsap.context 和资源清理。 |
| [gsap-scrolltrigger](./gsap-scrolltrigger) | 提供 GSAP ScrollTrigger 指南，覆盖滚动动画、固定、擦洗、视差和触发器。 |
| [gsap-timeline](./gsap-timeline) | 提供 GSAP 时间线指南，覆盖动画编排、时间线嵌套和播放控制。 |
| [gsap-utils](./gsap-utils) | 提供 GSAP 工具函数指南，覆盖 clamp、mapRange、normalize、random、snap、wrap 和 pipe。 |
| [human-writing](./human-writing) | 通用中文创作与改稿，覆盖知乎、公众号、故事、新闻、科普、教程、口播和演讲稿，强调自然中文与事实核验。 |
| [illustrated-story-video](./illustrated-story-video) | 将文章、脚本、故事想法或参考视频制作成静态插画短视频，并用 Remotion 和字幕完成交付。 |
| [image-to-code-skill](./image-to-code-skill) | 先生成并深度分析设计图，再实现高视觉要求的网站，使成品尽可能贴合设计。 |
| [imagegen-frontend-mobile](./imagegen-frontend-mobile) | 为 iOS、Android 和跨平台产品生成高级、原生感的移动端界面概念与流程图。 |
| [imagegen-frontend-web](./imagegen-frontend-web) | 生成高级、注重转化的网站设计参考图，并为每个页面区块单独生成横向图片。 |
| [implement-specs](./implement-specs) | 根据 PRODUCT.md 和 TECH.md 实现已批准功能，并保持规格与代码同步。 |
| [json-canvas](./json-canvas) | 创建和编辑带有节点、连线、分组与连接关系的 JSON Canvas 思维导图和流程图。 |
| [knowledge-ingest](./knowledge-ingest) | 将文章、提示词、方法、想法、复盘和洞见分类整理并保存到本地 Obsidian 知识库。 |
| [last30days](./last30days) | 研究过去 30 天内 Reddit、X、YouTube、TikTok、Hacker News、Polymarket、GitHub 和网页上的真实讨论。 |
| [leader](./leader) | 把一句话想法拆成 AI 智能体可独立执行的目标任务书，包含调研、验收、边界和断点续跑要求。 |
| [libtv-cli](./libtv-cli) | LibTV 官方 CLI 操作与运行手册，覆盖画布、项目、节点、模型、素材、工作区和脚本。 |
| [life-reset-coach](./life-reset-coach) | 引导式“人生重启”教练，用反愿景、隐藏目标、人生游戏地图和每日行动帮助用户改变现状。 |
| [minimalist-skill](./minimalist-skill) | 设计温暖单色、强调排版对比、扁平 Bento 网格的编辑型界面，避免渐变和厚重阴影。 |
| [obsidian-bases](./obsidian-bases) | 创建和编辑 Obsidian Bases，配置视图、过滤器、公式和汇总。 |
| [obsidian-cli](./obsidian-cli) | 通过 Obsidian CLI 管理笔记、任务、属性、插件、主题，并进行调试和页面检查。 |
| [obsidian-markdown](./obsidian-markdown) | 创建和编辑 Obsidian 风格 Markdown，处理双链、嵌入、标注、属性和其他专属语法。 |
| [orange-line-illustration](./orange-line-illustration) | 生成纽约客风格极简编辑插画，采用细黑线、大面积留白和单一橙色强调。 |
| [output-skill](./output-skill) | 强制输出完整内容，禁止占位符，并妥善处理超出上下文限制时的分段输出。 |
| [perry-article-illustrations](./perry-article-illustrations) | 生成 Perry 风格的中文正文配图、文章插图、封面、分镜清单和带少量中文批注的图片。 |
| [pr-walkthrough](./pr-walkthrough) | 为 PR、系统组件、数据流和依赖关系生成静态交互式 D3 可视化导览。 |
| [produce-cigar-douyin-video](./produce-cigar-douyin-video) | 将中文雪茄知识主题、文字、截图或用户图片制作成事实核查、电影感、真实运动的抖音视频。 |
| [react-best-practices](./react-best-practices) | 提供来自 Vercel 工程团队的 React 与 Next.js 性能优化实践。 |
| [react-native-skills](./react-native-skills) | 提供 React Native 与 Expo 的性能实践，覆盖组件、列表、动画和原生模块。 |
| [react-view-transitions](./react-view-transitions) | 指导使用 React View Transition 实现路由、共享元素、列表和界面状态的原生感过渡动画。 |
| [redesign-skill](./redesign-skill) | 在不破坏功能的前提下升级现有网站和应用，去除模板化 AI 风格并提升品质。 |
| [reproduce-bug-report](./reproduce-bug-report) | 启动 Oz 云端智能体复现界面问题，采集视觉证据并输出复现结果。 |
| [resolve-merge-conflicts](./resolve-merge-conflicts) | 通过提取未解决路径、冲突块和紧凑差异来处理 Git 合并冲突。 |
| [respond-to-pr-comments-in-blocklist](./respond-to-pr-comments-in-blocklist) | 获取 PR 审查意见，收集逐条响应决策，应用修复，并在发布前预览回复。 |
| [review-pr](./review-pr) | 审查 PR 差异，并为发布流程生成结构化的 review.json 反馈。 |
| [save-webpage-to-obsidian](./save-webpage-to-obsidian) | 将公开或需登录的网页、课程和文章保存为带图片的有序 Obsidian Markdown 笔记。 |
| [self-potential-venture](./self-potential-venture) | 引导自我潜能挖掘创业版流程，把经历、材料、反馈和技能转化为副业或创业方向假设并低成本验证。 |
| [self-understanding-coach](./self-understanding-coach) | 引导式“自我认知法”教练，按价值观、才能、热情的顺序帮助用户找到“真正想做的事”。 |
| [soft-skill](./soft-skill) | 通过字体、间距、阴影、卡片结构和动画规则，指导制作具有高级代理商质感的网站。 |
| [spec-driven-implementation](./spec-driven-implementation) | 先编写 PRODUCT.md 和 TECH.md，再以规格优先的方式实现功能并保持两者同步。 |
| [stitch-skill](./stitch-skill) | 为 Google Stitch 生成 DESIGN.md，用严格排版、色彩、非对称布局和微动效建立高级 UI 规范。 |
| [storage-analyzer](./storage-analyzer) | 只读分析 macOS 和 Windows 磁盘空间，找出占用大户并生成可执行的交互式 HTML 处置报告。 |
| [taste-skill](./taste-skill) | 为落地页、作品集和重设计提供反模板化前端指导，强调真实设计系统和先审查后实现。 |
| [taste-skill-v1](./taste-skill-v1) | 提供旧版 taste-skill，适用于需要完全兼容旧行为的项目。 |
| [update-skill](./update-skill) | 创建或更新 SKILL.md，处理技能结构、前置元数据和使用指导。 |
| [validate-changes-match-specs](./validate-changes-match-specs) | 验证分支或 PR 实现是否符合产品、技术、安全及相关规格。 |
| [vercel-cli-with-tokens](./vercel-cli-with-tokens) | 使用访问令牌而非交互式认证来部署和管理 Vercel 项目。 |
| [video-use](./video-use) | 通过对话完成视频转写、剪辑、调色、叠加动画、字幕和交付。 |
| [web-design-guidelines](./web-design-guidelines) | 按 Web 界面规范审查 UI 代码，覆盖可访问性、用户体验和设计最佳实践。 |
| [wechat-news-cover](./wechat-news-cover) | 根据照片和最新新闻信息制作中文 16:9 编辑型封面，保持克制的视觉语言。 |
| [write-product-spec](./write-product-spec) | 为重要的用户功能编写 PRODUCT.md，重点描述行为和验收标准。 |
| [write-tech-spec](./write-tech-spec) | 研究代码库、实现约束和架构后编写 TECH.md 技术规格。 |
| [xiaohongshu-profile-spider](./xiaohongshu-profile-spider) | 安装并运行 Spider_XHS 抓取小红书用户主页，保存媒体和 Excel 文件并安全恢复中断任务。 |

> `job-application-coach` 是本地专用 skill，按仓库规则不会公开到这里。

---

## 🧭 self-understanding-coach 详解

### 这是什么

把八木仁平《如何找到想做的事》里的"自我认知法"做成一段**多轮引导对话**。它不会直接给你答案，而是像教练一样**通过提问、倾听、反射**，帮你从自己身上挖出方向。

### 核心公式

```
喜欢的事 × 擅长的事             = 想做的事
喜欢的事 × 擅长的事 × 重要的事   = 真正想做的事
```

三大支柱：

- **重要的事（价值观 / Why）**：想以什么**状态**生活（自由地、安心地、热情地……）。人生指南针。
- **擅长的事（才能 / How）**：天生就比别人做得好、做起来不累的**方式**（深入思考、体察他人、把事讲清楚……）。不是后天学的技能知识。
- **喜欢的事（热情 / What）**：感兴趣、有好奇心的**领域**（AI、心理学、健康、棒球……）。

寻找顺序固定：**重要的事 → 擅长的事 → 喜欢的事 → 组合出"真正想做的事" → 找实现手段。**

### 它做得好的地方

- 一次只推进一步，**不会把一堆问题机械地砸给你**；
- 每收到回答**先提炼关键词、再前进**（你给碎片，它帮你拼图）；
- 主动**点破模式和矛盾**（比如"你向往的"和"你被教导的"在打架）；
- 用书里的**具体检验工具**（真假价值观、以他人→以自我、缺点→优点、兴趣vs有用），而不是空说"倾听内心"；
- 全程以**"假设"**措辞、温暖不说教。

### 何时会触发

说出类似下面的话，它会自动启动（中英文都行）：

> "不知道自己想做什么" · "对工作很迷茫" · "想转行但没方向" · "想找到自己的热爱/天赋" · "感觉像笼子里的金丝雀" · "I don't know what to do with my career" · "find my passion"

也可以直接 `/self-understanding-coach` 手动调用。

---

## 🧭 life-reset-coach 详解

### 这是什么

把 Dan Koe《How to fix your entire life in 1 day》的理论做成一段**犀利、直接、不留情面的多轮对话**（像作者本人那样）。它不哄你，而是带你先狠狠看清自己绝不想要的人生，再把改变落成可执行的行动。

### 核心信念

> **改变的不是行为，是身份。** 你不是靠意志力硬撑，而是先成为"那个会自然这么做的人"。

### 它怎么带你走

1. **反愿景**：狠狠看清你绝不想要的那种人生，逼出改变的能量；
2. **挖隐藏目标**：你的拖延 / 逃避，其实在偷偷完成某个目标（通常是"安全感"）——点破它；
3. **人生游戏地图**：把目标落成 6 个部件——反愿景 / 愿景 / 一年主线 / 一个月 Boss 战 / 每日杠杆 / 规则；
4. **只相信行动**：逼你每天产出一个"别人能看到、能反应"的东西，启动"行动→反馈→调整"的掌舵循环。

### 何时会触发

说出类似下面的话，它会自动启动（中英文都行）：

> "受够了现状" · "明明想改变却总坚持不下来" · "反复立flag又放弃" · "想重启人生" · "想被狠狠点醒" · "知道方向但卡在行动上" · "fix my life" · "reset my life"

也可以直接 `/life-reset-coach` 手动调用。

### 和 self-understanding-coach 的分工

- **self-understanding-coach（八木仁平 / ikigai）**：适合"完全不知道想做什么、要从零系统梳理价值观"。
- **life-reset-coach（Dan Koe）**：适合"已经受够现状、想被点醒并立刻把改变落成行动"。

---

## 📥 content-digest 详解

### 这是什么

一个**内容消化流水线**，专为"学习博主文章、复刻已验证的方法和商业模式来赚钱"设计。你发一篇文章 / 链接 / 长文，它在**同一次阅读里产出三类资产**，并把"能复刻变现的打法"钉在真实样本上，而不是飘成空想。

### 三类产物

- **知识** → 价值分诊（A 留全文+解读 / B 留全文+干净重写 / C 只留提炼+来源）后进「文章笔记」。
- **提示词** → 文中可复制的提示词抽进「提示词目录」，文章里只留指针双链、不重复抄。
- **想法/需求** → 博主可复刻的打法、或被激发的点子进「产品想法」，**自动抽「已验证样本证据」**（粉丝/收入/销量），并区分这是"想法"还是观察到的"真实需求"。

### 双模式

- **消化模式**（有文章）：去重 → 价值分诊 → 拆三类产物 → 分类路由 → 双链 → 验收清理。
- **速记模式**（只有你一句话的想法）：低摩擦捕捉，别盘问，直接进「产品想法」+ 更新索引看板。

> ⚠️ 这个 skill 把某个具体知识库的目录地图写死在 `SKILL.md` / `references/` 里（路径、提示词分类表、模板）。换库使用时先改顶部「知识库地图」。frontmatter 遵循库统一规范（type 8 值词表 / tags 块列表 / related_notes 加引号真实文件名）。

### 何时会触发

> 发来文章 / 链接 / Clippings 路径 · "帮我入库 / 整理这篇 / 这篇值不值得存" · "把提示词收进库" · "这个博主的打法能不能复刻" · "我有个想法 / 我想做一个 XX / 以后可以做 XX"

也可以直接 `/content-digest` 手动调用。

> 由 `knowledge-ingest`（知识入库）+ `capture-idea`（想法捕捉）合并而来——因为读一篇博主文章常常同时产出"知识"和"可复刻的赚钱点子"，分两个 skill 会漏掉后者。

---

## 🚀 安装与使用

把某个技能目录复制到你使用的 Agent 的个人技能目录：

- **Codex（Windows）**：`C:\Users\<你>\.codex\skills\`
- **Codex（macOS / Linux）**：`~/.codex/skills/`

```bash
git clone https://github.com/Georgellx/skills.git
# Windows (PowerShell)
Copy-Item -Recurse skills\self-understanding-coach "$env:USERPROFILE\.codex\skills\"
# macOS / Linux
cp -r skills/self-understanding-coach ~/.codex/skills/
```

之后在 Codex 里 `/self-understanding-coach` 调用，或在相关话题下让它自动触发；其他 Agent 请使用对应的 skills 目录。

---

## ➕ 新增技能

1. 在仓库根目录新建一个文件夹 `<your-skill>/`，写好 `SKILL.md`（含 `name` 和 `description` 两个必填的 frontmatter 字段）。
2. 在上面的"Skills 列表"里加一行。
3. 提交并推送：
   ```bash
   git add -A
   git commit -m "Add <your-skill>"
   git push
   ```

想从零做一个高质量 skill，推荐用官方的 `skill-creator`（draft → 测试 → 评审 → 迭代）。

---

## 🙏 致谢

`self-understanding-coach` 的方法论完全源自 **八木仁平《如何找到想做的事》**（徐艺菊 译，机械工业出版社）。

`life-reset-coach` 的方法论完全源自 **Dan Koe《How to fix your entire life in 1 day》**（[@thedankoe](https://x.com/thedankoe)）。

本仓库仅把上述流程整理为可复用的对话框架，强烈建议阅读原作以获得完整语境。

## 📄 License

[MIT](./LICENSE) © 2026 Georgellx

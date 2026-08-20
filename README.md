# skills

我的 Codex / Claude Agent **skills 收藏**。

每个子目录是一个独立的 skill，至少包含一个 `SKILL.md`，可选 `references/`（按需加载的参考资料）、`scripts/`（可执行脚本）、`assets/`（输出用的模板等）。Agent 会根据每个 skill 的 `description` 自动判断何时调用，也可以手动 `/<skill-name>` 触发。目录名与触发名可能不同，以各目录中的 `SKILL.md` 为准。

---

## ⭐ 精选 Skills

| Skill | 一句话说明 |
|---|---|
| [**self-understanding-coach**](./self-understanding-coach) | 引导式"自我认知法"教练，源自八木仁平《如何找到想做的事》——按"重要的事(价值观)→擅长的事(才能)→喜欢的事(热情)"一步步提问，帮你组合出"真正想做的事"。 |
| [**life-reset-coach**](./life-reset-coach) | 引导式"人生重启"教练，源自 Dan Koe《How to fix your entire life in 1 day》——先用"反愿景"逼出改变的能量，挖出行为背后的隐藏目标，再把目标落成一张"人生游戏地图"，用"只相信行动"逼你每天产出。 |
| [**content-digest**](./content-digest) | 内容消化官——读博主文章时一次产出三类资产：知识（按价值分诊进「文章笔记」）、提示词（进「提示词目录」）、想法/需求（可复刻的打法或被激发的点子进「产品想法」，自动抽「已验证样本证据」）。双模式：发来文章走完整消化、甩一句想法走低摩擦速记。由 `knowledge-ingest` + `capture-idea` 合并而来。 |
| [**obsidian-markdown**](./obsidian-markdown) | 写正确的 Obsidian 风格 Markdown——wikilink、嵌入(embed)、callout、properties(frontmatter)、注释等 Obsidian 专属语法，编辑 vault 里的 `.md` 文件时自动触发。第三方来源：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)（Obsidian 官方 CEO Steph Ango，MIT）。 |
| [**obsidian-bases**](./obsidian-bases) | 创建/编辑 Obsidian Bases（`.base`）——给笔记做数据库式视图：表格/卡片视图、按 tag/文件夹/属性/日期过滤、公式与汇总。第三方来源：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)。 |
| [**json-canvas**](./json-canvas) | 创建/编辑 JSON Canvas（`.canvas`）——节点、连线、分组，用来做思维导图、流程图、可视化画布，遵循 [JSON Canvas 1.0](https://jsoncanvas.org/spec/1.0/) 规范。第三方来源：[kepano/obsidian-skills](https://github.com/kepano/obsidian-skills)。 |

## 📦 全部 Skills（77 个公开 skill）

每个公开 skill 都在这里列出一句用途说明；说明来自对应目录 `SKILL.md` 的 `description`，点击名称可查看完整规则和参考资料。

| Skill | 一句话说明 |
|---|---|
| [agent-reach](./agent-reach) | MUST USE when user wants to 调研/research/搜索/search/查/找/look up anything on the internet — e.g. 全网调研 X / 帮我调研一下 X / 查一下 X / 搜搜 X / 看看大家怎么评价 X / X 上有什么讨论 / research this topic。… |
| [aihot](./aihot) | AI HOT (aihot.virxact.com) 中文 AI 资讯查询 Skill。当用户想知道“今天 AI 圈有什么”、AI 日报、AI 资讯、AI 热点或最近的模型与产品动态时使用。… |
| [aihot-weekly](./aihot-weekly) | 生成并复盘“AI 退烧贴”微信公众号科技内容，覆盖 AI/Agent 新闻选题、事实核查、实操文章、标题、封面、正文配图、移动端排版、发布草稿与数据复盘。 |
| [brandalf](./brandalf) | Guides creation, revision, and review of Warp- or Oz-branded assets, including launch pages, docs, UI mockups, prompts, social assets, copy, and presentations. |
| [brandkit](./brandkit) | Premium brand-kit image generation for high-end brand-guidelines boards, logo systems, identity decks, and visual-world presentations. |
| [brutalist-skill](./brutalist-skill) | Raw mechanical interfaces combining Swiss typographic print with military terminal aesthetics for data-heavy dashboards, portfolios, and editorial sites. |
| [check-impl-against-spec](./check-impl-against-spec) | Compare a pull request implementation against spec context and report material mismatches in review.json. |
| [competitive-analysis](./competitive-analysis) | Deep competitive analysis for solopreneur businesses, including competitor mapping, strategy, gaps, benchmarking, and positioning. |
| [composition-patterns](./composition-patterns) | React composition patterns for flexible component libraries and reusable APIs, including compound components, render props, and context providers. |
| [content-digest](./content-digest) | 消化外部文章并产出知识、可复用提示词、产品想法与已验证样本证据，保存到本地 Obsidian 知识库。 |
| [council](./council) | Run a model-diverse subagent council to investigate one problem from multiple perspectives, compare findings, and produce a recommendation. |
| [create-pr](./create-pr) | Create a pull request in the Warp repository for the current branch. |
| [de-ai-writing](./de-ai-writing) | 给中英文文本做去 AI 味、活人感审读和改写，处理机械、过度润色、空泛或营销腔。 |
| [deep-competitor-analysis](./deep-competitor-analysis) | 深度竞品分析与应对方案工作流，适用于竞品调研、对标分析、产品对比和可直接上交的竞品报告。 |
| [defuddle](./defuddle) | Extract clean Markdown from web pages with Defuddle CLI, removing clutter and navigation to save tokens. |
| [deploy-to-vercel](./deploy-to-vercel) | Deploy applications and websites to Vercel, including preview deployments and production releases. |
| [design-md-first-ui](./design-md-first-ui) | Drives a design-first, taste-aware UI workflow for building, redesigning, and polishing visually important web interfaces. |
| [diagnose-ci-failures](./diagnose-ci-failures) | Diagnose CI failures for a PR using GitHub CLI, extract logs, and generate a fix plan. |
| [edit-talking-head-video](./edit-talking-head-video) | Plan, edit, subtitle, package, and verify Chinese 9:16真人原声口播视频 from local footage and reference videos. |
| [fix-errors](./fix-errors) | Fix compilation errors, linting issues, and test failures in the Warp Rust codebase. |
| [frontend-design](./frontend-design) | Create distinctive, production-grade frontend interfaces with high design quality and without generic AI aesthetics. |
| [gpt-tasteskill](./gpt-tasteskill) | Elite UX/UI and advanced GSAP motion engineering with layout variance, AIDA structure, editorial typography, bento grids, and ScrollTriggers. |
| [gsap-core](./gsap-core) | Official GSAP core API guidance covering tweens, easing, stagger, responsive behavior, and reduced motion. |
| [gsap-frameworks](./gsap-frameworks) | Official GSAP guidance for Vue, Svelte, and other non-React frameworks, including lifecycle and cleanup. |
| [gsap-performance](./gsap-performance) | Official GSAP performance guidance covering transforms, layout thrashing, batching, and smooth 60fps animation. |
| [gsap-plugins](./gsap-plugins) | Official GSAP plugin guidance covering ScrollTo, ScrollSmoother, Flip, Draggable, SplitText, SVG, physics, and related plugins. |
| [gsap-react](./gsap-react) | Official GSAP guidance for React and Next.js, including useGSAP, gsap.context, and cleanup. |
| [gsap-scrolltrigger](./gsap-scrolltrigger) | Official GSAP ScrollTrigger guidance for scroll-linked animation, pinning, scrubbing, parallax, and triggers. |
| [gsap-timeline](./gsap-timeline) | Official GSAP timeline guidance for sequencing animations, nesting timelines, and playback. |
| [gsap-utils](./gsap-utils) | Official GSAP utilities guidance covering clamp, mapRange, normalize, random, snap, wrap, pipe, and related helpers. |
| [human-writing](./human-writing) | 通用中文创作与改稿，覆盖知乎、公众号、故事、新闻、科普、教程、口播和演讲稿，强调自然中文与事实核验。 |
| [illustrated-story-video](./illustrated-story-video) | Build static illustrated short-video projects from articles, scripts, story ideas, or reference videos with Remotion and subtitles. |
| [image-to-code-skill](./image-to-code-skill) | Generate and deeply analyze design images first, then implement visually important websites to match them closely. |
| [imagegen-frontend-mobile](./imagegen-frontend-mobile) | Generate premium app-native mobile screen concepts and flows for iOS, Android, and cross-platform products. |
| [imagegen-frontend-web](./imagegen-frontend-web) | Generate premium, conversion-aware website design references with one separate horizontal image for every section. |
| [implement-specs](./implement-specs) | Implement approved features from PRODUCT.md and TECH.md while keeping specs and code aligned. |
| [json-canvas](./json-canvas) | Create and edit JSON Canvas files with nodes, edges, groups, and connections for mind maps and flowcharts. |
| [knowledge-ingest](./knowledge-ingest) | Classify and save articles, prompts, methods, ideas, retrospectives, and insights into a local Obsidian vault. |
| [last30days](./last30days) | Research what people actually say about a topic in the last 30 days across Reddit, X, YouTube, TikTok, Hacker News, Polymarket, GitHub, and the web. |
| [leader](./leader) | 把一句话想法拆成 AI agent 可独立执行的目标任务书，含调研、验收、边界和断点续跑要求。 |
| [libtv-cli](./libtv-cli) | LibTV 官方 CLI 操作与运行手册，覆盖画布、项目、节点、模型、素材、工作区和脚本。 |
| [life-reset-coach](./life-reset-coach) | 引导式“人生重启”教练，用反愿景、隐藏目标、人生游戏地图和每日行动帮助用户改变现状。 |
| [minimalist-skill](./minimalist-skill) | Clean editorial-style interfaces with warm monochrome palettes, typographic contrast, flat bento grids, and no gradients or heavy shadows. |
| [obsidian-bases](./obsidian-bases) | Create and edit Obsidian Bases with views, filters, formulas, and summaries. |
| [obsidian-cli](./obsidian-cli) | Interact with Obsidian vaults through the CLI to manage notes, tasks, properties, plugins, themes, and debugging. |
| [obsidian-markdown](./obsidian-markdown) | Create and edit Obsidian Flavored Markdown with wikilinks, embeds, callouts, properties, and other Obsidian syntax. |
| [orange-line-illustration](./orange-line-illustration) | Generate minimalist New Yorker-style editorial illustrations with thin black ink, white space, and one orange accent. |
| [output-skill](./output-skill) | Enforce complete, unabridged output, ban placeholders, and handle token-limit splits cleanly. |
| [perry-article-illustrations](./perry-article-illustrations) | 生成 Perry 风格的中文正文配图、文章插图、封面、shot list 和带少量中文批注的图片。 |
| [pr-walkthrough](./pr-walkthrough) | Generate static interactive D3 walkthroughs of pull requests, system components, data flow, and dependencies. |
| [produce-cigar-douyin-video](./produce-cigar-douyin-video) | 将中文雪茄知识主题、文字、截图或用户图片制作成事实核查、电影感、真实运动的抖音视频。 |
| [react-best-practices](./react-best-practices) | React and Next.js performance optimization guidelines from Vercel Engineering. |
| [react-native-skills](./react-native-skills) | React Native and Expo best practices for performant components, lists, animations, and native modules. |
| [react-view-transitions](./react-view-transitions) | Guide smooth native-feeling React View Transition animations for routes, shared elements, lists, and UI states. |
| [redesign-skill](./redesign-skill) | Upgrade existing websites and apps to premium quality while preserving functionality and removing generic AI patterns. |
| [reproduce-bug-report](./reproduce-bug-report) | Launch Oz cloud agents with computer use to reproduce UI bugs, capture visual evidence, and report findings. |
| [resolve-merge-conflicts](./resolve-merge-conflicts) | Resolve Git merge conflicts by extracting only unresolved paths, hunks, and compact diffs. |
| [respond-to-pr-comments-in-blocklist](./respond-to-pr-comments-in-blocklist) | Fetch PR review comments, collect response decisions, apply fixes, and preview replies before posting. |
| [review-pr](./review-pr) | Review a PR diff and write structured feedback to review.json for the publishing workflow. |
| [save-webpage-to-obsidian](./save-webpage-to-obsidian) | Save public or authenticated webpages and course lessons as ordered Obsidian Markdown notes with images. |
| [self-potential-venture](./self-potential-venture) | 引导自我潜能挖掘创业版流程，把经历、材料、反馈和技能转化为副业或创业方向假设并低成本验证。 |
| [self-understanding-coach](./self-understanding-coach) | 引导式“自我认知法”教练，按价值观、才能、热情的顺序帮助用户找到“真正想做的事”。 |
| [soft-skill](./soft-skill) | Teach high-end agency web design through exact typography, spacing, shadows, card structures, and animations. |
| [spec-driven-implementation](./spec-driven-implementation) | Drive a spec-first workflow by writing PRODUCT.md and TECH.md before implementation and keeping them aligned. |
| [stitch-skill](./stitch-skill) | Generate agent-friendly DESIGN.md files for Google Stitch with premium, anti-generic UI standards. |
| [storage-analyzer](./storage-analyzer) | 只读分析 macOS / Windows 磁盘空间，找出占用大户并生成可执行的交互式 HTML 处置报告。 |
| [taste-skill](./taste-skill) | Anti-slop frontend guidance for landing pages, portfolios, and redesigns with real design systems and audit-first workflows. |
| [taste-skill-v1](./taste-skill-v1) | Original v1 taste-skill for projects that need exact backward-compatible behavior. |
| [update-skill](./update-skill) | Create or update SKILL.md files by generating, editing, or refining skill structure, frontmatter, and guidance. |
| [validate-changes-match-specs](./validate-changes-match-specs) | Validate branch or PR implementations against product, technical, security, and related specs. |
| [vercel-cli-with-tokens](./vercel-cli-with-tokens) | Deploy and manage Vercel projects with access tokens instead of interactive CLI authentication. |
| [video-use](./video-use) | Edit any video by conversation, including transcription, cutting, color grading, overlays, subtitles, and delivery. |
| [web-design-guidelines](./web-design-guidelines) | Review UI code for Web Interface Guidelines, accessibility, UX, and design best practices. |
| [wechat-news-cover](./wechat-news-cover) | Create Chinese 16:9 editorial covers from supplied photos and current-news information with restrained visual language. |
| [write-product-spec](./write-product-spec) | Write PRODUCT.md specs for substantial user-facing features, focused on behavior and validation. |
| [write-tech-spec](./write-tech-spec) | Write TECH.md specs after researching the codebase, implementation constraints, and architecture. |
| [xiaohongshu-profile-spider](./xiaohongshu-profile-spider) | Install and run Spider_XHS to crawl Xiaohongshu user profiles, save media and Excel files, and resume crawls safely. |

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

把某个 skill 目录复制到你使用的 Agent 的个人 skills 目录：

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

## ➕ 新增 skill

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

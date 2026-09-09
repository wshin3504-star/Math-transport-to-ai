# -*- coding: utf-8 -*-
"""
生成「几何分析专业转向 AI/Agent 就业市场」方案 Word 文档
"""

from docx import Document
from docx.shared import Pt, Cm, RGBColor, Inches
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

# ── 颜色定义 ──
DARK_BLUE  = RGBColor(0x1F, 0x3D, 0x7A)
MED_BLUE   = RGBColor(0x2E, 0x5C, 0x9E)
ACCENT_RED = RGBColor(0xC0, 0x39, 0x2B)
DARK_GREEN = RGBColor(0x1A, 0x6B, 0x3C)
GRAY       = RGBColor(0x55, 0x55, 0x55)
BLACK      = RGBColor(0x00, 0x00, 0x00)

# ── 工具函数 ──

def set_cell_shading(cell, color_hex):
    """设置单元格底色"""
    shading = cell._element.get_or_add_tcPr()
    shading_elm = shading.makeelement(qn('w:shd'), {
        qn('w:val'): 'clear',
        qn('w:color'): 'auto',
        qn('w:fill'): color_hex
    })
    shading.append(shading_elm)


def add_styled_paragraph(doc, text, *, size=11, bold=False, color=BLACK,
                         space_before=0, space_after=6, line_spacing=1.5,
                         first_indent_cm=None, alignment=None):
    """添加带样式的段落"""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(space_before)
    p.paragraph_format.space_after = Pt(space_after)
    p.paragraph_format.line_spacing = line_spacing
    if first_indent_cm is not None:
        p.paragraph_format.first_line_indent = Cm(first_indent_cm)
    if alignment is not None:
        p.alignment = alignment
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.bold = bold
    run.font.color.rgb = color
    run.font.name = '微软雅黑'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    return p


def add_heading_custom(doc, text, level=1):
    """自定义标题"""
    sizes  = {1: 16, 2: 13, 3: 11.5}
    colors = {1: DARK_BLUE, 2: MED_BLUE, 3: DARK_GREEN}
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(18 if level == 1 else 12)
    p.paragraph_format.space_after  = Pt(6)
    p.paragraph_format.line_spacing = 1.3
    run = p.add_run(text)
    run.font.size = Pt(sizes.get(level, 11))
    run.font.bold = True
    run.font.color.rgb = colors.get(level, MED_BLUE)
    run.font.name = '微软雅黑'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    return p


def add_bullet(doc, text, *, size=10.5, bold_prefix=None, color=BLACK,
               space_after=3, indent_cm=0.75):
    """添加项目符号段落"""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(space_after)
    p.paragraph_format.line_spacing = 1.4
    p.paragraph_format.left_indent  = Cm(indent_cm)
    p.paragraph_format.first_line_indent = Cm(-0.4)
    # 手动符号
    bullet_run = p.add_run("▪ ")
    bullet_run.font.size = Pt(size)
    bullet_run.font.color.rgb = MED_BLUE
    bullet_run.font.bold = True
    bullet_run.font.name = '微软雅黑'
    bullet_run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

    if bold_prefix:
        bp = p.add_run(bold_prefix)
        bp.font.size = Pt(size)
        bp.font.bold = True
        bp.font.color.rgb = color
        bp.font.name = '微软雅黑'
        bp._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.name = '微软雅黑'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    return p


def add_numbered(doc, text, num, *, size=10.5, color=BLACK, space_after=4):
    """添加编号段落"""
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(space_after)
    p.paragraph_format.line_spacing = 1.4
    p.paragraph_format.left_indent  = Cm(0.75)
    p.paragraph_format.first_line_indent = Cm(-0.5)
    num_run = p.add_run(f"{num}. ")
    num_run.font.size = Pt(size)
    num_run.font.bold = True
    num_run.font.color.rgb = MED_BLUE
    num_run.font.name = '微软雅黑'
    num_run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    run = p.add_run(text)
    run.font.size = Pt(size)
    run.font.color.rgb = color
    run.font.name = '微软雅黑'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    return p


# ── 主文档构建 ──

doc = Document()

# 页边距
for section in doc.sections:
    section.top_margin    = Cm(2.0)
    section.bottom_margin = Cm(2.0)
    section.left_margin   = Cm(2.5)
    section.right_margin  = Cm(2.5)

# 默认字体
style = doc.styles['Normal']
style.font.name = '微软雅黑'
style.font.size = Pt(11)
style._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

# ═══════════════════════════════════════════
#  封面标题
# ═══════════════════════════════════════════

add_styled_paragraph(
    doc, "从几何分析到 AI Agent：",
    size=22, bold=True, color=DARK_BLUE,
    space_before=60, space_after=4, line_spacing=1.3, alignment=WD_ALIGN_PARAGRAPH.CENTER
)
add_styled_paragraph(
    doc, "数学系研二学生转向 AI/Agent 就业市场方案",
    size=15, bold=True, color=MED_BLUE,
    space_after=20, line_spacing=1.3, alignment=WD_ALIGN_PARAGRAPH.CENTER
)
add_styled_paragraph(
    doc, "—— 基于无独立算力、无导师支持的资源约束条件 ——",
    size=10, color=GRAY,
    space_after=40, alignment=WD_ALIGN_PARAGRAPH.CENTER
)

# ═══════════════════════════════════════════
#  一、目标校准
# ═══════════════════════════════════════════

add_heading_custom(doc, "一、目标校准：「发一篇 CCF-A」是学术赛道的答案，不是就业市场的答案", level=1)

add_styled_paragraph(
    doc,
    "你老师给的建议在申 PhD 的语境下是对的，但对就业来说权重完全不同。"
    "翻看今年正在招的 27 届校招 JD（智谱 GLM Code Agent、上海人工智能实验室大模型/Agentic RL、OPPO 大模型智能体等），"
    "实际筛选权重是：",
    size=11, first_indent_cm=0.74, space_after=6
)

# 高亮权重排序
p = doc.add_paragraph()
p.paragraph_format.space_before = Pt(2)
p.paragraph_format.space_after  = Pt(8)
p.paragraph_format.line_spacing = 1.5
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run("实习经历（return offer）＞ 工程能力和可展示项目 ＞ 论文")
run.font.size = Pt(11.5)
run.font.bold = True
run.font.color.rgb = ACCENT_RED
run.font.name = '微软雅黑'
run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

add_styled_paragraph(doc, "论文基本写的是「有 NeurIPS / ICML / ICLR 发表者优先」——是加分项，不是硬门槛。", size=11, first_indent_cm=0.74, space_after=10)

add_styled_paragraph(doc, "几个你需要接受的现实判断：", size=11, bold=True, first_indent_cm=0.74, space_after=4)

add_numbered(doc,
    "单兵、无导师、无算力、一年时间，一作 CCF-A 概率很低（个位数百分比），把它当唯一目标是豪赌。"
    "但 CCF-A 可以在工业界实习期间跟 mentor 合作产出——实习才是「没有资源」这个问题的总解。",
    1, size=10.5)
add_numbered(doc,
    "Workshop 论文 / arXiv 预印本 + 高质量开源代码，对秋招简历筛选已经够用，"
    "尤其配上 985 数学背景的牌子。",
    2, size=10.5)
add_numbered(doc,
    "时间线：如果你是三年制学硕，现在研二（2026 秋），你是 28 届，秋招在 2027 年 9–11 月，满打满算约 12 个月。"
    "请务必先去教务确认你是 27 届还是 28 届——两年半/两年制的话秋招就在此刻，方案要压缩执行。",
    3, size=10.5, color=ACCENT_RED)

# ═══════════════════════════════════════════
#  二、你的真实资产
# ═══════════════════════════════════════════

add_heading_custom(doc, "二、你的真实资产：几何分析背景在哪条 AI 赛道上是稀缺的", level=1)

add_styled_paragraph(
    doc,
    "纯数学学生转 Agent / AI 最容易犯的错，是去和 CS 学生拼工程框架（LangChain、RAG、CRUD 式 agent 开发）——那是以短击长。"
    "你的资产是数学成熟度、流形 / PDE / 分析训练、以及「懂真数学」这件事本身。三个高价值交叉点：",
    size=11, first_indent_cm=0.74, space_after=10
)

# --- 首选 ---
add_heading_custom(doc, "首选：LLM × 形式化数学 / 定理证明 Agent（Lean 4 方向）", level=2)

add_styled_paragraph(doc, "这是目前为你这种背景量身定做的窄门，理由很硬：", size=11, first_indent_cm=0.74, space_after=4)

add_bullet(doc, "proof search agent 主要靠 API 调用（DeepSeek / Qwen API 百万 token 几块钱）+ 单卡跑 7B 模型 LoRA。"
    "一个独立开发者项目 ensemble-prover 纯靠 GPT-5、DeepSeek-V4 等 API 模型，"
    "2026 年 8 月已经在 PutnamBench 榜上刷到 65 道 Putnam 题——证明无资源个人完全能做一线研究。",
    bold_prefix="算力需求极低：")
add_bullet(doc, "形式化需要人懂定理本身。Mathlib 里分析/几何的覆盖远不如代数完整，"
    "几何分析几乎是空白——这就是你的护城河，别人抄不走。",
    bold_prefix="真正吃数学功底：")
add_bullet(doc, "DeepSeek-Prover-V2（2025）把 miniF2F 刷到 88.9%；"
    "2026 年 2 月 AI 形式化了 Viazovska 的菲尔兹奖工作（8/24 维球堆积——这本身就是几何！）；"
    "2026 年 9 月 4 日 Claude 11 天形式化费马大定理。DeepSeek、Anthropic、Google 都在重金投入。",
    bold_prefix="赛道正爆：")
add_bullet(doc, "定理证明搜索 = 任务分解 + 工具调用（Lean verifier）+ 环境反馈 + 策略规划，"
    "是最纯粹的 agentic planning，且有可验证奖励——面试时你讲的故事就是「我做的是 Agent」。",
    bold_prefix="它就是 Agent 研究：")

# --- 次选 ---
add_heading_custom(doc, "次选：数学推理 / Agentic RL", level=2)

add_styled_paragraph(
    doc,
    "可验证奖励强化学习（RLVR、GRPO 那一套）中，数学题是标准训练场。"
    "JD 里「Agentic RL、工具调用、轨迹/奖励建模」正在成为热点（上海人工智能实验室实习 JD 明确写了）。"
    "你能设计和理解高难数学数据，这是多数工程师做不到的。算力需求中等（7B/14B + LoRA，租卡可承受）。",
    size=11, first_indent_cm=0.74, space_after=10
)

# --- 备选 ---
add_heading_custom(doc, "备选：几何深度学习 / 科学机器学习", level=2)

add_styled_paragraph(
    doc,
    "流形上的扩散模型与 flow matching、最优传输（Monge-Ampère 方程就是几何分析）、"
    "神经 PDE（极小曲面、调和映射、Ricci 流）。和你专业最亲，但更吃算力、更拥挤，"
    "适合作为论文选题的理论侧而非主线。",
    size=11, first_indent_cm=0.74, space_after=10
)

# ═══════════════════════════════════════════
#  三、「没有资源」的具体解法
# ═══════════════════════════════════════════

add_heading_custom(doc, "三、「没有资源」的具体解法", level=1)

# 表格
table = doc.add_table(rows=5, cols=2)
table.alignment = WD_TABLE_ALIGNMENT.CENTER
table.style = 'Table Grid'

# 表头
headers = ["缺什么", "解法"]
for i, h in enumerate(headers):
    cell = table.rows[0].cells[i]
    cell.text = ""
    p = cell.paragraphs[0]
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(h)
    run.font.size = Pt(11)
    run.font.bold = True
    run.font.color.rgb = RGBColor(0xFF, 0xFF, 0xFF)
    run.font.name = '微软雅黑'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
    set_cell_shading(cell, '2E5C9E')

# 数据行
resources_data = [
    ("GPU",
     "AutoDL / 恒源云租 4090（约 2 元/时，一篇 7B 实验全程几百到两千元）；"
     "Kaggle 每周 30h 免费；Colab；OpenI 启智社区 / 智源免费额度；"
     "GitHub Student Pack 含云额度"),
    ("钱",
     "Agent / 形式化方向主要是 API 费，总预算 2000–5000 元能撑完一年"),
    ("导师 / 反馈",
     "① 工业界研究实习（终极答案：给算力、给 mentor、给论文署名）；"
     "② Lean 官方 Zulip 社区对新人极其友好；"
     "③ EleutherAI 等开源社区 Discord；"
     "④ 冷邮件本校计算数学/优化方向和隔壁 CS 做 ML 的老师；"
     "⑤ 联系在 AI 实验室的校友"),
    ("题源",
     "每天刷 arXiv（cs.AI / cs.CL / cs.LO）、跟 PutnamBench / miniF2F 榜、"
     "NeurIPS「AI for Math」workshop 的 open problems"),
]

for row_idx, (col1, col2) in enumerate(resources_data, start=1):
    row = table.rows[row_idx]
    for col_idx, text in enumerate([col1, col2]):
        cell = row.cells[col_idx]
        cell.text = ""
        p = cell.paragraphs[0]
        p.paragraph_format.space_before = Pt(2)
        p.paragraph_format.space_after  = Pt(2)
        p.paragraph_format.line_spacing = 1.3
        run = p.add_run(text)
        run.font.size = Pt(10)
        run.font.name = '微软雅黑'
        run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')
        if col_idx == 0:
            run.font.bold = True
            run.font.color.rgb = DARK_BLUE
            p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        if row_idx % 2 == 0:
            set_cell_shading(cell, 'E8EEF5')

# 设置列宽
for row in table.rows:
    row.cells[0].width = Cm(3.0)
    row.cells[1].width = Cm(13.5)

doc.add_paragraph()  # 空行

# ═══════════════════════════════════════════
#  四、12 个月路线图
# ═══════════════════════════════════════════

add_heading_custom(doc, "四、12 个月路线图（2026.09 → 2027.11）", level=1)

# Phase 0
add_heading_custom(doc, "Phase 0｜地基（9–10 月，每天 3–4 小时）", level=2)
add_bullet(doc, "Python 熟练化 → PyTorch → 跟着 Karpathy 的 Neural Networks: Zero to Hero 手写 micrograd 和 nanoGPT 并跑通。"
    "数学学生转行最大的死穴是眼高手低，代码量是硬指标。",
    bold_prefix="代码：")
add_bullet(doc, "《动手学深度学习》选读 + Transformer / RL 基础（PPO → GRPO 这条线）。",
    bold_prefix="理论：")
add_bullet(doc, "装 Lean 4 + VS Code，刷 Functional Programming in Lean、Natural Number Game、Mathematics in Lean。",
    bold_prefix="Lean：")
add_bullet(doc, "DeepSeek-Prover V1/V2、AlphaProof、LeanDojo、ReProver、DSP（Draft-Sketch-Prove）、"
    "PutnamBench、Kimina-Prover、BPT 等。每天 1 篇。",
    bold_prefix="论文清单 30 篇起步：")
add_bullet(doc, "建 GitHub，从第一天起打卡式提交。",
    bold_prefix="开源：")

# Phase 1
add_heading_custom(doc, "Phase 1｜复现 + 差异化作品（11–12 月）", level=2)
add_bullet(doc, "复现一个 API 驱动的 theorem-proving agent（LeanDojo / ensemble-prover 架构："
    "规划→检索→证明→Lean 验证→修复），全部代码开源。",
    bold_prefix="复现：")
add_bullet(doc, "把你领域内一批小结果（微分几何 / 几何分析入门定理）形式化成 Lean，"
    "或提 PR 给 Mathlib，或自建 repo。这是你的简历核爆点。",
    bold_prefix="独一无二的事：")
add_bullet(doc, "11 月起投寒假 / 日常实习：字节 Seed、阿里通义、腾讯 AI Lab、"
    "智谱、MiniMax、月之暗面、上海人工智能实验室等，日常实习滚动招聘。",
    bold_prefix="投实习：")

# Phase 2
add_heading_custom(doc, "Phase 2｜第一个研究产出（2027.1–4 月）", level=2)
add_styled_paragraph(doc, "现实选题举例：", size=11, bold=True, first_indent_cm=0.74, space_after=4)
add_bullet(doc, "几何分析定理的 autoformalization 数据集 + prover 评测（Mathlib 几何空白 = 直接的数据集贡献）；")
add_bullet(doc, "Proof agent 的子目标分解 / 树搜索策略改进（API 预算分配、多模型分工、失败修复）；")
add_bullet(doc, "定理证明 agent 的失败模式 benchmark / 过程奖励分析。")

add_styled_paragraph(doc, "出口按把握度排序：", size=11, bold=True, first_indent_cm=0.74, space_before=4, space_after=4)
p = doc.add_paragraph()
p.paragraph_format.left_indent = Cm(0.75)
p.paragraph_format.space_after = Pt(8)
p.paragraph_format.line_spacing = 1.4
run = p.add_run("arXiv 预印本 + 开源（保底）→ AITP 等专业会议 / NeurIPS、ICLR workshop → EMNLP / NAACL / COLING（CCF-B）→ CCF-A 主会（冲刺）")
run.font.size = Pt(10.5)
run.font.color.rgb = DARK_BLUE
run.font.name = '微软雅黑'
run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

# Phase 3
add_heading_custom(doc, "Phase 3｜研究实习（2027.3–7 月）", level=2)
add_styled_paragraph(
    doc,
    "带着 Phase 1/2 的作品面上实习，进去 3–6 个月：用实验室的算力和 mentor 冲 CCF-A"
    "（NeurIPS 2027 主会截稿约 5 月、ICLR 2028 约 9 月），同时拿 return offer——这是秋招最大的底牌。",
    size=11, first_indent_cm=0.74, space_after=8
)

# Phase 4
add_heading_custom(doc, "Phase 4｜秋招（2027.7–11 月）", level=2)
add_styled_paragraph(
    doc,
    "简历 = 985 数学 + 实习 return offer + 在投/发表论文 + 开源项目（prover agent + Lean 形式化 repo）。",
    size=11, first_indent_cm=0.74, space_after=4
)
add_styled_paragraph(
    doc,
    "备选赛道：量化私募（幻方——DeepSeek 的母体——、九坤、明汯等）对纯数学背景的对口度和薪资都高于互联网算法岗，建议同步关注；AI 应用开发岗作为兜底。",
    size=11, first_indent_cm=0.74, space_after=10
)

# ═══════════════════════════════════════════
#  五、本周就做的 7 件事
# ═══════════════════════════════════════════

add_heading_custom(doc, "五、本周就做的 7 件事", level=1)

actions = [
    "找教务/师兄师姐确认你是 27 届还是 28 届（27 届则秋招正在进行，立即边补边投，别等）。",
    "装好 Python + PyTorch 环境（本地或 AutoDL）。",
    "看完 Karpathy「Let's build GPT」并跑通 nanoGPT。",
    "装好 Lean 4，开始 Natural Number Game。",
    "注册 GitHub，建学习 repo，今天就第一次 commit。",
    "列好 30 篇论文清单，开始每天一篇。",
    "给本校做计算数学 / 优化 / ML 的老师发一封请教邮件（附带你的想法，不用等「准备好了」）。",
]
for i, action in enumerate(actions, 1):
    add_numbered(doc, action, i, size=10.5, space_after=5)

# ═══════════════════════════════════════════
#  六、三个必须提醒的风险
# ═══════════════════════════════════════════

add_heading_custom(doc, "六、三个必须提醒的风险", level=1)

risks = [
    ("别裸辞式转行：",
     "毕业论文还得是几何分析，和导师沟通好预期，建议固定每天 2–4 小时投入、保证毕业优先。"),
    ("别死磕单兵 CCF-A：",
     "论文是手段不是目标；实习同时解决算力、导师、论文、offer 四个问题，优先级最高。"),
    ("别去拼通用 Agent 工程岗：",
     "RAG / 工作流开发岗今年虽然在扩招，但你的差异化在「真数学 + 形式化 + 可验证 RL」这个交叉窄门里——"
     "费马大定理被形式化才过去五天，这个窗口对你是敞开的。"),
]
for prefix, text in risks:
    add_bullet(doc, text, bold_prefix=prefix, color=ACCENT_RED, size=10.5, space_after=5)

# ── 分隔线 ──
doc.add_paragraph()

# ── 参考信息 ──
add_heading_custom(doc, "参考信息来源", level=3)
refs = [
    "DeepSeek-Prover: Advancing Theorem Proving in LLMs through Large-Scale Synthetic Data. arXiv:2405.14333, 2024.",
    "DeepSeek-Prover-V2: Advancing Formal Mathematical Reasoning via RL for Subgoal Decomposition. arXiv:2504.21801, 2025.",
    "Ensemble Prover — 独立开发者项目，PutnamBench 榜 65 题. github.com/graviterra/ensemble-prover, 2026.",
    "Anthropic: Claude 形式化费马大定理. 中国科学报, 2026-09-05.",
    "秋季校招 AI 岗暴增近两倍，游戏行业「新门槛」正在形成. 游戏新知, 2026-09.",
    "智谱 27 届校招 JD (GLM-Code Agent / 大模型算法 Agent 方向). mokahr.com, 2026-08.",
    "上海人工智能实验室实习 JD (大模型算法 / Agentic RL). shlab.org.cn, 2026-08.",
    "OPPO 校招 JD (算法工程师 大模型&智能体方向). careers.oppo.com, 2025-07.",
]
for ref in refs:
    p = doc.add_paragraph()
    p.paragraph_format.space_before = Pt(0)
    p.paragraph_format.space_after  = Pt(3)
    p.paragraph_format.line_spacing = 1.3
    p.paragraph_format.left_indent  = Cm(0.75)
    p.paragraph_format.first_line_indent = Cm(-0.4)
    run = p.add_run(f"[{refs.index(ref)+1}] {ref}")
    run.font.size = Pt(9)
    run.font.color.rgb = GRAY
    run.font.name = '微软雅黑'
    run._element.rPr.rFonts.set(qn('w:eastAsia'), '微软雅黑')

# ── 保存 ──
output_path = r"c:\Users\32752\Desktop\转码参考\Transport_to_AI\几何分析转AI_Agent就业方案.docx"
doc.save(output_path)
print(f"文档已保存至: {output_path}")

# selfcheck.py：跨行进度自检表
# 问 5 个问题 → 统计得分 → 按分数分档给建议 → 列出未完成项。
# 这是本周最有价值的脚本：它同时是学习成果、自媒体素材、和你的进度仪表盘。
# 用到的知识全部来自前 4 天：input / in / if / 列表 append / join / f-string / datetime

# ===== 1. 准备工作 =====
from datetime import date          # 导入日期类，最后算剩余天数用

# YES 是一个元组（tuple，和 list 类似但用圆括号、不可修改）
# 存放所有可接受的"肯定回答"，后面用 in 判断，避免把 4 种写法各写一遍
YES = ("是", "是的", "y", "Y", "yes")

score = 0          # 计数器：答对一个 +1，初始为 0（int 型）
gaps = []          # 空列表：收集没完成的项目，最后统一打印

# ===== 2. 五个问题（每个问题结构相同：输入 → in 判断 → 计分或记录缺口）=====
ans1 = input("1. Python 环境跑通了吗？（是/否）").strip()
if ans1 in YES:                    # 输入在 YES 元组里 = 回答"是"
    score = score + 1              # 计数器加 1（也可写作 score += 1，是同一意思的简写）
else:
    gaps.append("① Python 环境")   # list 的 .append()：把一项追加到列表末尾

ans2 = input("2. Linux 命令行能用吗？（是/否）").strip()
if ans2 in YES:
    score = score + 1
else:
    gaps.append("② Linux 命令行")

ans3 = input("3. 能解释 10 个行业术语了吗？（是/否）").strip()
if ans3 in YES:
    score = score + 1
else:
    gaps.append("③ 行业术语表")

ans4 = input("4. 自媒体账号开了吗？（是/否）").strip()
if ans4 in YES:
    score = score + 1
else:
    gaps.append("④ 自媒体账号")

ans5 = input("5. 开始投递公司了吗？（是/否）").strip()
if ans5 in YES:
    score = score + 1
else:
    gaps.append("⑤ 投递简历")

# ===== 3. 输出得分 =====
print()
print(f"===== 自检结果 =====")
print(f"得分：{score}/5")

# ===== 4. 分档建议（if / elif / else，从高到低判断）=====
# 顺序很重要：必须先判 >=4，再判 >=2；反过来写 5 分也会命中 ">=2"
if score >= 4:
    print("进展正常，把重心转到技术深度。")
elif score >= 2:
    print("半只脚进门，本月内必须开始投递。")
else:
    print("还在门外，先解决下面列出的缺口。")

# ===== 5. 列出未完成项 =====
# len(gaps) 是列表长度；> 0 说明至少有一项没完成
if len(gaps) > 0:
    print("未完成项：")
    # "\n".join(gaps)：用换行符把列表里的每一项拼成多行文本（Day 3 的 join 方法）
    # "\n" 是换行符的写法，两个字符 \ 和 n 合起来表示"换一行"
    print("\n".join(gaps))

# ===== 6. 倒计时（Day 2 的 datetime 知识复用）=====
days = (date(2027, 1, 31) - date.today()).days   # 距硬指标的天数，每天自动更新
print()
print(f"距 2027-01-31 还有 {days} 天，按每周 20 小时算约 {round(days / 7 * 20)} 小时。")

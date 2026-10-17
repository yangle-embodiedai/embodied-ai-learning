# guess_number.py：猜数字游戏
# 程序随机出题（1-100），你反复猜，程序提示"大了/小了"，猜中显示次数。
# 这是 Day 5 的综合练习：random + while + if/elif + 计数器 + input + 类型转换，全部前 5 天的知识。

# ===== 1. 导入随机数工具 =====
# random 是标准库模块（和 datetime 一样自带），randint 是其中的函数
# random.randint(a, b)：返回一个 a 到 b 之间的随机整数，**含 a 也含 b**（注意：range 不含止，randint 含止，两者规则不同！）
import random

answer = random.randint(1, 100)     # 出题：程序心里想一个 1-100 的整数，存进 answer
print(f"[调试] 答案是{answer}")
# 想调试时看答案，可以临时加一行：print(f"[调试] 答案是 {answer}")

# ===== 2. 初始化状态 =====
count = 0                           # 计数器：猜了几次（Day 4 selfcheck.py 用过同款）

# ===== 3. 主循环：反复猜，直到猜中 =====
while True:                         # 死循环：猜中靠 break 退出（calculator.py 的结构）
    guess_raw = input("猜一个 1-100 的整数：").strip()   # 每轮读一次输入

    # 输入校验：非数字（abc、8.5、空回车）不算猜错，也不计入次数，直接重来
    if not guess_raw.isdigit():
        print("请输入整数")
        continue                    # 跳过本轮剩余，回到 while 开头重新出提示

    guess = int(guess_raw)          # 转成 int 才能比大小
    count = count + 1               # 走到这里说明输入合法且算一次猜测

    # 三分支比较（Day 4 的 if/elif/else）
    if guess > answer:
        print("大了")
    elif guess < answer:
        print("小了")
    else:
        # 猜中：显示结果后 break 结束整个循环
        print(f"猜对了！答案就是 {answer}，你共猜了 {count} 次")
        break

# ===== 4. 按次数评语 =====
# 必须顶格（不缩进）：放在主循环外面，游戏结束时只执行一次
# 用 if/elif/else 分档（Day 4 语法），不用 while——while 是"重复"用的，这里只说一次
# 你原版的两个错：① 放在主循环内 → 每猜一次都触发 ② 内层 while True 无更新无出口 → 死循环刷屏
# 另：原文件第 44 行末尾多了一个 2，那是 SyntaxError，整个文件都跑不起来
if count <= 2:
    print(f"你是一个欧皇！只用了 {count} 次")
elif count <= 5:
    print(f"中规中矩，再接再厉！用了 {count} 次")
else:
    print(f"太非了！要不要再试一次？用了 {count} 次")
# ===== 4. 循环结束后 =====
# 程序到这里就结束了。以后可以加：按次数评语（<=7 次很棒）、是否再来一局
# 顺带一提：二分策略（每次猜区间中点）最多 7 次必中，因为 2 的 7 次方 = 128 > 100
# 猜完可以试试验证这一点

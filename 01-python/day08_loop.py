# day08_loop.py —— 10.30 学习材料：for 循环实战 + while 循环
# 配套小测：quiz_2026-10-30.py（错开一日，考 10.28 的条件嵌套 + for 嵌套 + 字符串方法）
#
# 【术语先定义】
# - range()：生成一串整数序列的函数，三种写法：
#     range(5)        → 0,1,2,3,4        （只给终点，起点默认 0，终点不含）
#     range(1, 6)     → 1,2,3,4,5        （给起点和终点，起点含、终点不含）
#     range(0, 10, 2) → 0,2,4,6,8        （第三个参数是"步长"，每次跨几步）
# - 累加器（accumulator）：一个变量，在循环里不断把新值加上去，最后得到总和。
# - enumerate()：遍历时同时拿到"下标"和"值"，写法 for i, v in enumerate(列表)
# - while：条件为 True 就一直循环，条件变 False 才停。必须自己让条件变化，否则死循环。
# - break：立刻跳出"当前这层"整个循环。continue：跳过本轮剩下的代码，直接进入下一轮。

# ===================== 第一部分：for 循环实战 =====================
# 示例 1：range 只给终点（起点默认 0，终点不含）
for i in range(5):          # i 依次取 0,1,2,3,4（取不到 5）
    print(i)                # 每行打印一个 i
# 输出：0 / 1 / 2 / 3 / 4（共 5 行，每行一个数字）

# 示例 2：range 给起点和终点（起点含、终点不含）
for i in range(1, 6):       # i 依次取 1,2,3,4,5（取不到 6）
    print(i)
# 输出：1 / 2 / 3 / 4 / 5（共 5 行）
# 踩坑点：range(1,6) 是 5 个数不是 6 个；想取到 6 得写 range(1, 7)

# 示例 3：range 给步长（第三个参数，每次跨几步）
for i in range(0, 10, 2):   # i 依次取 0,2,4,6,8（从 0 开始，每次 +2，不到 10）
    print(i, end=" ")       # end=" " 表示打印完接一个空格，不换行
print()                     # 上面都没换行，这里手动换一行
# 输出：0 2 4 6 8（一行）

# 示例 4：for 遍历字符串（逐个字符）
word = "深圳机器人"
for ch in word:             # ch 依次取 深、圳、机、器、人（每次一个字符）
    print(ch)
# 输出：深 / 圳 / 机 / 器 / 人（5 行）

# 示例 5：for 遍历列表 + 累加器求和
scores = [88, 92, 76]
total = 0                   # 累加器：先设为 0
for s in scores:            # s 依次取 88、92、76
    total = total + s       # 每轮把 s 加到 total 上（0+88=88，88+92=180，180+76=256）
print(total)                # 输出：256
average = total / len(scores)   # len() 拿列表长度 = 3；总和除以数量 = 平均分
print(average)              # 输出：85.33333333333333

# 示例 6：enumerate 同时拿下标和值
cities = ["深圳", "杭州", "苏州"]
for index, city in enumerate(cities):   # index 是下标（0,1,2），city 是值
    print(index, city)
# 输出：
#   0 深圳
#   1 杭州
#   2 苏州

# 示例 7：for 遍历字典（.items() 同时拿键和值）
company = {"name": "帕西尼", "city": "深圳", "layer": "零部件"}
for key, value in company.items():      # key 是键名，value 是键值
    print(key, "=", value)
# 输出：
#   name = 帕西尼
#   city = 深圳
#   layer = 零部件
# 注意：直接 for k in company 只能拿到"键"，拿不到值

# ===================== 第二部分：while 循环 =====================
# 示例 8：while 基本形式（计数器，必须有让条件变化的那一行）
count = 1                   # 起始值
while count <= 3:           # 条件：count <= 3 成立就继续循环
    print("第", count, "次")  # 每一轮打印当前次数
    count = count + 1       # 关键：每轮 +1，让条件最终变 False（不加就是死循环）
print("循环结束，count =", count)   # 循环跑完 count 变成 4
# 输出：第 1 次 / 第 2 次 / 第 3 次 / 循环结束，count = 4
# 踩坑点：忘写 count = count + 1 → count 永远是 1 → 条件永远 True → 死循环卡住

# 示例 9：while 累加（把 1 到 100 加起来）
n = 1                       # 从 1 开始
total2 = 0                  # 累加器
while n <= 100:             # 只要 n 不超过 100 就继续
    total2 = total2 + n     # 把当前的 n 加到总和上
    n = n + 1               # n 自增，往 101 走
print(total2)               # 输出：5050（1+2+...+100）

# 示例 10：break 立刻跳出，continue 跳过本轮
for i in range(1, 6):       # i 取 1,2,3,4,5
    if i == 3:
        break               # i 到 3 时立刻跳出整个循环，后面的 4、5 都不跑了
    print(i, end=" ")
print()
# 输出：1 2（3 就被 break 掉了，4、5 根本没轮到）

for i in range(1, 6):       # i 取 1,2,3,4,5
    if i == 3:
        continue            # i 到 3 时跳过本轮剩下的代码，直接进下一轮（i=4）
    print(i, end=" ")
print()
# 输出：1 2 4 5（只有 3 被跳过，其他都打印）

# ===================== 自写练习（你来补 2 段）=====================
# 练习 1：用 for + range 算 1 到 10 的平方和（1²+2²+...+10² = 385）
# 要求：用累加器 total_square，循环里把 i*i 加上去，最后 print
total_square = 0
# 在这里写你的 for 循环（提示：for i in range(1, 11)）
# 你的代码：

# 练习 2：用 while 循环，从 10 倒数到 1，每行打印一个数，最后打印"发射！"
# 要求：countdown = 10 起步，条件是 countdown >= 1，每轮 -1
countdown = 10
# 在这里写你的 while 循环
# 你的代码：

# ===================== self-test =====================
# 补完 2 个练习后跑 python day08_loop.py，检查下面期望输出
# 练习 1 期望：385
# 练习 2 期望：10 / 9 / 8 / 7 / 6 / 5 / 4 / 3 / 2 / 1 / 发射！

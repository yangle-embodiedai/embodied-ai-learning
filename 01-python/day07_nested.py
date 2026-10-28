# day07_nested.py —— 10.28 学习材料：条件嵌套 + for 循环嵌套 + 字符串方法
# 配套小测：quiz_2026-10-28.py（错开一日，考 10.27 的作用域+默认参数）
#
# 【术语先定义】
# - 条件嵌套（if inside if）：if 的函数体里再写 if，一层套一层。
#   规则：只有外层条件为 True，才会进外层 if 体；进了外层后，还要看内层条件。
# - 循环嵌套（for inside for）：for 的函数体里再写 for，外层跑 1 次，内层跑完一整轮。
#   总执行次数 = 外层次数 × 内层次数。
# - 字符串方法（str methods）：字符串自带的"功能"，用 .方法名(参数) 调用。
#   本期学 4 个：.strip() / .split() / .replace() / .upper()
#   注意：str 方法都是"不改变原串"，要么返回新串要么返回列表。
#
# ===================== 第一部分：条件嵌套 =====================
# 示例 1：if 套 if（逐层判断）
score = 85
if score >= 60:
    print("及格")          # 外层：score>=60 真 → 执行
    if score >= 90:
        print("优秀")       # 内层：score>=90 假 → 不执行
# 输出：及格（只打印及格，不打印优秀）
# 踩坑点：外层 False 时，内层整块跳过，连"判断"都不发生。

# 示例 2：if-elif-else（互斥，从上往下命中一个就停）
temp = 30
if temp > 35:
    print("热")
elif temp > 25:
    print("舒适")          # 命中这行
else:
    print("冷")
# 输出：舒适
# 关键：elif/else 和 if 同级缩进；命中 elif 后 else 不再判断。

# 示例 3：if 里再套 if-else（最常见）
age = 20
has_license = True
if age >= 18:
    if has_license:
        print("可以开车")
    else:
        print("成年了但没驾照")
else:
    print("未成年")
# 输出：可以开车

# ===================== 第二部分：for 循环嵌套 =====================
# 示例 4：两层 for（外层×内层）
for i in range(3):        # 外层 3 次：i = 0, 1, 2
    for j in range(2):    # 内层 2 次：j = 0, 1
        print(i, j)
# 输出顺序（外层跑 1 次，内层跑完 2 轮）：
#   0 0
#   0 1
#   1 0
#   1 1
#   2 0
#   2 1
# 总执行 = 3 × 2 = 6 次

# 示例 5：嵌套 for + 条件（提前 break）
for i in range(5):
    for j in range(5):
        if i == 2:
            break          # 外层 i=2 时，内层只跑 1 次就停
        print(i, j)
# 输出：
#   0 0 / 0 1 / 0 2 / 0 3 / 0 4
#   1 0 / 1 1 / 1 2 / 1 3 / 1 4
#   （i=2 时内层 break，不打印）
# 踩坑点：break 只跳出"当前这层"循环，外层继续。

# ===================== 第三部分：字符串方法（4 个）=====================
# 示例 6：.strip() 去首尾空白（不影响中间空格）
s = "  深圳  机器人  "
print(s.strip())          # 输出：深圳  机器人（首尾空格没了，中间保留）

# 示例 7：.split() 按空格拆成列表
text = "深圳 机器人 谷"
words = text.split(" ")   # 按空格拆
print(words)              # 输出：['深圳', '机器人', '谷']
print(words[0])           # 输出：深圳（列表第一个）
# 注意：split 不传参默认按"任意连续空白"拆（空格/制表符/换行都算）

# 示例 8：.replace() 替换（不改变原串，返回新串）
city = "深圳"
new = city.replace("圳", "河")
print(city, new)          # 输出：深圳 深圳→替换后是"深河"
# 关键：city 本身没变，new 是替换后的新串

# 示例 9：.upper() 转大写（英文）
word = "hello"
print(word.upper())       # 输出：HELLO
# 中文没有大小写，.upper() 对中文串无效（原样返回）

# ===================== 自写练习（你来补 2 段）=====================
# 练习 1：写嵌套 if，根据 price 输出：
#   price > 100 → "贵"
#   price > 50 且 <=100 → "中等"
#   price <= 50 → "便宜"
# 提示：用 if / elif / else
price = 60
if price > 100:
    print("贵")
elif 50 < price <= 100:
    print("中等")
else: 
    print("便宜")

# 练习 2：两层 for，打印乘法口诀表（1-3），外层 i=1..3，内层 j=1..3
# 只打印 j <= i 的部分（即 1×1 / 1×2 2×2 / 1×3 2×3 3×3）
# 输出格式：i*j=i*j 结果（如 2*3=6）
for i in range(1,4):
    for j in range(1,4):
        if j <= i:
            print(f"{i}*{j}={i*j}")
# ===================== self-test =====================
# 跑完 2 个练习后，下面 3 行直接执行
price = 60
if price > 100:
    print("贵")
elif price > 50:
    print("中等")
else:
    print("便宜")
# 期望：中等

for i in range(1, 4):
    for j in range(1, 4):
        if j <= i:
            print(f"{i}*{j}={i*j}")
# 期望：
# 1*1=1
# 2*1=2
# 2*2=4
# 3*1=3
# 3*2=6
# 3*3=9

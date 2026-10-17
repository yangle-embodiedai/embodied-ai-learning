# calculator.py：带菜单循环的计算器
# 菜单：1 加法 2 减法 3 乘法 4 除法 5 退出。选 5 才停，其他选完继续。
# 这是本周交付物"4 个脚本"的最后一个：循环 + 条件 + 输入的综合。
# 两个新概念：while 循环、break/continue。逐行注释见下。

# ===== 1. 新概念：while 循环 =====
# 定义：while 条件: 会反复执行缩进块，直到条件变为 False。
# while True: 条件永远成立 → 死循环，必须靠 break（跳出）才能退出。
# 菜单类程序的标准写法就是 while True + break。

while True:                                    # 循环开始：每轮 = 显示菜单 → 读选项 → 执行 → 回到开头
    print()
    print("====== 计算器 ======")
    print("1. 加法  2. 减法  3. 乘法  4. 除法  5. 退出")

    choice = input("请选择：").strip()          # 读用户选项，str 型（"1"-"5"）
    
    # ---- 选项合法性判断 ----
    if choice not in ("1", "2", "3", "4", "5"):     # not in：不在元组里 = 选项无效
        print("无效选项，请输入 1-5")            # 提示后不做任何计算
        continue                               # continue：跳过本轮剩余代码，直接回到 while 开头重新显示菜单
    
    # ---- 退出分支 ----
    if choice == "5":                          # 注意：比较的是字符串 "5"，不是数字 5
        print("再见。")                         # break：立刻跳出整个 while 循环，执行循环后面的代码
        break
    
    # ---- 读操作数（走到这里说明 choice 是 1-4，需要两个数字）----
    a_raw = input("第一个数：").strip()          # 原始输入，str
    b_raw = input("第二个数：").strip()          # 同上

    # ---- 输入合法性：两个都必须是纯数字 ----
    # a_raw.isdigit() and b_raw.isdigit()：任一个不是数字（如 abc、8.5、负号）就提示并重来
    if not (a_raw.isdigit() and b_raw.isdigit()):
        print("两个操作数都必须是 0 或正整数，请重新选择")
        continue                               # 回到菜单，不算了

    a = int(a_raw)                             # 转成 int 才能做算术
    b = int(b_raw)

    # ---- 按选项计算（if/elif 分发，Day 4 的知识）----
    if choice == "1":
        print(f"{a} + {b} = {a + b}")          # f-string 里直接写运算
    elif choice == "2":
        print(f"{a} - {b} = {a - b}")
    elif choice == "3":
        print(f"{a} * {b} = {a * b}")
    else:                                      # 剩下唯一可能：choice == "4"（除法）
        if b == 0:
            # 除零防护：任何数除以 0 在数学上无定义，Python 会直接崩
            # 不判断的话报 ZeroDivisionError: division by zero
            print("除数不能为 0")
        else:
            # / 的结果永远是 float（小数），10 / 4 = 2.5，10 / 2 = 5.0
            # round(x, 2) 保留 2 位小数，输出更整洁；round 是内置函数
            print(f"{a} ÷ {b} = {round(a / b, 2)}")

    # 代码走到这里 = 本轮结束，自动回到 while 开头，重新显示菜单

# ===== 2. 测试清单（跑起来后逐个验证）=====
# 85 + 15 = 100；20 - 32 = -12（结果可为负）；20 * 52 = 1040
# 10 ÷ 4 = 2.5（float）；10 ÷ 0 → 除数不能为 0
# 选 9 → 无效选项；输入 abc 当操作数 → 提示重来；选 5 → 再见，程序结束

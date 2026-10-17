# day04_drill.py：条件判断练习
# 内容：if/elif/else 语法、比较运算符、逻辑运算符、嵌套判断
# 跑法：VS Code 打开本文件 → Ctrl+S → Ctrl+F5
# 注意：本文件末尾有 input()，运行后终端会等你打字，逐个回答即可

# ===== 1. if / elif / else 基本语法 =====
# 语法三要素：
#   ① if 条件:        ← 条件后面必须有英文冒号
#   ② 缩进 4 个空格    ← 缩进内的代码属于这个 if（Python 靠缩进划分代码块，不是大括号）
#   ③ elif = else if（否则如果），else = 以上都不满足
# 执行顺序：从上往下逐个检查条件，命中一个就执行它并跳过其余分支

score = 85
if score >= 90:            # 85 >= 90 是 False，跳过
    print("等级 A")
elif score >= 80:          # 85 >= 80 是 True，命中这里
    print("等级 B")        # ← 会打印这行，然后整个 if 块结束
elif score >= 60:
    print("等级 C")        # 即使 85 也 >= 60，也不会执行（前面已命中）
else:
    print("等级 D")

# 常见错误示范（不要学）——两种独立错误，报错信息不同：
# 错误① if 行末少了冒号（哪怕缩进了也报错）：
#   if score >= 90
#       print("A")
#   → SyntaxError: expected ':'      （冒号是"开启代码块"的标志，没有它，缩进无意义）
# 错误② 有冒号但下一行没缩进：
#   if score >= 90:
#   print("A")
#   → IndentationError: expected an indented block after 'if' statement
# 记法：冒号开启代码块，缩进划清代码块归属，两者缺一不可，报错信息也不同。

# ===== 2. 比较运算符（结果永远是 bool：True / False）=====
print(85 >= 80)    # True
print(85 == 80)    # False。注意：== 是"比较"，= 是"赋值"，两者完全不同
print(85 != 80)    # True。!= 读作"不等于"
print(85 < 80)     # False

# == 和 = 的区别（新手第一大坑）：
# =   赋值：把右边的值存进左边的变量   score = 85
# ==  比较：判断两边是否相等，返回 True/False   score == 85
# 写错的现象：if score = 85:  →  SyntaxError（Python 禁止在条件里赋值，会直接报错拦住你）

# ===== 3. 逻辑运算符：and / or / not =====
# and：两边都 True 才 True
# or ：任意一边 True 就 True
# not：取反
hours = 20
deadline_days = 106

print(hours >= 15 and deadline_days < 120)   # True and True → True（时间和进度都达标）
print(hours >= 25 or deadline_days < 120)    # False and True → False？不对——
# 上面这行实测是 True：or 只要一边 True 就 True（deadline_days < 120 是 True）
print(not (hours >= 25))                     # not False → True

# 组合实例：判断"是否该进入投递阶段"
# 条件：每周投入 >= 15 小时，且环境已跑通
env_ready = True
if hours >= 15 and env_ready:
    print("可以启动投递：时间和环境都具备")
else:
    print("先补时间和环境，再谈投递")

# ===== 4. 嵌套判断（if 里面再套 if）=====
# 场景：先判断输入是否合法，合法才进一步分级
score2 = 105
if 0 <= score2 <= 100:          # Python 支持连续比较：0 <= 105 <= 100 → False
    if score2 >= 90:
        print("合法分数，等级 A")
    else:
        print("合法分数，其他等级")
else:
    print("分数超出 0-100,输入不合法")   # ← 会打印这行

# ===== 5. input + 条件判断（qa.py 里已用过一次）=====
# input() 返回 str，比较数字前必须 int()；比较文字（"是"/"否"）则直接用 ==
answer = input("你已经注册 GitHub 了吗？（是/否）").strip()   # .strip() 去掉两端空格
if answer == "是":
    print("好，下一步是保证每天一次提交")
else:
    print("今天就把 GitHub 注册了,10 分钟的事")

# 防御性写法：用户可能敲 "Y" "y" "yes" "是的"
# 统一用 in 判断多个可接受值，比写 4 个 or 更简洁
if answer in ("是", "是的", "y", "Y", "yes"):
    print("（宽松匹配）已注册")
else:
    print("（宽松匹配）未注册")

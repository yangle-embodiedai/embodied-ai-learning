# day06_scope.py —— 10.27 学习材料：函数作用域（局部/全局）+ 默认参数
# 配套小测：quiz_2026-10-27.py
#
# 【术语先定义】
# - 全局变量（global variable）：定义在函数体外面（模块顶层）的变量，整个文件任何地方都能读。
# - 局部变量（local variable）：定义在函数体里面的变量，只有这个函数内部能看见；
#   函数跑完，局部变量就销毁（下次再调用函数，会重新创建）。
# - 作用域（scope）：一个变量"能被发现"的范围。Python 规则：
#   先在本函数内找（局部），找不到再往外一层找（全局），再找不到就 NameError。
# - 默认参数（default argument）：def 时给参数写一个默认值，调用时不传就用默认值。
#
# ===================== 第一部分：作用域 =====================
# 示例 1：全局变量被函数读（合法）
score = 100          # 全局变量
def show_score():
    print(score)     # 读全局变量，不会报错，输出 100
show_score()         # 输出 100

# 示例 2：函数内"写"同名变量 → 是新的局部变量，全局那个没变
score = 100          # 全局变量
def reset_score():
    score = 0        # 这里创建的是局部变量 score，和全局的无关
    print(score)     # 输出 0（局部）
reset_score()
print(score)         # 输出 100（全局没被改）
# 踩坑点：函数内直接给"同名变量"赋值，Python 会把它当局部变量，
# 不是"修改全局"。想真的改全局，要在函数内写 global score 声明。

# 示例 3：用 global 声明后，函数内改的就是全局
total = 0
def add_one():
    global total     # 声明：total 用全局的那个
    total = total + 1
add_one()
add_one()
add_one()
print(total)         # 输出 3（全局被改了 3 次）

# 示例 4：函数跑完，局部变量就没了
def make_name():
    nickname = "老杨"   # 局部变量
    print(nickname)     # 函数内能看见
make_name()
#print(nickname)      # 放开这行会 NameError：nickname 是局部变量，函数外看不见

# ===================== 第二部分：默认参数 =====================
# 示例 5：默认参数的基本用法
def greet(name, greeting="你好"):
    print(greeting + "," + name)
greet("白杨")                # 没传 greeting → 用默认值，输出 你好,白杨
greet("老杨","早上好")        # 传了 → 输出 早上好,老杨

# 示例 6：默认参数常用场景 = 可选配置
def add(a, b=0):
    return a + b
add(5)               # 输出 5（b 用默认 0）
add(5, 3)            # 输出 8（b 传 3）

# 示例 7：默认参数在 def 时求值，不是调用时（进阶坑）
# 记住这条就够：默认参数里的"值"在写 def 那行时就算好存下来，
# 后面再调用不会重新算。对 int/str 这种不可变类型看不出差别；
# 如果默认参数是 list/dict（可变对象），反复调用会互相污染（本期不深究，知道现象即可）。

# ===================== 自写练习（你来补 2 个函数）=====================
# 练习 1：写函数 set_default(x, base=10)，输出 x + base。
#         调用：set_default(5) → 15；set_default(5, 2) → 7
def set_default(x, base=10):
    return x + base
set_default(5)
set_default(5,2)

# 练习 2：写函数 counter()，用 global 把模块顶层的 call_count 每次 +1，
#         并打印 call_count。调用 3 次后应输出 1 / 2 / 3。
call_count = 0
def counter():
    global call_count
    call_count = call_count + 1
counter()
counter()
counter()
print(call_count)


# ===================== self-test（跑完 2 个练习后，放开下面 3 行）=====================
set_default(5)          # 期望 15
set_default(5, 2)       # 期望 7
counter()               # 期望 1
counter()               # 期望 2
counter()               # 期望 3
print(call_count)       # 期望 3

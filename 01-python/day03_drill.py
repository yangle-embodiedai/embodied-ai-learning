# day03_drill.py：字符串专题练习
# 内容：索引 / 切片 / 常用方法 / f-string / input()
# 跑法：VS Code 打开本文件 → Ctrl+S → Ctrl+F5
# 注意：本文件用到 input()，所以要用"运行"而不是"调试"，
#       否则终端会等你手动输入。Ctrl+F5 会直接在终端跑并等待输入。

# ===== 1. 字符串索引与切片 =====
s = "具身智能"
# 索引：字符串里每个字符有位置编号，从 0 开始（不是从 1！）
# s[0] 是第 1 个字"具"，s[1] 是第 2 个字"身"
# s[-1] 是最后一个字"能"（负数从末尾往前数）
print(s[0])     # 具
print(s[-1])    # 能

# 切片 s[起:止:步]：取第 起 到 止-1 的位置（**包含起、不包含止**）
# 这是新手最容易错的地方：s[0:4] 取 4 个字符，不是到第 4 个
word = "embodied"
print(word[0:4])    # embo（取第0,1,2,3位，即前4个）
print(word[0:4:2])  # eo （从0开始，每次跳2步：第0、2位）
print(word[::2])    # eoi  （从开头到结尾，每2个取1个）
print(word[::-1])   # deidobme（步长-1，倒序；e m b o d i e d 反过来）

# ===== 2. 字符串常用方法 =====
# 方法 = 字符串自带的"动作"，用 .方法名() 调用，不改变原字符串，返回新字符串
raw = "  优必选：深圳  "
print(raw.strip())            # 去掉两端空格 → "优必选：深圳"
print(raw.lower())           # 全转小写（中文不变，英文 A→a）
print(raw.upper())           # 全转大写
print(raw.replace("深圳", "杭州"))   # 把"深圳"换成"杭州"

# split()：按分隔符把字符串拆成 list
line = "执行器,丝杠,减速器,电机"
parts = line.split(",")      # 按逗号拆开，得到 list：["执行器","丝杠","减速器","电机"]
print(parts)                 # 整个 list
print(parts[0])             # 第1个："执行器"
print(len(parts))          # 元素个数：4

# in：判断某段文字是否包含在字符串里，返回 True / False
print("深圳" in raw)        # True（raw 里有"深圳"）
print("上海" in raw)        # False

# join()：和 split 相反，把 list 用某字符重新拼成字符串
cities = ["深圳", "杭州"]
print("-".join(cities))     # "深圳-杭州"（用-连接）

# ===== 3. f-string（f 前缀的格式化字符串，Python 3.6+）=====
# 在字符串前加字母 f，就能用 {变量名} 直接把变量值填进字符串
# 对比昨天 profile.py 的写法：
#   旧：print("按每周 " + str(hours_per_week) + " 小时算")   ← 要反复 str() 转换
#   新：f"按每周 {hours_per_week} 小时算"                  ← {} 里直接写变量，自动转
hours = 20
print(f"按每周 {hours} 小时算，一年约 {hours * 52} 小时")
# {} 里可以放任意表达式，包括运算：{hours * 52} 直接算出 1040
# 这是最省事的输出方式，以后默认都用它

# ===== 4. input()：读取用户输入 =====
# input("提示语") 会在终端显示提示语，然后停下等你打字，回车后把**你输入的字符串**返回
# 关键坑：input() 返回值永远是 str，要参与算术必须先 int() 转换
# 下面这段会真的等你输入，所以单独放在文件末尾。
# 想跳过直接看，可以先把下面 3 行注释掉（行首加 #）再运行。

name_in = input("你叫什么？")        # 终端显示"你叫什么？"，等输入，回车后存进 name_in
hours_in = input("每周投入几小时？")  # 同样等你输入，返回的是字符串
hours_num = int(hours_in)           # 把字符串 "20" 转成整数 20，才能做算术
# print(f"你好 {name_in}，按每周 {hours_num} 小时，一年约 {hours_num * 52} 小时")

print("=== 练习部分结束 ===")
print("要试 input()：把上面 4 行 input 的 # 注释去掉，再 Ctrl+F5 运行，终端会等你打字")
print(f"你好{name_in},按每周{hours_num}小时,一年约{hours_num*52}小时")
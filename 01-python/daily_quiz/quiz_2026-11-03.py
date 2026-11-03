# 11.03 第 10 期每日小测
# 规则：小测考昨天的、学习材料学今天的（错开一日）
# 昨日（11.02）实际动手的：week5_tool.py 补全 —— dict 统计累加 + .items() 遍历 + 函数返回值链路
#                          （另含第9期修正区的 type() 输出格式）
# 今日学习材料（02-sql/ 下的 sql_01_select.sql + sql_02_where.sql）：SQL 建表/SELECT/WHERE —— 不考，明天 11.04 第 11 期才考
# 配套复习：week5_tool.py 第 17-43 行（先读复习区再作答）

# ============ 今日知识点复习（先读这 5 张速记卡，再做题）============
# - 速记卡 1：字典统计累加的标准写法 —— counts[s] = counts.get(s, 0) + 1
#              .get(s, 0) 的意思是"查 s 的次数，查不到就当 0"，所以第一次遇到记 0+1=1
# - 速记卡 2：遍历字典要拿"键+值" → for key, value in 字典.items()
#              直接 for k in 字典 只能拿到键，拿不到值
# - 速记卡 3：return 把结果交出去，函数外面必须用变量接住（如 result = count_status(...)）；
#              print 只是显示在屏幕上，交不出去
# - 速记卡 4：函数返回值可以直接当另一个函数的参数传入（show_report(result) 就是接住再传）
# - 速记卡 5：type() 输出格式固定为 <class '类型名'>，类型名两边必须带单引号

# ============ 题目 1：字典统计累加（考 11.02 的 count_status 写法）============
# 读代码，把输出写出来，再回答问 2。
words = ["OK", "ERR", "OK", "WARN", "OK"]
counts = {}
for w in words:
    counts[w] = counts.get(w, 0) + 1
print(counts)
# 问 1：print(counts) 输出什么？（写出完整字典）
# 问 2：如果循环里写成 counts[w] = counts[w] + 1（去掉 .get），第一次遇到 "OK" 时会发生什么？
# 【我的作答区】
# 问 1：["OK","ERR","WARN"]
# 问 2：会输出空字典{}

# ============ 题目 2：.items() 遍历 + 函数返回值（考 11.02 的 show_report）============
# 读代码，把输出按行写出来，再回答问 2。
def show_report(counts):
    for key, value in counts.items():
        print(key, ":", value)

def make_count():
    return {"OK": 3, "ERR": 1}

result = make_count()
show_report(result)
# 问 1：上面这段输出几行？每行写清楚。
# 问 2：如果把最后两行改成 show_report(make_count())，输出会变吗？为什么？
# 【我的作答区】
# 问 1：输出两行行 "OK": 3/"ERR": 1
# 问 2：这个不清楚

# ============ 错题回收（每周一规则，本期抽 2 条）============
# 规则：抽错题库里"挂期最早 + 还没连对 2 次"的 2 条，换数字重测。
# 当前挂期：⑬（11-06 到期）、⑱（11-06 到期）、⑰（11-09 到期）
# 本期抽：⑬ + ⑱（11-06 到期，挂期最早）

# 【错题回收 1 · 抽 ⑬】换数字重测"str 值参与数字运算前要 int() 转换"
product = {"name": "灵巧手", "price": "899"}
print(product["price"] + 1)
# 问 1：这行会报什么错？为什么？
# 问 2：修正成一行正确代码怎么写？修正后输出多少？
# 回收答 1：会报错，要参与数字运算首先要转int
# 回收答 2：print(int(product["price"]) + 1) , 900

# 【错题回收 2 · 抽 ⑱】换数字重测".get() 默认值≠恒定输出"
def get_city(company):
    return company.get("city", "未知")
print(get_city({"name": "越疆", "city": "深圳"}))
print(get_city({"name": "乐聚"}))
# 问 1：第一行 print 输出什么？
# 问 2：第二行 print 输出什么？为什么没崩？
# 回收答 1：深圳
# 回收答 2：未知，因为有.get()

# ============ 答案与点评（AI 回填区，用户作答后由 AI 填写）============

# ---------- 题 1 批（字典统计累加）----------
# 问 1：words = ["OK","ERR","OK","WARN","OK"]，数每个状态出现几次。
#   counts.get(w, 0)+1 累加后，counts = {'OK': 3, 'ERR': 1, 'WARN': 1}  ✅ 标准答案
#   你答 ["OK","ERR","WARN"] ❌ —— 两个错：①这是列表不是字典，统计结果必须用 {} 存"状态→次数"；
#   ②你丢了次数！统计字典要带数字（OK 3 次、ERR 1 次、WARN 1 次），你只列了键名。
#   关键：统计字典格式是 {'键': 次数, '键': 次数}，不是 ['键','键']。
# 问 2：counts[w] = counts[w] + 1 去掉 .get，第一次遇到 "OK" 时 counts 还是 {}，
#   里面没有 "OK" 这个键，counts["OK"] 读不存在的键 → 报 KeyError（不是输出空字典）。
#   你答"会输出空字典{}" ❌ —— 空字典是初始值，但代码会崩，根本走不到 print。
#   为什么 .get 不会崩：.get(w, 0) 查不到键时按 0 算，不会报错；直接 counts[w] 查不到就 KeyError。

# ---------- 题 2 批（.items() + 函数返回值）----------
# 问 1：make_count() 返回 {"OK":3,"ERR":1}，show_report 里 for key,value in counts.items()
#   遍历，print(key, ":", value) 用逗号分隔 → 输出 2 行：
#     OK : 3      （key="OK", value=3，print 逗号自动加空格）
#     ERR : 1
#   你答 "OK": 3 / "ERR": 1 🔶 半对 —— 内容和行数对了，但格式错：
#   ①你写了字典字面量格式带引号，实际 print 输出的是 OK : 3（不带引号）
#   ②print 逗号分隔输出，冒号两边有空格。
# 问 2：show_report(make_count()) 输出不会变。make_count() 返回 {"OK":3,"ERR":1}，
#   直接作为 show_report 的参数传入，效果和先 result = make_count() 再 show_report(result) 完全一样。
#   你答"不清楚" ❌ —— 没答出来。记住：函数返回值可以直接当另一个函数的参数传，不用先存变量。

# ---------- 错题回收批 ----------
# 【回收 1 · 抽 ⑬】product["price"] = "899"（str）
#   问 1：print(product["price"] + 1) 报 TypeError（str 和 int 不能相加）。
#         你答"要参与数字运算首先要转 int" 🔶 方向对，但没点明报错类型是 TypeError。
#   问 2：print(int(product["price"]) + 1) 输出 900  ✅ 对（这次数字对，899+1=900）

# 【回收 2 · 抽 ⑱】get_city 只 return company.get("city", "未知")
#   问 1：print(get_city({"name":"越疆","city":"深圳"})) → 深圳  ✅ 对
#   问 2：print(get_city({"name":"乐聚"})) → 未知，因为 .get("city","未知") 查不到 city 时返回默认"未知"，不崩。
#         你答"未知，因为有 .get()" ✅ 对（理由对，没多写 name）

# ---------- 错题库更新（11.03 批改后）----------
# ⑬（str 值参与运算要 int()）：问2对、问1半对 → 半对，续挂 11-06
# ⑱（.get() 默认值≠恒定输出）：两问全对 → 连对 2 次？不，⑱本次只算1次对，需看上次。上次10.30半对挂11-06。
#   本次两问全对 = 连对第 1 次 → 仍挂 11-06（等 11.06 再测，若再对就出库）
# 题1/题2（新错）：字典统计格式 + KeyError + .items() 格式 + 函数返回值直接传参 —— 新增 4 个新错，挂 7 天

# ============ 我的修正（读完点评后，把正确答案亲手写一遍，只列错题）============
# 规则：修正区只放答错的题，列原题 + 提示 + 空白作答位，不提前写答案。
# 全对/半对不列？—— 回收 1 问 2、回收 2 问 1、回收 2 问 2 全对不列；回收 1 问 1 半对列。
# 以下 5 处是你要补的（含 1 处半对）。
#
# 【题 1 问 1】原题：words = ["OK","ERR","OK","WARN","OK"]，统计完 counts 是什么？
#   原代码：
#     counts = {}
#     for w in words:
#         counts[w] = counts.get(w, 0) + 1
#     print(counts)
#   提示：统计字典格式是 {'键': 次数}，要带数字；OK 几次、ERR 几次、WARN 几次？
#   你的修正：{"OK": 3,"ERR":1,"WARN":1}
#
# 【题 1 问 2】原题：把循环里 counts[w] = counts.get(w, 0) + 1 改成 counts[w] = counts[w] + 1
#   （去掉 .get），第一次遇到 "OK" 时会发生什么？
#   原代码：
#     counts = {}
#     for w in words:
#         counts[w] = counts[w] + 1    # 去掉了 .get
#   提示：counts 一开始是 {}，里面没有 "OK" 这个键，直接 counts["OK"] 读会怎样？
#   你的修正：会报错 KeyError
#
# 【题 2 问 1】原题：show_report 里 print(key, ":", value) 用逗号分隔，输出格式是什么？
#   原代码：
#     def show_report(counts):
#         for key, value in counts.items():
#             print(key, ":", value)
#     result = make_count()   # make_count() 返回 {"OK":3,"ERR":1}
#     show_report(result)
#   提示：print 逗号分隔会加空格、字符串不带引号，是 "OK : 3" 还是 "OK": 3？
#   你的修正：OK : 3
#            ERR : 1 
#
# 【题 2 问 2】原题：把最后两行 result = make_count() 和 show_report(result)
#   改成 show_report(make_count())，输出会变吗？为什么？
#   原代码：
#     show_report(make_count())    # 直接传返回值
#   提示：函数返回值可以直接当另一个函数的参数传，不必先存变量。
#   你的修正：不会变，等价描述
#
# 【回收 1 问 1】原题：print(product["price"] + 1) 报什么错？类型是哪个？
#   原代码：
#     product = {"name": "灵巧手", "price": "899"}
#     print(product["price"] + 1)
#   提示：product["price"] 是 "899"（str），str + int 会报 TypeError。
#   你的修正：str + int 会报 TypeError

# ============ AI 复核（11.04 复核通过）============
# 5 处修正全部通过 ✅
#   ① 题 1 问 1：{'OK': 3, 'ERR': 1, 'WARN': 1} —— 对（统计字典带数字）
#   ② 题 1 问 2：KeyError —— 对（读不存在的键直接崩）
#   ③ 题 2 问 1：OK : 3 / ERR : 1 —— 对（print 逗号加空格，不带引号）
#   ④ 题 2 问 2：不会变，等价 —— 对（返回值直接传参等价）
#   ⑤ 回收 1 问 1：TypeError —— 对（str+int 报 TypeError）
# 第 10 期正式收尾 ✅
# 错题库：⑬（半对）续挂 11-06；⑱本次全对但上次半对，连对第 1 次，仍挂 11-06（下次再对出库）；
#         题 1/题 2 的 4 个新错经修正区通过补齐理解，按规则挂 7 天。

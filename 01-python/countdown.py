# countdown.py：硬指标倒计时
# 算出距离 deadline 还剩多少天、按每周小时数还能投入多少小时。
# 这是你的"倒计时仪表盘"，建议每天早上跑一次，比励志文章管用。

# ===== 1. 引入日期工具 =====
# from ... import ... 的含义：从 datetime 这个标准库模块里，把 date 类拿出来用
# date 类表示"年/月/日"（不带时分秒）
from datetime import date

# ===== 2. 变量区：改这里 =====
deadline = date(2027, 1, 31)   # 硬指标：入职截止日。date(年, 月, 日)，注意月从 1 开始
today = date.today()           # 自动取"今天"，不用手改。date.today() 从操作系统读当前日期
hours_per_week = 20            # 每周可投入小时数，int 型

# ===== 3. 计算剩余天数 =====
# 两个 date 相减，得到 timedelta（时间段）对象
# .days 是它的"天数"属性
delta = deadline - today
days_left = delta.days        # 今天(10-14)到 2027-01-31 = 109 天

# ===== 4. 计算可投入小时 =====
# 剩余天数换算成"周数"再乘以每周小时
# days_left / 7 得到"还剩多少周"，* hours_per_week 得到小时
# round() 四舍五入成整数，方便看
hours_left = round(days_left / 7 * hours_per_week)   # 109/7*20 ≈ 311 小时

# ===== 5. 输出 =====
# str() 把非字符串转成字符串，才能和文字用 + 拼接
print("今天是 " + str(today))
print("距离 " + str(deadline) + " 还有 " + str(days_left) + " 天")
print("按每周 " + str(hours_per_week) + " 小时算，还能投入约 " + str(hours_left) + " 小时")

# ===== 6. 进阶：自动取"当天"，不用手改 =====
# 第 2 段已改用 date.today() 自动取当天，这里不再重复
# 如果想手动指定"今天"做练习，把第 12 行改成 today = date(2026, 10, 14) 即可
print("\n[提示] today 用的是自动模式，明天跑会自动变成明天日期")
print("自动模式下距截止还有 " + str((deadline - today).days) + " 天")

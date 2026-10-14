# profile.py：个人信息卡片
# 用变量存你的跨行设定，输出一张信息卡。
# 这是 Day 2 的第 3 步，写完推送 GitHub 后，Day 2 过半。

# ===== 1. 变量区：改这里 =====
name = "Yangle"            # str：你的真名或常用名
target_city = "深圳"        # str：目标城市
target_industry = "具身智能"  # str：目标行业
deadline = "2027-01-31"    # str：硬指标日期（入职截止）
hours_per_week = 20        # int：每周可投入小时数

# ===== 2. 输出区：把变量拼成卡片 =====
# 用 + 和 str() 拼接，不用 f-string（f-string 是周四内容）
print("====== 跨行信息卡 ======")
print("姓名：" + name)
print("目标城市：" + target_city)
print("目标行业：" + target_industry)
print("硬指标：" + deadline)
print("每周投入：" + str(hours_per_week) + " 小时")   # hours_per_week 是 int，拼接前必须 str() 转
print("一年可投入约 " + str(hours_per_week * 52) + " 小时")   # 数字必须用运算算出，不许手写 1040
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
# Day 3 起改用 f-string：字符串前加字母 f，{} 里直接写变量名或表达式
# 对比 Day 2 的写法 "..." + str(x) + "..."，省掉了所有 str() 和 + 号
print("====== 跨行信息卡 ======")
print(f"姓名：{name}")                                  # {name} 直接把变量值填进来，自动转 str
print(f"目标城市：{target_city}")
print(f"目标行业：{target_industry}")
print(f"硬指标：{deadline}")
print(f"每周投入：{hours_per_week} 小时")                # int 也能直接填，不用 str()
print(f"一年可投入约 {hours_per_week * 52} 小时")        # {} 里能写运算：先算 20*52 再填
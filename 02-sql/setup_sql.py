# setup_sql.py —— SQL Day 1 建库建表脚本（11.03）
# 目标：用 sqlite3 建一个 robot_log.db，里面建 robot_log 表并插入 5 条测试数据。
# 用法：在 D:\embodied-ai-learning\02-sql 目录下跑 python setup_sql.py
#
# 【术语先定义】
# - sqlite3：Python 内置模块，用来操作 SQLite 数据库（一个 .db 文件，免安装）
# - CREATE TABLE：建表语句，定义有哪些列、每列什么类型
# - INSERT INTO：插入数据的语句
# - 主键（PRIMARY KEY）：每行唯一的编号，用来唯一标识一条记录

import sqlite3   # 引入 sqlite3 模块，才能操作数据库

# ① 连接数据库：如果 robot_log.db 不存在就自动创建，存在就打开
conn = sqlite3.connect("robot_log.db")

# ② 创建一个"游标"（cursor）：用它来执行 SQL 语句
cursor = conn.cursor()

# ③ 建表：如果表已存在就跳过（IF NOT EXISTS），定义 5 列
cursor.execute("""
    CREATE TABLE IF NOT EXISTS robot_log (
        id INTEGER PRIMARY KEY,     -- 主键，整数，唯一
        robot TEXT,                 -- 机器人名字，文本
        status TEXT,                -- 状态，文本（OK/ERR/WARN）
        duration INTEGER,           -- 任务耗时（秒），整数
        date TEXT                   -- 日期，文本（存成 'YYYY-MM-DD'）
    )
""")

# ④ 插入 5 条测试数据（一次插一条，对应上面的表）
cursor.execute("INSERT INTO robot_log (id, robot, status, duration, date) VALUES (1, '越疆', 'OK', 15, '2026-11-01')")
cursor.execute("INSERT INTO robot_log (id, robot, status, duration, date) VALUES (2, '帕西尼', 'ERR', 8, '2026-11-01')")
cursor.execute("INSERT INTO robot_log (id, robot, status, duration, date) VALUES (3, '乐聚', 'OK', 22, '2026-11-01')")
cursor.execute("INSERT INTO robot_log (id, robot, status, duration, date) VALUES (4, '越疆', 'WARN', 12, '2026-11-02')")
cursor.execute("INSERT INTO robot_log (id, robot, status, duration, date) VALUES (5, '帕西尼', 'OK', 19, '2026-11-02')")

# ⑤ 提交改动（保存到文件）—— 必须执行，否则数据只存在内存里，关掉就没了
conn.commit()

# ⑥ 验证：查一下表里现在有几行
cursor.execute("SELECT COUNT(*) FROM robot_log")
count = cursor.fetchone()[0]   # fetchone() 拿第一行，[0] 取第一个数字
print("robot_log 表当前行数：", count)

# ⑦ 关掉连接（好习惯，释放资源）
conn.close()

# 期望输出：robot_log 表当前行数： 5

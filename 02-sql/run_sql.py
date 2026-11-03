# run_sql.py —— SQL 查询执行器（11.03）
# 目标：把 SQL 语句传进来，连上 robot_log.db 执行，打印结果。
# 用法：python run_sql.py "SELECT * FROM robot_log"
# 举例：python run_sql.py "SELECT robot, status FROM robot_log"
#        python run_sql.py "SELECT DISTINCT status FROM robot_log"
#
# 【术语先定义】
# - sys.argv：命令行参数列表。sys.argv[1] 就是你敲的第一条 SQL（在引号里）
# - fetchall()：把查询结果的所有行一次性取出来，返回一个列表
# - 参数占位符 ?：execute 里用 ? 占位，后面参数用元组传，防止 SQL 注入（本脚本暂用简单方式）

import sqlite3
import sys

# ① 取命令行里传进来的 SQL 语句（sys.argv[1] 是第一条参数）
if len(sys.argv) < 2:
    print("用法：python run_sql.py \"你的 SQL 语句\"")
    sys.exit(1)   # 没有参数就退出

sql = sys.argv[1]

# ② 连接数据库（只读打开，不用建表）
conn = sqlite3.connect("robot_log.db")
cursor = conn.cursor()

# ③ 执行 SQL，取回所有行
cursor.execute(sql)
rows = cursor.fetchall()

# ④ 打印结果：每行一个，打印成列表形式
print(f"执行：{sql}")
print("结果（共", len(rows), "行）：")
for row in rows:
    print(row)

# ⑤ 关连接
conn.close()

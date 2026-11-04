-- day11_sql_group.sql —— 学习日 11：SQL 入门 3（GROUP BY 聚合）
-- 主题：GROUP BY 分组 + 聚合函数（COUNT/SUM/AVG/MAX/MIN）
-- ⚠️ 日期待填：等你真正学了这节，再把日期标到实际学习日
-- 配套：setup_sql.py（建表插数据）+ run_sql.py（执行器）
-- 用法：python run_sql.py "你的 SQL"

-- ===================== 一、聚合函数（把一列压缩成一个数）=====================

-- COUNT(*)：数总行数（5）
-- 跑：python run_sql.py "SELECT COUNT(*) FROM robot_log"
SELECT COUNT(*) FROM robot_log;

-- SUM(duration)：总耗时（15+8+22+12+19 = 76）
-- 跑：python run_sql.py "SELECT SUM(duration) FROM robot_log"
SELECT SUM(duration) FROM robot_log;

-- AVG(duration)：平均耗时（76/5 = 15.2）
-- 跑：python run_sql.py "SELECT AVG(duration) FROM robot_log"
SELECT AVG(duration) FROM robot_log;

-- MAX(duration)：最长耗时（22）
-- 跑：python run_sql.py "SELECT MAX(duration) FROM robot_log"
SELECT MAX(duration) FROM robot_log;

-- MIN(duration)：最短耗时（8）
-- 跑：python run_sql.py "SELECT MIN(duration) FROM robot_log"
SELECT MIN(duration) FROM robot_log;

-- ===================== 二、GROUP BY（按某列分组再统计）=====================

-- 按 robot 分组，数每台几条日志
-- 跑：python run_sql.py "SELECT robot, COUNT(*) FROM robot_log GROUP BY robot"
SELECT robot, COUNT(*) FROM robot_log GROUP BY robot;

-- 按 status 分组，数每种状态几条
-- 跑：python run_sql.py "SELECT status, COUNT(*) FROM robot_log GROUP BY status"
SELECT status, COUNT(*) FROM robot_log GROUP BY status;

-- 按 robot 分组，求每台总耗时
-- 跑：python run_sql.py "SELECT robot, SUM(duration) FROM robot_log GROUP BY robot"
SELECT robot, SUM(duration) FROM robot_log GROUP BY robot;

-- 按 status 分组，求每种状态平均耗时
-- 跑：python run_sql.py "SELECT status, AVG(duration) FROM robot_log GROUP BY status"
SELECT status, AVG(duration) FROM robot_log GROUP BY status;

-- ===================== 三、自写练习（你来写 3 个）=====================

-- 练习 1：按 robot 分组，数每台机器人有几行日志，只显示 robot 和 COUNT(*)。
--         期望：乐聚1 / 帕西尼2 / 越疆2
-- 你的 SQL：

-- 练习 2：按 status 分组，求每种状态的平均耗时，只显示 status 和 AVG(duration)。
--         期望：ERR 8.0 / OK 18.67 / WARN 12.0
-- 你的 SQL：

-- 练习 3：按 date 分组，数每天有几行日志。
--         期望：2026-11-01 有 3 行、2026-11-02 有 2 行
-- 你的 SQL：

-- ===================== self-test =====================
-- 练习 1 期望：乐聚1 / 帕西尼2 / 越疆2
-- 练习 2 期望：ERR 8.0 / OK 18.67 / WARN 12.0
-- 练习 3 期望：2026-11-01 有 3 行、2026-11-02 有 2 行

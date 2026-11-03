-- sql_01_select.sql —— SQL Day 1 学习材料（11.03 补）
-- 主题：建库建表 + SELECT 三种基本用法
-- 配套：setup_sql.py（建表插数据）+ run_sql.py（执行器）
-- 用法：python run_sql.py "你的 SQL"

-- ===================== 一、先看数据长什么样 =====================
-- 数据源：robot_log 表（setup_sql.py 已建好，5 条机器人日志）
-- 列：id（编号）/ robot（机器人）/ status（状态）/ duration（耗时秒）/ date（日期）

-- ===================== 二、SELECT 三种基本用法 =====================

-- 用法 1：查整张表（* 表示"所有列"）
-- 在终端跑：python run_sql.py "SELECT * FROM robot_log"
SELECT * FROM robot_log;

-- 用法 2：查指定列（只要 robot 和 status 两列）
-- 在终端跑：python run_sql.py "SELECT robot, status FROM robot_log"
SELECT robot, status FROM robot_log;

-- 用法 3：去重（DISTINCT 去掉重复值）
-- 在终端跑：python run_sql.py "SELECT DISTINCT status FROM robot_log"
-- 结果：OK / ERR / WARN（只出现一次的，因为重复的被去掉了）
SELECT DISTINCT status FROM robot_log;

-- ===================== 三、自写练习（你来写 2 个）=====================

-- 练习 1：查整张表，但只想要 robot 和 duration 两列。
--         写一条 SELECT，只取这两列，跑出来应该是 5 行。
-- 你的 SQL：

-- 练习 2：看看 robot_log 表里有哪些不同的 robot？
--         用 DISTINCT 查 robot 列，应该得到 越疆 / 帕西尼 / 乐聚 3 个。
-- 你的 SQL：

-- ===================== self-test =====================
-- 练习 1 期望：5 行，每行 (robot, duration)，如 ('越疆', 15)
-- 练习 2 期望：3 行，越疆 / 帕西尼 / 乐聚

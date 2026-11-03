-- sql_02_where.sql —— SQL Day 2 学习材料（11.03）
-- 主题：WHERE 过滤 + 比较运算符 + 逻辑运算符（AND/OR/NOT）
-- 配套：setup_sql.py（建表插数据）+ run_sql.py（执行器）
-- 用法：python run_sql.py "你的 SQL"

-- ===================== 一、比较运算符 =====================

-- 等于 = ：只拿"越疆"的日志（字符串要单引号）
-- 跑：python run_sql.py "SELECT * FROM robot_log WHERE robot = '越疆'"
SELECT * FROM robot_log WHERE robot = '越疆';

-- 不等于 != ：非 OK 状态
-- 跑：python run_sql.py "SELECT * FROM robot_log WHERE status != 'OK'"
SELECT * FROM robot_log WHERE status != 'OK';

-- 大于 > ：耗时超过 10 秒
-- 跑：python run_sql.py "SELECT robot, duration FROM robot_log WHERE duration > 10"
SELECT robot, duration FROM robot_log WHERE duration > 10;

-- 大于等于 >= ：耗时 ≥ 15 秒
-- 跑：python run_sql.py "SELECT * FROM robot_log WHERE duration >= 15"
SELECT * FROM robot_log WHERE duration >= 15;

-- 小于 < ：耗时不足 10 秒
-- 跑：python run_sql.py "SELECT * FROM robot_log WHERE duration < 10"
SELECT * FROM robot_log WHERE duration < 10;

-- 小于等于 <= ：耗时 ≤ 12 秒
-- 跑：python run_sql.py "SELECT * FROM robot_log WHERE duration <= 12"
SELECT * FROM robot_log WHERE duration <= 12;

-- ===================== 二、逻辑运算符 =====================

-- AND：两个条件都成立（越疆 且 状态OK）
-- 跑：python run_sql.py "SELECT * FROM robot_log WHERE robot = '越疆' AND status = 'OK'"
SELECT * FROM robot_log WHERE robot = '越疆' AND status = 'OK';

-- OR：至少一个成立（ERR 或 WARN）
-- 跑：python run_sql.py "SELECT * FROM robot_log WHERE status = 'ERR' OR status = 'WARN'"
SELECT * FROM robot_log WHERE status = 'ERR' OR status = 'WARN';

-- NOT：取反（非 OK）
-- 跑：python run_sql.py "SELECT * FROM robot_log WHERE NOT status = 'OK'"
SELECT * FROM robot_log WHERE NOT status = 'OK';

-- ===================== 三、自写练习（你来写 3 个）=====================

-- 练习 1：查"乐聚"这台机器人的所有日志（整行）。
--         写一条 SELECT ... WHERE robot = ...，应该得到 1 行。
-- 你的 SQL：

-- 练习 2：查耗时超过 15 秒的日志，只要 robot 和 status 两列。
--         应该得到 2 行（乐聚22、帕西尼19）。
-- 你的 SQL：

-- 练习 3：查"帕西尼"且状态不是"OK"的日志（AND + != 组合）。
--         应该得到 1 行（帕西尼 ERR）。
-- 你的 SQL：

-- ===================== self-test =====================
-- 练习 1 期望：1 行，乐聚 OK 22
-- 练习 2 期望：2 行，('乐聚', 'OK') 和 ('帕西尼', 'OK')
-- 练习 3 期望：1 行，帕西尼 ERR 8

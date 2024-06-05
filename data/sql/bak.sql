-- --------------------------------------------------------
-- 主机:                           C:\Users\Vincent\Documents\code\students-assignments\data\database.db
-- 服务器版本:                        3.44.0
-- 服务器操作系统:                      
-- HeidiSQL 版本:                  12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES  */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- 导出 database 的数据库结构
CREATE DATABASE IF NOT EXISTS "database";
;

-- 导出  表 database.assignment 结构
CREATE TABLE IF NOT EXISTS assignment (
    assignment_id VARCHAR(50) PRIMARY KEY,
    teacher_id VARCHAR(50) NOT NULL,
    assignment_name VARCHAR(50) NOT NULL,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) ON UPDATE CASCADE ON DELETE NO ACTION
);

-- 正在导出表  database.assignment 的数据：10 rows
/*!40000 ALTER TABLE "assignment" DISABLE KEYS */;
INSERT INTO "assignment" ("assignment_id", "teacher_id", "assignment_name") VALUES
	('FA20240601', 't2024001', '危险的想法与刑法'),
	('FA20240602', 't2024001', '法外狂徒与完整的刑法'),
	('EXP20240601', 't2024002', '铁山靠基本动作与衍生舞蹈'),
	('YS20240101', 't2024003', '必修1高等元素论'),
	('YS20240102', 't2024003', '必修2普通破盾学'),
	('YS20240103', 't2024003', '必修3伤害乘区论'),
	('YS20240104', 't2024003', '必修4韧性力学'),
	('YS20240105', 't2024003', '必修5反应详解'),
	('YS20240106', 't2024003', '抽卡时的心态管理'),
	('LC20240106', 't2024010', '只有苹果才能做到');
/*!40000 ALTER TABLE "assignment" ENABLE KEYS */;

-- 导出  表 database.students 结构
CREATE TABLE IF NOT EXISTS students (
    student_id VARCHAR(50) PRIMARY KEY,
    student_name VARCHAR(50) NOT NULL
);

-- 正在导出表  database.students 的数据：10 rows
/*!40000 ALTER TABLE "students" DISABLE KEYS */;
INSERT INTO "students" ("student_id", "student_name") VALUES
	('202412340101', '坤一'),
	('202412340102', '熊二'),
	('202412340103', '张三'),
	('202412340104', '李四'),
	('202412340105', '王五'),
	('202412340106', '赵六'),
	('202412340107', '孙七'),
	('202412340108', '周八'),
	('202412340109', '吴九'),
	('202412340110', '郑十');
/*!40000 ALTER TABLE "students" ENABLE KEYS */;

-- 导出  表 database.submits 结构
CREATE TABLE IF NOT EXISTS submits (
    student_id VARCHAR(50) NOT NULL,
    assignment_id VARCHAR(50) NOT NULL,
    FOREIGN KEY (assignment_id) REFERENCES assignment(assignment_id) ON UPDATE CASCADE ON DELETE NO ACTION,
    FOREIGN KEY (student_id) REFERENCES students(student_id) ON UPDATE CASCADE ON DELETE NO ACTION
);

-- 正在导出表  database.submits 的数据：10 rows
/*!40000 ALTER TABLE "submits" DISABLE KEYS */;
INSERT INTO "submits" ("student_id", "assignment_id") VALUES
	('202412340103', 'FA20240601'),
	('202412340104', 'FA20240601'),
	('202412340103', 'FA20240602'),
	('202412340101', 'YS20240106'),
	('202412340102', 'YS20240106'),
	('202412340104', 'YS20240106'),
	('202412340105', 'YS20240106'),
	('202412340106', 'YS20240106'),
	('202412340107', 'YS20240106'),
	('202412340108', 'YS20240106');
/*!40000 ALTER TABLE "submits" ENABLE KEYS */;

-- 导出  表 database.teachers 结构
CREATE TABLE IF NOT EXISTS teachers (
    teacher_id VARCHAR(50) PRIMARY KEY,
    teacher_name VARCHAR(50) NOT NULL
);

-- 正在导出表  database.teachers 的数据：10 rows
/*!40000 ALTER TABLE "teachers" DISABLE KEYS */;
INSERT INTO "teachers" ("teacher_id", "teacher_name") VALUES
	('t2024001', '罗翔'),
	('t2024002', '蔡徐坤'),
	('t2024003', '派蒙'),
	('t2024004', '温迪'),
	('t2024005', '钟离'),
	('t2024006', '雷电影'),
	('t2024007', '纳西妲'),
	('t2024008', '芙宁娜'),
	('t2024009', '刘伟'),
	('t2024010', '库克');
/*!40000 ALTER TABLE "teachers" ENABLE KEYS */;

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;

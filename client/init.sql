-- 删除已经存在的表
DROP TABLE IF EXISTS "students";
DROP TABLE IF EXISTS "teachers";
DROP TABLE IF EXISTS "assignment";
DROP TABLE IF EXISTS "submits";
-- 创建学生表
CREATE TABLE "students" (
	"student_id" VARCHAR(50) NOT NULL,
	"student_name" VARCHAR(50) NOT NULL,
	PRIMARY KEY ("student_id")
)
;
-- 创建教师表
CREATE TABLE "teachers" (
	"teacher_id" VARCHAR(50) NOT NULL,
	"teacher_name" VARCHAR(50) NOT NULL,
	PRIMARY KEY ("teacher_id")
)
;
-- 创建作业布置表
CREATE TABLE "assignment" (
	"assignment_id" VARCHAR(50) NOT NULL,
	"teacher_id" VARCHAR(50) NOT NULL,
	"assignment_name" VARCHAR(50) NOT NULL,
	PRIMARY KEY ("assignment_id")
	CONSTRAINT "0" FOREIGN KEY ("teacher_id") REFERENCES "teachers" ("teacher_id") ON UPDATE CASCADE ON DELETE NO ACTION
)
;
-- 创建作业统计表
CREATE TABLE "submits" (
	"student_id" VARCHAR(50) NOT NULL,
	"assignment_id" VARCHAR(50) NOT NULL,
	CONSTRAINT "0" FOREIGN KEY ("assignment_id") REFERENCES "assignment" ("assignment_id") ON UPDATE CASCADE ON DELETE NO ACTION,
	CONSTRAINT "1" FOREIGN KEY ("student_id") REFERENCES "students" ("student_id") ON UPDATE CASCADE ON DELETE NO ACTION
)
;
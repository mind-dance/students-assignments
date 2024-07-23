-- 删除已经存在的表
DROP TABLE IF EXISTS students;
DROP TABLE IF EXISTS submits;

-- 创建学生表
CREATE TABLE "students" (
    "sid" TEXT PRIMARY KEY,
    "sname" VARCHAR(50) NOT NULL
);

-- 创建作业统计表
CREATE TABLE "submits" (
	"sid" TEXT NOT NULL,
	"hw" TEXT NULL,
	"status" INTEGER NOT NULL DEFAULT 0,
	"path" TEXT NULL,
	FOREIGN KEY ("sid") REFERENCES "students" ("sid") ON UPDATE CASCADE ON DELETE CASCADE
);
--
-- 由SQLiteStudio v3.2.1 产生的文件 周日 6月 28 20:10:19 2020
--
-- 文本编码：UTF-8
--
PRAGMA foreign_keys = off;
BEGIN TRANSACTION;

-- 表：Dorm
CREATE TABLE Dorm (
    Time        TEXT   PRIMARY KEY
                       NOT NULL
                       DEFAULT (datetime('now', 'localtime') ),
    Temperature DOUBLE NOT NULL,
    Humidity    DOUBLE NOT NULL
);


COMMIT TRANSACTION;
PRAGMA foreign_keys = on;

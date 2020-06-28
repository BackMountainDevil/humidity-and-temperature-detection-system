# humidity-and-temperature-detection-system
Humidity and temperature detection systembased on ESP8266 and DH11.[基于ESP8266和DH11的温湿度检测系统](https://blog.csdn.net/weixin_43031092/article/details/107006663)
[矫情文章传送](http://kearney.club/2020/06/23/%E5%AE%BF%E8%88%8D%E5%86%85%E7%9A%8424h%E7%9A%84%E6%B0%94%E8%B1%A1%E7%9B%91%E6%B5%8B/)
[技术文章和效果传送](https://blog.csdn.net/weixin_43031092/article/details/107006663)

# 文件目录
IotClient     ESP8266的程序
IoTServer.py  服务端程序
Dorm.sql      数据库的表结构文件
jsontest.py   python测试jason用例
# 如何使用

# sqlite数据库示例
在Dorm.sql中有数据库表的结构，如果不够清楚的话。。。留下一个当时建库建表的操作记录
```bash
[root@ecs ~]# sqlite3  IoT.db
SQLite version 3.26.0 2018-12-01 12:34:55
Enter ".help" for usage hints.

sqlite> .databases
main: /root/IoT.db

sqlite> CREATE TABLE Dorm(
   Time TEXT PRIMARY KEY     NOT NULL DEFAULT (datetime('now','localtime')),
	Temperature    DOUBLE    NOT NULL,
	 Humidity       DOUBLE    NOT NULL
);

sqlite> .tables
Dorm
//sqlite> DROP TABLE Dorm;

sqlite> INSERT INTO Dorm(Temperature,Humidity) VALUES (25.6,26.6);
sqlite> SELECT * FROM Dorm;
```

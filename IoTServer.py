'''
/**********************************************************************
项目名称/Project          : 零基础入门学用物联网
程序名称/Program name     : cs-s-py.py
团队/Team                : 
作者/Author              : Kearney
日期/Date（YYYYMMDD）     : 20200628
程序目的/Purpose          : 
演示如何实现NodeMCU间通过WiFi进行与服务器通讯。服务端采用python接收数据，
ESP8266以客户端模式运行并将数据发往服务器的8888端口（可自定义），

 
此代码为服务端代码。此代码主要功能：
    - 通过HTTP协议接收来自客户端的数据并将数据存储到数据库
-----------------------------------------------------------------------
修订历史/Revision History  
日期/Date    作者/Author      参考号/Ref    修订说明/Revision Description
-----------------------------------------------------------------------
***********************************************************************/
'''
import threading
import socket
import json
import sqlite3

encoding = 'utf-8'
BUFSIZE = 2048    #缓冲区大小，可自定义

#将数据插入数据库的函数
def insertSql(temp,humi):
    conn = sqlite3.connect('IoT.db')
    if(conn):
        #print( "Opened database successfully")
        c = conn.cursor()
        cursor = c.execute("INSERT INTO Dorm(Temperature,Humidity) VALUES ('{}','{}')".format( temp,humi) )
        conn.commit()
        #print ("Insert success")
        conn.close()
    else:
        print ("Opened database fail!!!")
    #print ("DB close")

##读取端口消息
class Reader(threading.Thread):
    def __init__(self, client):             ##获取客户端
        threading.Thread.__init__(self)
        self.client = client

    def run(self):                  ##持续接收消息并处理
        while True:
            data = self.client.recv(BUFSIZE)        ##接收字节消息
            if (data):
                string = bytes.decode(data, encoding)           ##转化为字符串
                print()
                #print(string)               ##打印接收到的消息
                #print(type(string))
                data2 = json.loads(string)
                temp = data2['temp']
                humi = data2['humi']
                #print(temp)
                #print(humi)
                insertSql(temp,humi)
                print()
                #self.client.send("Received data successfully")##回复消息
            else:
                break
        # print("close:", self.client.getpeername())        

##建立端口监听
class Listener(threading.Thread):
    def __init__(self, port):
        threading.Thread.__init__(self)
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind(("0.0.0.0", port))
        self.sock.listen(0)

    def run(self):
        print("listener started")
        while True:
            client, cltadd = self.sock.accept()
            Reader(client).start()
            client.send("Test from py".encode())
            cltadd = cltadd
            # print("accept a connect")

try:  
    lst = Listener(8888)  # 建立监听线程，端口号根据需要修改
    lst.start()  # 启动监听
except SocketError as e:
    if e.errno != errno.ECONNRESET:
        raise
    pass    

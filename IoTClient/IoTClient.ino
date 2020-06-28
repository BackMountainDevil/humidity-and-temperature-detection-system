/**********************************************************************
项目名称/Project          : 零基础入门学用物联网
程序名称/Program name     : cs-s-py.py
团队/Team                : 
作者/Author              : Kearney
日期/Date（YYYYMMDD）     : 20200628
程序目的/Purpose          : 
演示如何实现NodeMCU间通过WiFi进行与服务器通讯。服务端采用python接收数据，
ESP8266以客户端模式运行并将数据发往服务器的8888端口（可自定义），

 
此代码为客户端代码。此代码主要功能：
    - 通过HTTP协议将采集到的温湿度数据发往服务器的8888端口
数据样式：json
    {'temp': 31.25, 'humi': 30.50}
DH11：
温度（摄氏度） 0.00-50.00  精度2.00
湿度 20.00%-80.00%   精度5.00%
-----------------------------------------------------------------------
修订历史/Revision History  
日期/Date    作者/Author      参考号/Ref    修订说明/Revision Description
-----------------------------------------------------------------------
***********************************************************************/

#include <Adafruit_Sensor.h>
#include <DHT.h>
#include <DHT_U.h>
#include <ESP8266WiFi.h>

const char* ssid = "Kearney";        //wifi名称，请修改为自己家的wifi信息
const char* password = "123456789";  //wifi密码，请修改为自己家的wifi信息
const char* host = "111.111.111.111";    //服务器公网ip，请修改为自己的服务器的公网IP
const int httpPort = 8888;              //服务器端口号，请修改为自己的服务器的端口

#define DHTPIN D4     
int delayMS = 600000 ;   //测量时间间隔10mins = 10*60*1000 ms

String payloadJson = "";
float temp;   
float humi; 

#define DHTTYPE    DHT11     
DHT_Unified dht(DHTPIN, DHTTYPE);

void setup() {
  Serial.begin(9600);
  
  Serial.println("");
  Serial.println("Begin");
  WiFi.begin(ssid, password);               //使用名称和密码链接wifi
  while (WiFi.status() != WL_CONNECTED) {   //如果连接成功跳出循环,没成功则一直尝试连接
    delay(500);
    Serial.print(".");
  }
  Serial.println("");
  Serial.println("WiFi connected");
  
  dht.begin();

  sensor_t sensor;
  dht.temperature().getSensor(&sensor);
  dht.humidity().getSensor(&sensor);
}

void loop() {
  sensors_event_t event;
  dht.temperature().getEvent(&event);         //采集温度
  if (isnan(event.temperature)) {
    Serial.println(F("Error reading temperature!"));
  }
  else {
    temp = event.temperature;

  }
  

  dht.humidity().getEvent(&event);        //采集湿度
  if (isnan(event.relative_humidity)) {
    Serial.println(F("Error reading humidity!"));
  }
  else {
    humi = event.relative_humidity;
  }

  payloadJson = "{\"temp\": ";
  payloadJson += String(temp);  
  payloadJson += ", \"humi\": "; 
  payloadJson += String(humi);  
  payloadJson += "}";  
  Serial.println( payloadJson);


 Serial.println("Start Connecting ...  ");
  WiFiClient client;    // 建立WiFi客户端对象，对象名称client

  if(client.connect(host,httpPort)){    //向服务器发送连接请求
    Serial.print("Connecting Successfully to ");
    Serial.print(host);  
    Serial.print("  :  ");   
    Serial.println(httpPort);     

    Serial.print("Current Client Status: ");  //获取设备与服务器的连接状态
    Serial.println(client.status());          //4代表成功建立连接，10代表连接超时
    

    client.print(payloadJson);     // 向服务器发送数据
    Serial.print("Sending Data:  ");
    Serial.println(payloadJson);
    

  }
  else{//连接失败
    Serial.println("Connect Failed");
    Serial.print(WiFi.localIP());
    return;
  }
  client.stop();    //关闭连接
  Serial.println("Connection Closed ");
  Serial.println("END");
  Serial.println();
  delay(delayMS);
}

'''
解析json数据
'''
import json

json_str2 = '{"programers":[ {"firstName":"Breet","lastName":"MMM","email":"XXX"},'\
            '{"firstName":"Breet","lastName":"MMM","email":"XXX"}], ' \
            '"author": [{"firstName": "su", "lastName": "yang", "email": "XXX"},'\
            '{"firstName": "Breet", "lastName": "MMM", "email": "XXX"}]}'

data2 = json.loads(json_str2)

print(type(json_str2))
print(data2['author'])

stringData = '{"temp": 32.90, "humi": 38.00}'
#stringData = "{'temp': 32.90, 'humi': 38.00}"
'''
震惊，单双引号导致的错误
'''
data = json.loads(stringData)
print(type(stringData))
print(data['temp'])

'''
jsonData = {'temp': 32.40, 'humi': 40.00}
strData = "{'temp': 32.40, 'humi': 40.00}"
print(jsonData['temp'])
#print(strData['temp'])

json = json.loads(strData)
print (json)

                
'''

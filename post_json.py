#coding:utf-8
import requests,json
 
#第一行注解的#coding:utf-8表示可以支持中文，不然代码里面有中文会报错
url = "http://10.2.3.222:8080"
headers = {"Content-Type":"application/x-www-form-urlencoded"}
data1 = {"face_set_id":"1","people_id":"20220291"}
data = {"type":"req","id":"82104128-a1ad-4161-aa83-f0fac85f3ee3","name":"GetFaceList","body":data1}
r = requests.post(url = url,data = json.dumps(data),headers = headers)
print(r)
print('result=' + r.text)
#print(r.url)
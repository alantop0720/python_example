import requests
import os
import json

url = "http://10.2.3.222:8080"

file = 'D:/hk/fullface/310109111201805220785zp1.jpg'


headers = {'Content-type': 'multipart/form-data'}

data1 = {"face_set_id": "1",\
         "people_id": "999999",\
        "image": "msg://1"}
payload ={"type": "req",\
       "id": "82104128-a1ad-4161-aa83-f0fac85f3ee3",\
       "name": "AddFace","body":data1}

files = {
     'json': (None, json.dumps(payload), 'multipart/form-data'),
     'file': (os.path.basename(file), open(file, 'rb'), 'application/octet-stream')
}
 
r = requests.post(url, files=files)
print(r)
print(r.text)
 




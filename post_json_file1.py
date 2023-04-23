import requests



url = 'http://10.2.3.222:8080'

data1 = {"face_set_id": "1",\
         "people_id": "999999",\
        "image": "msg://1"}
payload ={"type": "req",\
       "id": "82104128-a1ad-4161-aa83-f0fac85f3ee3",\
       "name": "AddFace","body":data1}

file = 'D:/hk/fullface/310109111201805220785zp1.jpg'

files = {'files': (file, open(file, 'rb'), 'image/jpeg')}
r = requests.post(url, files=files, data=payload)
print(r.status_code)
print(r.text)


import requests
import base64
print('For exit enter -1 :')
while True :
    pic_num = input('Enter your picture number:')
    if pic_num == '-1' :
        break
    mode = input('Enter your reques, Serial or FaceDetection?')
    data = {'pic_name':f'{pic_num}.jpg', 'func':mode}
    r = requests.get('http://localhost:5050/', data=data)
    res = r.json()
    if res['status'] == 'OK':
        f = open('res.png','wb')
        f.write(base64.b64decode(res['content']))
        print(res['msg'])
    else:
        print(res['content'])
    

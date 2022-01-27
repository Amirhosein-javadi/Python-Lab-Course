import hug, cv2
import glob, base64

def face_detector(picname):
    image = cv2.imread(picname)
    image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades+\
                                         'haarcascade_frontalface_default.xml')
    faces = face_cascade.detectMultiScale(image_gray)
    
    for x, y, width, height in faces:
        cv2.rectangle(image, (x, y), (x + width, y + height), color=(255, 0, 0), thickness=2)
    if len(faces) == 0:
        return (0,picname)
    else :
        cv2.imwrite(f"/tmp/{picname}", image)
        return (len(faces), f"/tmp/{picname}")

@hug.get('/')
def get_image(pic_name, func):
    if func == 'Serial':
        if pic_name in img_list:
            b64img = base64.b64encode(open(pic_name,'rb').read())
            return { 'status':'OK', 'content':b64img, 'msg':'Your picture is finded!' }
        else:
            return {'status':'NOK', 'content':'Sorry, but this image does not exist :(\n'}
    elif func == 'FaceDetection':
        if pic_name in img_list:
            n, picStr = face_detector(pic_name)
            b64img = base64.b64encode(open(picStr,'rb').read())
            return { 'status':'OK', 'content': b64img, 'msg':'There is a face!' if n else 'No face detected!' }
        else:
            return {'status':'NOK', 'content':'Sorry, but this image does not exist :(\n'}
    else:
        return {'status':'dorost nis!', 'content':'Not valid func'}


img_list = glob.glob('*.png')
img_list += glob.glob('*.jpg')


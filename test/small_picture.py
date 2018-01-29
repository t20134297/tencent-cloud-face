from PIL import Image, ImageTk
im = Image.open('1cp1.jpeg')
out = im.resize((280, 360),Image.ANTIALIAS)
path='/home/ansheng/Desktop/face_detect/test/ssss'
out.save('1chenpeng.jpeg', 'jpeg')

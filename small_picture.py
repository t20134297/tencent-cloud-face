from PIL import Image, ImageTk
im = Image.open('6zww1.jpeg')
out = im.resize((280, 360),Image.ANTIALIAS)

out.save('6zhangwuwei.jpeg', 'jpeg')

from PIL import Image, ImageTk
im = Image.open('T.jpeg')
out = im.resize((280, 360),Image.ANTIALIAS)

out.save('46.jpeg', 'jpeg')

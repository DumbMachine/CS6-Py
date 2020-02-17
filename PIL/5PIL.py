from PIL import Image
img = Image.open("Abc.jpg","r")

datas = img.getdata()

for item in datas:
    print("({},{},{}".format(255-item[0],255-item[1],255-item[2]))
       

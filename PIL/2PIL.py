from PIL import Image 
img = Image.open("picture.jpg")  
img.thumbnail((200, 200)) 
img.save("Tpic.jpg")
img.show()

from PIL import Image
img = Image.open("picture.jpg") 
width, height = img.size 
#resize
img = img.resize((width/2, height/2))          
img.save("resized_picture.jpg")
img.show()
#Converting to grayscale
image = img.convert('L')
image.show()
#Cropping the image
left = 5
top = height / 4
right = 164
bottom = 3 * height / 4
im1 = img.crop((left, top, right, bottom))  
im1.show()
#Rotating image
angle = eval(input("Enter the angle: "))
img.rotate(45).show()

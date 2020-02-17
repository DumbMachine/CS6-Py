from PIL import Image
img = Image.open("abc.jpg",'r')
pixels = img.load()
for i in range(img.size[0]):    
    for j in range(img.size[1]):    
        pixels[i,j] = (pixels[i,j][0]+5, pixels[i,j][1]+5, pixels[i,j][2]+5) 
img.show()

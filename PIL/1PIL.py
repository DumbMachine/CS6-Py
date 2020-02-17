from PIL import Image
im = Image.open('abc.jpg','r')
im.show()
print(im.mode)
pix_val = list(im.getdata())
pixVal = [x for sets in pix_val for x in sets]
print(pixVal)

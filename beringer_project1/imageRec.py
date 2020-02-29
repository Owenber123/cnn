from PIL import Image
import PIL
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

#change this path to where the image you want to resize is
image_path = "C:/Users/msmai/Desktop/ADD final/2.png"
original_image = Image.open(image_path)

#this is for printing the image.. not necessary later
canvas = plt.gcf()
size = canvas.get_size_inches()
canvas.set_size_inches(size*2)

#finding the size of the image
old_width, old_height = original_image.size
print("Image size: {}x{} pixels.".format(old_width, old_height))
_ = plt.imshow(original_image)


#Math to resize 
resize_factor_width = (old_width/28)
resize_factor_height = (old_height/28)
new_width = int(old_width/resize_factor_width)
new_height = int(old_height/resize_factor_height)

#resizing image
resized_image = original_image.resize((new_width, new_height), Image.BILINEAR)

#printing new image size and the picture itself
print("Image size: {}x{} pixels.".format(new_width, new_height))
_ = plt.imshow(resized_image)

#save the resized image
resized_image= resized_image.save("resized_image.png")
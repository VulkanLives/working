import os
from os import path, walk
import platform
import sys
import re


joke_path = []
#'/home/chris/PycharmProjects/TTA/app_images/jokes'
foldersx = []
pngFilesx = []
background_img2x = []
background_img3x = []
meme_imagesx = []
dice_imgx = []
jpeg_imgsx = []
img_path = str

print(platform.system())
os_name = platform.system()
if os_name == "Windows":
    img_path = 'C:/Users/creid/PycharmProjects/TTA/classes/app_images/backgrounds/'
    print("yes yes")
else:
    img_path= '/home/chris/PycharmProjects/TTA/app_images/backgrounds/'
    print("no on  nonono ")
    

class ImageBank:

    def __init__(self) -> None:
       # self.background_img2x = []
        self.pngFilesx = pngFilesx
        self.background_img2x = background_img2x
        self.background_img3x = background_img3x
        self.meme_images = []
        self.dice_img = []
        self.jpeg_imgs = jpeg_imgsx
        self.img_path = img_path
        print(img_path)

        for dirpath, dirnames,filenames in walk(str(img_path)):

            for filename in filenames:
                if filename.endswith(".png"):
                    pngFilesx.append(filename)
                   # background_img2x.append(path.abspath(filename))
                    background_img3x.append(path.join(dirpath,filename))
                 #   print("BFORE files for back ground " + str(background_img2x))
                elif filename.endswith(".jpeg"):
                    jpeg_imgsx.append(filename)

                print("NEW ARRAY: files for back ground " + str(background_img3x))
        return


ImageBank()
my_str = background_img3x[1]
word_list = my_str.split()  # list of words
print(str(word_list))
print("AFTER files for back ground " + str(background_img3x))
print("AFTER files for back ground " + str(pngFilesx))



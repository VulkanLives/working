import os
from typing import List, Any

folders = []
pngFiles = []
background_imgs=[]
meme_images = []

dice_img = []

class ImageBank():
   array_y: list[str] = []
    #look through the foler specified for png files.
    # why do this? instead of just writing them into an array myself?
    #should allow me to copy a paste new pic into folders an dit will pick them up
    #could probably do it by using python to add file then saving the path but that will be later down the the line
   def __int__(self, bg_array):
       self.bg_array = bg_array
       for dirpath, dirnames, filenames in os.walk('/classes/app_images/backgrounds'):
          for filename in filenames:
                if filename.endswith(".png"):
                    pngFiles.append(filename)
                    background_imgs.append(os.path.abspath(filename))
                    background_imgs.append(os.path.abspath(os.path.join(dirpath, filename)))
   array_y = background_imgs

ImageBank()
print(background_imgs)
print(background_imgs)





# class ImageBank:
#
#     print("Listing Python file:")
#     for dirpath, dirnames, filenames in os.walk("."):
#         for filename in filenames:
#             if filename.endswith(".png"):
#                 pngFiles.append(filename)
#        # for dirname in dirnames in os.walk("/background"):
#            # print("yes" + str(dirname))
#         for name in dirnames:
#             folders.append(name)



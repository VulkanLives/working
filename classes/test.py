import os


class ImageBank:
    back_imgs = []
    #look through the foler specified for png files.
    # why do this? instead of just writing them into an array myself?
    #should allow me to copy a paste new pic into folders an dit will pick them up
    #could probably do it by using python to add file then saving the path but that will be later down the the line
    def __int__(self, bg_array):
        self.bg_array = bg_array
        for dirpath, dirnames, filenames in os.walk('/app_images/backgrounds'):
           for filename in filenames:
                if filename.endswith(".png"):
                    self.bg_array.append(os.path.abspath(os.path.join(dirpath, filename)))

        print(self.bg_array)
        print(bg_array)
        return(bg_array)

imagebank = ImageBank()
print(ImageBank.back_imgs)



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



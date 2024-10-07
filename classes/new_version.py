import tkinter as Tk
import random
from tkinter import messagebox
import customtkinter as ctk
from customtkinter import CTkImage

import roll_dice as rd
from PIL import Image

from classes.imageBank import ImageBank

#from imageBank import background_imgs


ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
root= ctk
app.title("TableTop Allie")
app.geometry("800x600", )  # set starting window size
app.resizable(width=False, height=True)

def show_roll_order(s_order):
    dice_order = int(s_order)
    print(s_order)

top_frame = root.CTkFrame(master=app, fg_color="orange", border_width=2, border_color="black")
# note: the side=top makes the object stick highest point in the of the window when resizing whislt running
top_frame.pack(side="top", fill="both", expand=True)
bottom_frame = root.CTkFrame(master=app, fg_color="blue", border_width=2, border_color="black")
bottom_frame.pack(side="top", fill="both", expand=True)


user_frame =ctk.CTkFrame(master=top_frame, border_width=2, width= 200, border_color="black")
# note: the side=top makes the object stick highest point in the of the window when resizing whislt running
user_frame.pack(side="left", fill="both", expand=False)

result_frame =root.CTkFrame(master=top_frame, fg_color="blue", border_width=2, border_color="black")
result_frame.pack(side="left", fill="both", expand=True)
dice_order_frame = Tk.LabelFrame(master=top_frame, text="Order of the rolls")

#

frame3 = root.CTkFrame(master=bottom_frame, fg_color="orange", border_width=2, border_color="black")
frame3.pack()
bg_img = root.CTkImage(Image.open("app_images/backgrounds/scene2.png"), size=(300, 300))
bg_img_label = ctk.CTkLabel(master=frame3, image=bg_img)
bg_img_label.pack(side = 'left',fill = 'both', expand = 1)


#print(image_index.__len__())
#attempt making a rolling background list by creaating arrays in the class ImageBank2
#and using Random to call
random_image = str(ImageBank.background_imgs[random.randint(0,int(ImageBank.background_imgs.__len__()))])
print("random image" + str(random_image))
bg_img2: CTkImage= root.CTkImage(Image.open(str(random_image)), size=(300, 300))
bg_img_label2 = ctk.CTkLabel(master=frame3, image=bg_img)
bg_img_label2.pack(side= 'right', fill = 'both', expand = 1)


e = root.CTkEntry(master=user_frame, border_width=1)
e.pack(side='top')




def roll(event=None):
    global result_array
    try:
        x = int(e.get())
        rd.RollDice(x)
        result_array = rd.occurance_list
        pass
    except ValueError:
        messagebox.showwarning("Invalid Entry", "Numbers only please")  # first text is title of new window
        e.delete(0, 'end')  # clear entry box
        e.focus()  # make cursor active in entry box
    display_result(result_array)



def dice_results_in_order():
    global result_list
    dice_order_frame.grid(row=15, column=4)

roll_btn = root.CTkButton(master=user_frame, text="Roll Dice",
                          command=roll)  # "command" makes the calls the above function, fg is text colour "foreground" and Bg = background


def load_user_frame():
    global label_one
    my_font = root.CTkFont(family="Helvetica", size=44, weight="bold")  # weight bold/normal, slant=italic/roman

    root.CTkLabel(master=result_frame, fg_color="grey", text_color="orange", width=1, text='\u2680', font=my_font).grid(row=1, column=1, padx=1)
    label_one = root.CTkLabel(master=result_frame, fg_color="white", width=1, height=1, text=str(rd.occurance_list[0]),
                              font=my_font).grid(row=1, column=2, padx=1)
    root.CTkLabel(master=result_frame, fg_color="white", text='\u2681', font=my_font).grid(row=2, column=1, padx=10)
    label_two = root.CTkLabel(master=result_frame, fg_color="white", width=1, height=1, text=str(rd.occurance_list[1]), font=my_font).grid(
        row=2, column=2, padx=10)
    root.CTkLabel(master=result_frame, fg_color="white", text="\u2682", font=my_font).grid(row=3, column=1, padx=10)
    label_three = root.CTkLabel(master=result_frame, fg_color="white", width=1, height=1, text=str(rd.occurance_list[2]),
                                font=my_font).grid(row=3, column=2, padx=10)
    root.CTkLabel(master=result_frame, fg_color="white", text="\u2683", font=my_font).grid(row=4, column=1, padx=10)
    label_four = root.CTkLabel(master=result_frame, fg_color="white", width=1, height=2, text=str(rd.occurance_list[3]), font=my_font).grid(
        row=4, column=2, padx=10)
    root.CTkLabel(master=result_frame, fg_color="white", text="\u2684", font=my_font ).grid(row=5, column=1, padx=10)
    label_five = root.CTkLabel(master=result_frame, fg_color="white", width=1, height=2, text=str(rd.occurance_list[4]), font=my_font).grid(
        row=5, column=2, padx=10)
    root.CTkLabel(master=result_frame, fg_color="white", text="\u2685", font=my_font).grid(row=6, column=1, padx=10)
    label_six = root.CTkLabel(master=result_frame, fg_color="white", width=1, height=2,text=str(rd.occurance_list[5]), font=my_font).grid(
        row=6, column=2, padx=10)

def display_result(res_array):

    root.CTkLabel(master=user_frame, fg_color="white", width=1, text='\u2680' + str(res_array[0])).pack(padx= 15,side='left')
    root.CTkLabel(master=user_frame, fg_color="white", text='\u2681' + str(res_array[1])).pack(padx= 15,side='left')
    root.CTkLabel(master=user_frame, fg_color="white", text="\u2682 = " + str(res_array[2])).pack(padx= 15,side='left')
    root.CTkLabel(master=user_frame, fg_color="white", text="\u2683 = " + str(res_array[3])).pack(padx= 15,side='left')
    root.CTkLabel(master=user_frame, fg_color="white", text="\u2684 = " + str(res_array[4])).pack(padx= 15,side='left')
    root.CTkLabel(master=user_frame, fg_color="white", text="\u2685" + str(res_array[5])).pack(padx= 15,side='left')
    load_user_frame()



#
#roll_btn.bind('<Return>', command=roll)
# attempt at using enter key
roll_btn.pack(side='top')
button_quit = root.CTkButton(master=user_frame, text="Exit", command=app.quit)  # set up quit button
button_quit.pack(side='top')

#create var for Menu
my_menu= Tk.Menu(app)
# Create a category item  menu
file_menu = Tk.Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="File", menu=file_menu)
edit_menu = Tk.Menu(my_menu, tearoff=0)
my_menu.add_cascade(label="Edit", menu=edit_menu)

# Add sub-items to File_Menu
file_menu.add_separator()
file_menu.add_command(label="Exit", command=app.quit)
# Add sub-items to File_Menu
# edit_menu.add_separator()
# edit_menu.add_cascade(label="results")
# Add sub item to edit menu
edit_menu.add_checkbutton(label="show dice in order", command=lambda: show_roll_order(True))

app.config(menu=my_menu)
load_user_frame()
e.focus()


app.mainloop()
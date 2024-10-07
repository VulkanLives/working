
from tkinter import messagebox, Label, StringVar
import customtkinter as ctk
import roll_dice as rd
from PIL import ImageTk,Image
import tkinter as Tk

ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
root= ctk
#load image for background

app.title("TableTop Allie")
app.geometry("800x600", )  # set starting window size
app.resizable(width=False, height=True)



# Show image using label


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
dice_order_frame = root.CTkFrame(master=top_frame)
dice_order_frame.pack(side="right", fill="both", expand=True)

img_size = result_frame.grid_size()
print(img_size)
# Add image file
#bg_img_path = os.path
#'home/chris/PycharmProjects/TTA/scene2.png'))
bg_img = root.CTkImage(Image.open("app_images/backgrounds/scene2.png"), size=(300, 300))
bg_img_label = ctk.CTkLabel(master=result_frame, image=bg_img)
bg_img_label.pack(fill = 'both', expand = 1)
#user_frame_image = Label(image=rf_image).pack


frame3 = root.CTkFrame(master=bottom_frame, fg_color="orange", border_width=2, border_color="black")

e = root.CTkEntry(master=user_frame, border_width=1)
e.pack(side='top')



def roll(event=None):
    global result_array
    try:
        x = int(e.get())
        rd.RollDice(x)
        result_array = rd.occurance_list
        sequence_array = rd.roll_order
        pass
    except ValueError:
        messagebox.showwarning("Invalid Entry", "Numbers only please")  # first text is title of new window
        e.delete(0, 'end')  # clear entry box
        e.focus()  # make cursor active in entry box
    display_result(result_array)

def display_result(res_array):

    root.CTkLabel(master=user_frame, fg_color="white", width=1, text='\u2680' + str(res_array[0])).pack(padx= 15,side='left')
    root.CTkLabel(master=user_frame, fg_color="white", text='\u2681' + str(res_array[1])).pack(padx= 15,side='left')
    root.CTkLabel(master=user_frame, fg_color="white", text="\u2682 = " + str(res_array[2])).pack(padx= 15,side='left')
    root.CTkLabel(master=user_frame, fg_color="white", text="\u2683 = " + str(res_array[3])).pack(padx= 15,side='left')
    root.CTkLabel(master=user_frame, fg_color="white", text="\u2684 = " + str(res_array[4])).pack(padx= 15,side='left')
    root.CTkLabel(master=user_frame, fg_color="white", text="\u2685" + str(res_array[5])).pack(padx= 15,side='left')

def dice_results_in_order():
    global result_list
    dice_order_frame.grid(row=15, column=4)

roll_btn = root.CTkButton(master=user_frame, text="Roll Dice",
                          command=roll)  # "command" makes the calls the above function, fg is text colour "foreground" and Bg = background

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
edit_menu.add_command(label="results")
# Add sub item to edit menu
edit_menu.add_checkbutton(label="show dice in order", command=lambda: show_roll_order(True))

app.config(menu=my_menu)

e.focus()


app.mainloop()
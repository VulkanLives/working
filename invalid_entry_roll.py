import random
from tkinter import *
from tkinter import messagebox


root = Tk()

root.title("Welcome to the dice roller")
root.geometry("400x800") # set starting window size
#root.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon


# WOULD WORK WITH TK PIL frame = LabelFrame(root, text= "Enter number of dice", padx=50,pady=50, anchor= "CENTER") #only here to show what it affects
frame = LabelFrame(root, text= "      Enter number of dice",pady=20) #only here to show what it affects
frame.grid(row=1, column= 1,columnspan=3, padx=10)
roll_score_iteration_frame = LabelFrame(root,text="How many of each dice") #init 2nd frame but no need to display
dice_order_frame = LabelFrame(root,text="Order of the rolls")
e = Entry(frame, width = 10)
e.grid()
e.focus() #starts window with cursor in entry box
occurance_list = [0,0,0,0,0,0]  # array for how many of each dice
result_list = [] # initialise empty array

def popupWarn(error):
    messagebox.showwarning("Invalid Entry", "Numbers only please") #first text is title of new window
    e.delete(0, 'end') # clear entry box
    e.focus() #make cursor active in entry box
def roll_prep():
#creating instances of buttons and label and canvas etc
    result_list.clear() # clear array for next set of results as on repeating it was adding the user entry to the end of the
                        # of the previous results, so if they rolled 5 dice twice the results would should
                        # a result of 5 first then of 10 next, would better to use numpy
    try:
     int(e.get())
     amount_of_dice = int(e.get()) #convert user string into int
     print("amount of dice var= "+str(amount_of_dice))
     rollDice(amount_of_dice)
    except ValueError:
     popupWarn(e.get())


def rollDice(number):

  global occurance_list
  x  = result_list.__sizeof__()
  totalSum = 0
  possibleFaces = [1,2,3,4,5,6] # set possible dice results
  occurance_list = [0,0,0,0,0,0] #array to store how many of times a player scored each result
  #                                 # this would be btter using multi dimension version of the Possible Faces array
  #                                 # Maybe numPY

  for die in range(number):
   
   roll = random.choice(possibleFaces) #roll a dice
   result_list.append(roll) # add dice result to array

    # print the results on screen for each dice
   if int(roll) == 6:
     occurance_list[5]+=1
   elif int(roll) == 5:
     occurance_list[4]+=1
   elif int(roll) == 4:
     occurance_list[3]+=1
   elif int(roll) == 3:
    occurance_list[2]+=1
   elif int(roll) == 2:
    occurance_list[1]+=1
   else:
    occurance_list[0]+=1



   totalSum += roll
  average = totalSum / number
  print_array()
  dice_results_in_order()

  print("occurance list :" + str(occurance_list))





  print("Total sum: ", totalSum)
  print("Average roll: ", average)
  print(result_list)

def print_array():
  roll_score_iteration_frame.grid(row= 3,  column=2)
  Label(roll_score_iteration_frame, text="1s = " +str(occurance_list[0])).grid()
  Label(roll_score_iteration_frame, text="2s = " +str(occurance_list[1])).grid()
  Label(roll_score_iteration_frame, text="3s = " +str(occurance_list[2])).grid()
  Label(roll_score_iteration_frame, text="4s = " +str(occurance_list[3])).grid()
  Label(roll_score_iteration_frame, text="5s = " +str(occurance_list[4])).grid()
  Label(roll_score_iteration_frame, text="6s = " +str(occurance_list[5])).grid()
  Label(roll_score_iteration_frame, text="Array size= " +str(occurance_list.__len__())).grid()


def dice_results_in_order():
  global result_list
  dice_order_frame.grid(row= 3, column=1)

  for i in range(result_list.__len__()):
    Label(dice_order_frame, text = "Die "+ str(i + 1) + " result: " +str(result_list[i-1])).pack()

def clear_results_in_order():
    global roll_score_iteration_frame
    global dice_order_frame

    #removes the existing frames and then create same ones again
    roll_score_iteration_frame.destroy()
    dice_order_frame.destroy()

    roll_score_iteration_frame = LabelFrame(root, text="How many of each dice")  # init 2nd frame but no need to display
    dice_order_frame = LabelFrame(root, text="Order of the rolls")




roll_btn = Button(frame, text= "Roll Dice", command=roll_prep) #"command" makes the calls the above function, fg is text colour "foreground" and Bg = background
clear_btn = Button(frame, text= "clear", command=clear_results_in_order)
button_quit = Button(frame, text="Exit", command= root.quit) #set up quit button
button_quit.grid(row= 3, column =1)

clear_btn.grid()
roll_btn.grid()
root.mainloop()
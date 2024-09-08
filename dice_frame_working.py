import random
from tkinter import *

root = Tk()

root.title("Welcome to the dice roller")
root.geometry("400x650") # set starting window size
#root.iconbitmap("images/Treetog.ico") #uses an .ico file for little window Icon


# WOULD WORK WITH TK PIL frame = LabelFrame(root, text= "Enter number of dice", padx=50,pady=50, anchor= "CENTER") #only here to show what it affects
frame = LabelFrame(root, text= "      Enter number of dice", padx=50,pady=50) #only here to show what it affects
frame.pack(padx=100 ,pady=100)
e = Entry(frame, width = 10)
e.pack()
e.focus()


def button_click2():
#creating instances of buttons and label and canvas etc
    user_input = e.get() #get user input,will be as string
    amount_of_dice = int(user_input) #convert user string into int
    rollDice(amount_of_dice) #call roll function and pass it number entered by user

def rollDice(number):
  totalSum = 0
  possibleFaces = [1,2,3,4,5,6] # set possible dice results
  result_list = [] # initialise empty array
  occurance_list = [0,0,0,0,0,0] #array to store how many of times a player scored each result
                                  # this would be btter using multi dimension version of the Possible Faces array
                                  # Maybe numPY

  for die in range(number):
    roll = random.choice(possibleFaces) #roll a dice
    result_list.append(roll) # add dice result to array
    #Label(frame, text= "Die " + str(die+1) + " result: " + str(roll)).pack(anchor= W) #print the results on screen for each dice
    Label(frame, text="Die " + str(die + 1) + " result: " + str(roll)).pack()  # print the results on screen for each dice
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
  print("occurance list :" + str(occurance_list))





  print("Total sum: ", totalSum)
  print("Average roll: ", average)
  print(result_list)



#displaying a random button, but instead of using "root"
# #we are using "frame" to make it actually go in frame specifically
button2 = Button(frame, text= "Roll Dice", command=button_click2) #"command" makes the calls the above function, fg is text colour "foreground" and Bg = background


#thing to not here, you can't use grid and pack when dealing with root
#but you can if use both if referring differnt bit, in this case we are reffering to labelFrame
#not root
#button2.grid(row = 0, column= 0)

button2.pack()

root.mainloop()

#

#

#
#
#

#
# button2 =
# # print the items from the above into window
# button2.pack()
#
#
#


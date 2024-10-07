import random

roll_order = []
occurance_list = [0, 0, 0, 0, 0, 0]

class RollDice:



    def __init__(self,number):
        self.occurance_list = occurance_list
        self.roll_order = roll_order
        x=int(number)
        for die in range(x):
           roll = random.randint(1,6)  # roll a dice
           roll_order.append(roll)  # add dice result to array

           # print the results on screen for each dice
           if int(roll) == 6:
               occurance_list[5] += 1
           elif int(roll) == 5:
               occurance_list[4] += 1
           elif int(roll) == 4:
               occurance_list[3] += 1
           elif int(roll) == 3:
               occurance_list[2] += 1
           elif int(roll) == 2:
               occurance_list[1] += 1
           else:
               occurance_list[0] += 1
        print("occurance_list = " +str(occurance_list))
        print("roll order = " + str(roll_order))
        print("no of dice rolled = " + str(x))
        return
RollDice(6)
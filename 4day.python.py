import random
#import aaaa
#float_random = random.randint(0,5) # random. randint function give a chance to choose integer randomly
#print(float_random)
#print(aaaa.name)# we can transfer data from another file by "import smth"
#random_float = random.random() * 5
#print(random_float) ==> random.random() function use for to choose float number [o,1) 1 dont inside


# Heads or tails game coding
#choise = random.randint(0,1)
#if choise == 1:
#    print("Heads")
#else:
#    print("Tails")

# Who start the card game coding 

#print("Welcome to program that choose who strat card game ")
#name = input(" Enter all names, seperated by comma ")
#list_names = name.split(",")# split() method use to extract smth from the string variable and give output into list
#len_name= len(list_names)
#randing =random.randint(0, len_name-1)
#who =list_names[randing]
#print( who + " start the game ")


#who =random.choice(list_names)# random.choice function use to choose string from list randomly
#print(who)

 #List data type cointain any data types
#any_list = ["kamron",777, True, 1.11]
#print(any_list[2])
#name = ["kamron", "sabrina"]
#name.append("afruza")# apeend() use to add new item inside the list
#print(name)

#name[1]= "friend"# exchange item inside the list
#print(name)




#Nested list
#cars= ["jeep"," malibu"," mers", "bmw"]
#bikes = ["ural", "flex", "gonchik"]
#transports=[cars,bikes]
# i need mers+ gonchik
#need = transports[0][2] +" , "+ transports[1][2]
#print("I need "+ need)


# treasure map
#print("welcome to treasure map")
#raw1 =[" ",  " ",  " "]
#raw2 =[" ",  " ",  " "]
#raw3 =[" ",  " ",  " "]

#map =[raw1,raw2,raw3]
#print(f"{raw1}\n{raw2}\n{raw3}")  
#position = input(" Where do you put your treasure? first digit for horizontal raw, second for vertical raw  ")
#horizantal = int(position[0])
#vertical = int(position[1])
#map[horizantal-1][vertical-1] = "x"
#print(f"{raw1}\n{raw2}\n{raw3}")







# roCK, paper, scissors game coding


#rock = '''
#    _______
#---'   ____)
#      (_____)
#      (_____)
#      (____)
#---.__(___)
#'''

#paper = '''
#    _______
#---'   ____)____
#          ______)
#          _______)
#         _______)
#---.__________)
#'''

#scissors = '''
#    _______
#---'   ____)____
#          ______)
#      __________)
#      (____)
#---.__(___)
#'''
#print(" Welcome to Rock , Paper, Scissor game")
#you = int(input(" Choose one of them: '0' for rock, '1' for paper, '2' for scissors "))
#if you == 0:
#   print(rock)
#elif you == 1:
#    print(paper)
#elif you ==2:
#    print(scissors)
#else:
#    print("Choose exit choice")

    
#compyuter = random.randint(0,2)
#if compyuter == 0:
#   print(rock)
#elif compyuter == 1:
#    print(paper)
#lif compyuter ==2:
#    print(scissors)
#else:
#    print("Choose exit choice")
#    
#if you == compyuter:
#    print(" Draw")
#elif you ==0 and compyuter ==2:
#    print("You win")
#elif you ==0 and compyuter ==1:
#    print("Computer win")
#elif you ==1 and compyuter==0:
#    print(" You win")
#elif you==1 and compyuter ==2:
#    print("Compyuter win")
#elif you ==2 and compyuter ==0:
#    print("Compyuter win")
#elif you ==2 and compyuter ==1:
#   print("You win")
#else:
#    print("Wrong input")
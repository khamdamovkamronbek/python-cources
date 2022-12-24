# 3-day lesson: conditions,code blocks , scopre, logical operators.

# If/ elif /else ==> conditional statements
 
#checking my phone number code
 
#my_number = "01043818844"
#num = input(" Enter phone number ? ")
#if num == my_number:
 #   print('You found my number')
#else:
#    print("it's wrong, try again!")   



# code that find the number odd or even 
#print(" welcome to program that find number odd or even ")
#num = int(input(" Enter the any number? "))
#if num % 2 ==1:
#    print('this is odd number')
#else:
#    print("this is even number")
        
        
        
 # Body mass index calculator with their currently weight conditions
 
#print("Welcome to my BMI calculator.")
#weight = float(input("Enter your weight in kg "))  
#height = float(input(" enter your height in metr"))
#bmi =  round(weight / height **2 ,2)
#print(f"your BMI is {bmi}")   
#if  bmi < 18.5:
#    print("You are under weight !!!")
#elif  bmi< 25:
#      print("You are normal weight!")
#elif bmi <30:
#        print('You are overweight')
#elif bmi <35: 
#        print("You are obese")
#else:
#    print('You are clinically obese') 
                
                
                
                
                
# the code of find  leap year " Kabisa yili"
#print("welcome to finding leap year program")
#year = int(input("enter the year "))
#if year %4 ==0:
#   if year % 100==0:
#      if year%400 ==0:
#        print("its leap year")
#    else:
#       print("its not leap year")   
# else:
#    print("its leap year")   
#else:
#    print("its not leap year")



# code of Pizza delivery
#print("Welcome to my KEVIN pizza delivery")
#bill = 0
#print("Menu:\nsmall pizza==> $8,\n medium pizza ==> $12,\n large pizza==> $15")
#size =input("What size pizza do you want? small, medium or large .")
#print("Menu:\n cola==> $3,\n fanta==> $2")
#drinks = input("do you want to drink smth ? cola, fanta or not: ")
#print("menu:\n small free == $4\n large free==> $5")
#free =input("Do you want to free ? large or small size.")
#if size == "small":
 # bill = 8
 # print("small pizza cost is $ 8")
 
#if size =="medium":
## print("cost of medium pizza is $ 12")
 
#if size =="large":
 # bill= 15
 # print("cost of large pizza is $ 15")           
 
#if drinks == "cola":
#  bill+=3
#if drinks == "fanta":
#  bill+= 2
  
#if free == "large":
#  bill+= 5
#if free == "small":
#  bill+= 4        
#print(f"Total bill is ${bill}")        

# code of love calculator

#print ("Welcome to Love calculator")
#name1= input("Enter your name\n")
#name2 =input(" Enter your darling name\n")
#lower_case1= name1.lower()
#lower_case2 = name2.lower()
#T =lower_case1.count("t")
#t =lower_case2.count("t")
#t1 = T+t
#R= lower_case1.count("r")
#r= lower_case2.count("r")
#r1 = R+r
#U = lower_case1.count("u")
#u =lower_case2.count("u")
#u1=U+u
#E =lower_case1.count("e")
#e = lower_case2.count("e")
#e1= E+e
#true = t1 +r1 +u1+ e1
#print(f" 'T' occurs {T+t} times")
#print(f" 'R' occurs{R+r} times ")
#print(f" 'U' occurs {U+u} times")
#print(f" 'E' occurs {E+e} times")

#print(f"Total score is {true}")


#L=lower_case1.count("l")
#l=lower_case2.count("l")
#l1 =L+l
#O = lower_case1.count("o")
#o= lower_case2.count("o")
#o1 =O+o 
#V= lower_case1.count("v")
#v= lower_case2.count("v")
#1 =V+v  
#E= lower_case1.count("e")
#e =lower_case2.count("e")
#e1 = E+e 
#print(f" 'L' occurs {l1} times")
#print(f" 'O' occurs {o1} times")
#print(f" 'V' occurs {v1} times")
#print(f" 'E' occurs {e1} times")
#love = l1 + o1+ v1 +e1
#print(f"Total score is {love}")
#love_score1 = int(str(true) + str(love))
#print(love_score1)
#ove_score = str(true) +str(love)

#if love_score1 <= 10 or love_score1 >= 50:
#    print(f" Your score is{love_score}, you go together like a coke and mentos")
#elif love_score1> 40 and love_score1 <50:
#    print(f"Your score is {love_score}, you are alright together ")    
#else:
#    print("Your LOVE SCORE is  " + love_score + "%")





# the code of finding treasure 
 
#print(" Welcome to Kevin Treasure Island\n You are mission to find treasure.") 
#side =input(' You are at the cross road.What side do you like to go? Type \"left" or "right" ').lower()
#if side == "left":
#   print("You come to lake. There is a island in the middle of Lake. ")
#   lake = input("Type 'wait' to wait for boat or type 'swim' ").lower()
#    if lake == "wait":
#        door= input(" you arived Kevin Island.There is house with 3 doors. Yellow , blue and red. which door do you choose? ")
#        if door == "blue":
#           print("You find the treasure. You are now rich")
#       else:
#           print(" you choose wrong door. Game over ")
#    else:
#       print(" You are already sinked. Game over")    
#    
#else:
#    print(" You are wrong way, you lose the game ")





























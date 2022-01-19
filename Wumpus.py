# BY ARNAV PATHAK
# imported the modules
from ast import Interactive
import wikipedia
import time 


#The Choice Maker
print("||||||||The WUMPUS||||||||")
print("1 : Wikipedia Something")
time.sleep(0.5)
print("2 : Calculator")
time.sleep(0.5)
print("3 : Subscribe the Creator")
time.sleep(0.5)
print("4 : Release Notes.")
time.sleep(0.5)
print("5 : The Special Feature..Shh.")
time.sleep(0.5)
print("6 : Your Feedback = Our Support.")



choice = int(input("Enter your choice here: "))




#Wikipedia
if choice == 1:
    search = input("Enter the search to wikipedia: ")
    print(wikipedia.summary(search, sentences=4))




#Calculator
if choice == 2:
    print("Welcome to the Maths World")
    print("1: Addition")
    time.sleep(0.5)
    print("2 : Subtraction")
    time.sleep(0.5)
    print("3 : Multiplication")
    time.sleep(0.5)
    print("4: Division")

    time.sleep(0.7)

    choicem = int(input("Enter your choice here: "))
    
    if choicem == 1:                                                                                                #Addition
        a = int(input("Enter your Number 1 here: "))
        b = int(input("Enter your Number 2 here: "))
        c = print("The sum of numbers are:",a+b)

    if choicem == 2:                                                                                                #Subtraction
        print("#NOTE : FIRST NUMBER IS TO BE BIGGER THAN 2ND OR ELSE RESULT WILL BE IN NEGATIVE NUMBERS")
        d = int(input("Enter your Number 1 here: "))
        e = int(input("Enter your Number 2 here: "))
        f = print("The differnce of numbers are:",d-e)

    if choicem == 3:                                                                                                #Multiplication
        g = int(input("Enter your Number 1 here: "))
        h = int(input("Enter your Number 2 here: "))
        i = print("The product of numbers are:",g*h)


    if choicem == 2:                                                                                                 #Divison
        print("#NOTE : FIRST NUMBER IS TO BE BIGGER THAN 2ND OR ELSE RESULT WILL BE IN UNDESIRED RESULT")
        j = int(input("Enter your Number 1 here: "))
        k = int(input("Enter your Number 2 here: "))
        l= print("The quotient of numbers are:",j/k)

    else:
        print("Enter a valid option")
    

    




#My Channel
if choice == 3:
    print("This Program has beeen created by Arnav Pathak © Variety ")
    time.sleep(0.5)
    print("My channel : https://www.youtube.com/channel/UCOzP7pE267-vnP2rvUQbo9A")
    time.sleep(0.5)
    print("Subscribe me Guys..")



#Release Notes.
if choice == 4:
    print("This is version 1.0. Updates will further be given.")
    time.sleep(0.5)
    print("Name of AI: Wumpus.")
    time.sleep(0.5)
    print("Version 1.O. ")



#Special Feature.

if choice == 5:
    print("We are currently working on this feature and ITS AN EASTER EGG. :)")          
    time.sleep(0.5)



#Feedback

if choice == 6:
    Suggest = int(input("Please give your feedback. Rate between 1 and 10."))
    print("Thank you for using our AI. WE will improve it and make it more stable and effecient.")



else:
    print("Enter a valid option")
    
    
# BY ARNAV PATHAK
# BY ARNAV PATHAK
# BY ARNAV PATHAK
    
    

    













    




    

    
    





    




     
    
    


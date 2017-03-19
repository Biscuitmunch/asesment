import math
#start

#ask the user for their name
name = input("What is your name?")

#will be used to hang the opening welcome if the the program has run once
used = False

#function for calcularing volume
def volume ():
    radius = float(input("What is the radius of the base?"))
    hight = float(input("What is the high to the cone?"))
    answer = 1/3*3.14*radius**2*hight
    print(name, "the volume is", answer)

#function for calculations surface area
def area ():
    radius = float(input("What is the radius of the base?"))
    hight = float(input("What is the high to the cone?"))
    answer = 3.14*radius*math.sqrt(radius**2+hight**2)
    print(name, "the surface area is", answer)

#this is the while loop that is going to contain the main body of the program
while True:

    #the try is hear to stop the code from breacking
    try:
        if used == True :

            #this is the menu mesage if the program has ran at leat once already
            print("Want to do anouther calculation", name, "? For volume of a cone enter 1, \n for surface area of a cone 2, to exit enter 0.")
            
            menu = input("")

        else:

            #this is te menu mesage if the program has not run yet
            print("wlcome to the cone calculator", name, " For volume of a cone enter 1, \n for surface area of a cone 2, to exit enter 0")
            menu = input("")

        #now the program takes the user input and decides what option the user chose

        if menu == "1":

            #uses the area calculation function and tells the progam its been used once
            volume()
            used = True

        elif menu == "2":

            #uses the area function and tells the progam its ben used
            area()
            used = True

        elif menu == "0":

            #says goodbye and breaks the loop
            print("Have a good day", name)
            break

        else:

            #tells the user input is invald
            print("You did not enter valid input")
            
    #alows the program to continue to run even if invalid input is given 
    except (ValueError):
        print("invalid input")
        
        

    

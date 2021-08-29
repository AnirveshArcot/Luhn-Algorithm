from functionslist import *
clear()
choice=int(input("What would you like to do :\n 1.Check if a number follows the Luhn Algorithm (Enter 1 to choose this option )\n 2.Generate random numbers that follow the Luhn Algorithm (Enter 2 for this option)\n "))
if choice == 1 :
    clear()
    q1=input("Would you like to check if your number is valid (y/n) : ")
    if q1 == 'y':
      card = input("Enter your card no : ")
      f = open("NumLogs.txt", "a") 
      if(luhn_algorithm(card)):                 #The boolean value is returned here where its directly integrated with the if staement without the use of a variable 
          print("The number '"+card+"' is valid!")
          f.write(card+"  1\n")
      else:
          print("The number '"+card+"' is NOT valid!")
          f.write(card+"  0\n")
    elif q1=='n':
       print("Okay then,keep your secrets.")
    else:
       print("Are you blind? It said y OR n -_- ")

    os.system('pause')
    clear()
    f.close()

elif choice == 2 :
    clear()
    numofnumbers=int(input("How many numbers do you want?\n"))
    repeat=0
    lowerlmt=int(input("Enter how long your number must be (WARNING : it cannot be a 1 digit number) : \n"))
    upperlmt=lowerlmt+1
    lowerlmt2=pow(10 , lowerlmt-1) 
    upperlmt2=pow(10, upperlmt-1)
    if lowerlmt<2:
        clear()
        print("Are you blind?")
        os.system('pause')
        clear()
        exit()
    while (repeat<numofnumbers) :
        card=random.randint(lowerlmt2,upperlmt2)
        if (luhn_algorithm(str(card))):
            print(card_format(card))
            repeat=repeat+1
            print("")    
    os.system('pause')
    clear()

else:
    print("Are you blind ?? It said 1 or 2")
    os.system('pause')
    clear()

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
    name=platform.system()
    clear()
    r=int(input("How many numbers do you want?\n"))
    q=0
    x=int(input("Enter how long your number must be : \n"))
    y=x+1
    x2=pow(10 , x-1) 
    y2=pow(10, y-1)
    while (q<r) :
        card=random.randint(x2,y2)
        if (luhn_algorithm(str(card))):
            print(card_format(card))
            q=q+1
            print("")    
    os.system('pause')
    clear()

else:
    print("Are you blind ?? It said 1 or 2")
    os.system('pause')
    clear()

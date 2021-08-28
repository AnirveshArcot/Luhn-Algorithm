import os 
import sys
import platform
import random


def clear():
    name=platform.system()
    #for windows
    if name == 'Windows':
        _ = os.system('cls')
  
    #for Mac and Linux OS
    else:
        _ = os.system('clear')

def luhn_algorithm(card):                       #Function to calculate if it wasn't obvious
    cardno=list(card.replace(" ",""))           #Removing spaces from the input 
    cardno.reverse()                            #Reversing number because certain cards follow the reverse
    check_list = []
    for index , digit in enumerate(cardno):     
        if index % 2 != 0:
            doubledd=int(digit)*2
            if doubledd > 9:
                doubledd -= 9           
            check_list.append(doubledd)
        else:
          check_list.append(int(digit)*1)      
    if sum(check_list)%10 == 0:
        return True                            #The function doesn't return a variable just a boolean value directly 
    else:
       return False

def convertlist(list1):  #convert list into a string
    str = ''
    for i in list1:
        str += i  
    return str 

def card_format(numb):   #Function to format card numbers into a credit card like fashion
    formlist = []
    listnum=list(str(numb))
    for index1 , digit1 in enumerate(listnum):
        if index1%4==0:
            formlist.append(" ")
            formlist.append(digit1)
        else:
            formlist.append(digit1)
    formlist.pop(0)
    cardstr=convertlist(formlist)
    return cardstr
#CAMERON WATTS#
#COMP PROG#
#1 11 18#

import time #for text delay -> time.sleep(x)#
def namenum(): #function that prints list of names, and numbers#
    names = ["Bob", "Billy", "Jeff", "Billybob", "Boberson"] #list of names#
    print ("|Names > " +str(names)+ "")
    time.sleep(2)
    names[1:1] = ["JarJar", "Binks"] #added names#
    numbers = [42, 69, 21, 36, 66] #numbers#
    both = (names + numbers) #both#
    print ("|New Names > " +str(names)+ "")
    time.sleep(2)
    print ("|Numbers > " +str(numbers)+ "")
    time.sleep(2)
    print ("|Both > " +str(both)+ "")
namenum() #runs function#

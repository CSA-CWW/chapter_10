import time
def listt():
    for something in range(3):
        mylist = ["Cameron", "Feburary", "10", "2003", "Kyle"]
        place = mylist[4]
        date = mylist[1]
        print (mylist)

        mylist.insert(5, "Valerie")
        print (mylist)
        
        print ("I was born in " +str(place)+ ".")
        print ("The month was " +str(date)+ ".")
        print ("")
        time.sleep(1)
listt()

#CAMERON WATTS#
#1 18 18#
#COMP PROG#

listt = ['bob','billy','billybob','boberson','boberton']

def name_add(listt):
    name = input("Input a name.")
    listt.append(name)
    n_name = input("Would you like to add another name?\n1. Yes\n2. No").lower()
    if n_name == "y" or "yes" in n_name:
        name_add(listt)
    return listt

final_list = name_add(listt)
print (final_list)

#CAMERON WATTS#
#COMP PROG#
#1 25 18#

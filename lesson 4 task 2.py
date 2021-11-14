my_list = [20, 30, 2, 3, 40, 100, 5, 4, 3, 2, 2, 2]
a = [my_list [i] for i in range (1, len(my_list)) if my_list[i] > my_list [i-1]]


print (a)

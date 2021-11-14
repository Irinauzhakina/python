my_list = [20, 30, 2, 3, 40, 100, 5, 4, 3, 2, 2, 2]
#a = [i for i in range (my_list) if (my_list.count(i))]
a = [i for i in my_list if (my_list.count(i))==1]

print (a)

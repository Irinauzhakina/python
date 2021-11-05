my_list = [ 100, 20, 20, 5, 1, 1, 1]
a = int (input ('vvedite reiting:'))
for index, elem in enumerate (my_list):

    if a > elem:
        my_list.insert(index, a)
        break
        print(my_list)

    print (my_list)

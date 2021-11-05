a = input ('vvedite predlozhenie')
b = a.split()
for num, word in enumerate (b):
    print ('#' + str(num) + '-' + str (word[:10]))

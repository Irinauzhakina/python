from functools import reduce

my_list = [i for i in range (100, 1002) if i % 2 ==0]
#def fun_1 (a, b) 
#    return  my_list (i)*my_list(i+1)

a = reduce (lambda a,b  : a*b, my_list)

print (a)

def fun_expo (n1, n2):
    if n2 > 0:
        print ('not correct, should be less then 0')
    if n1 < 0:
        print('not correct, should be more then 0')
    else:
        return n1 ** n2


print (fun_expo(1,-2))

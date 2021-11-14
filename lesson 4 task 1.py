
def fun_zp(chas, stavka, prem):
    zp = chas * stavka + prem
    return zp

a = int (input ("vvedite chasi"))
b = int (input ("vvedite stavku"))
c = int (input ("vvedite premiu"))


print (fun_zp(a,b,c))

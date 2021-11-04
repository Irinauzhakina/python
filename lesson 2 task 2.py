spisok = input ("vvedite spisok ")
l = spisok.split()
dlina = len(l)
n = 0
if dlina > 1
    l[n], l[n+1]=l[n+1],l[n]
    n=n+1

print (l)

#a = list(input ('vvedite spisok')).split()
#a[::2], a[1::2] = a[1::2], a[::2]
#print (a)

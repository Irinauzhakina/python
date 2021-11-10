def fun_maksfromtree (n1, n2, n3):
    a = n1+n2+n3
    b = min (n1, n2, n3)
    return a-b

print (fun_maksfromtree(1,2,4))

n1 = int (input ('n1'))
n2 = int (input ('n2'))
n3 = int (input ('n3'))
print (fun_maksfromtree (n1, n2, n3))

a = int (input ('vvedite viruchku'))
b = int (input ('vvedite izderzhki'))
c = (a-b)/a
if a - b > 0:
    print ('porabotaly s pribilju, rentabelnost viruchki:')
    print (c)
    d = int (input ('vvedite chislennost'))
    e = int ((a-b) / d)
    print ('viruchka na odnogo sotrudnika:')
    print (e)
    
else :
    print ('porabotali s ubitkom')

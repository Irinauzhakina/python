def fun_int(txt):
    word = txt[0].upper()+txt[1:].lower()
    return word
string = input ('vvedite slova')
for word in string.split(' '):
    print (f'{fun_int(word)}', end=' ')

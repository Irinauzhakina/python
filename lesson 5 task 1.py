with open('test.txt', 'w') as file:
    vst_str = input('text:\n')

    while vst_str:

        file.write (f'{vst_str}\n')
        vst_str = input('text\n')

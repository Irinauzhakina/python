numb = {'one' : "odin", 'two' : "dva", 'three': "tri", 'four': "chetire"}
with open ('num.txt', 'w') as file, open ('num2.txt', 'w')  as new_file:
    file_lines = file.readlines()
    for line in file_lines:
        data = line.split()
        numrus = nums.get (data[0])
        new_file.write (f'{line.replace(data[0], numrus)}')
        

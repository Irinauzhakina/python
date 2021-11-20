with open('test.txt', 'w') as file:

    file_lines = file.readlines()
    N = 0

    for num, line in enumerate(file_lines):
        N += 1
        S = len(line.split())

        print(f'kol {num + 1} _ {S} slov')
    print(f'{N} strok')

archive = open('test.txt', 'r')

i = 0;
matrix_allocate = []
matrix_max = []
vector_available = []

for line in archive:
    line = line.replace('\n', '')
    if line == ';':
        i += 1
        continue
    data = line.split(' ')
    if i == 0:
        matrix_allocate.append(data)
    elif i == 1:
        matrix_max.append(data)
    elif i == 2 and line != '':
        vector_available = data

archive.close()

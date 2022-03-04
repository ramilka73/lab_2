K = int(input('Введите К: '))
wordCount = 0
length = 0
line = ''
char = ' '
f = open('text.txt', 'r')
while char:
    char = f.read(1)
    if char != '.':
        if line == '' and (char == ' ' or char == '\n'):
            continue
        else:
            line += char
    else:
        tmp = []
        tmp = line.split()
        flag = 0
        if len(tmp) % 2 == 1:
            for i in tmp:
                if len(i) <= K:
                    flag = 1
            if flag == 0:
                line += '.'
                print(line)
        line = ''
        
f.close()

from random import randint
grid1 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
grid2 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
grid3 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
grid4 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
grid5 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
grid6 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
grid7 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
grid8 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
grid9 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
grid10 = ['*', '*', '*', '*', '*', '*', '*', '*', '*', '*']
print (grid1)
print (grid2)
print (grid3)
print (grid4)
print (grid5)
print (grid6)
print (grid7)
print (grid8)
print (grid9)
print (grid10)
print (" ")
for i in range(0, 1000):
    x = randint(1, 10)
    y = randint(0, 9)
    if (x == 1):
        if (grid1[y] == ' '):
            grid1[y] = '*'
        elif (grid1[y] == '*'):
            grid1[y] = ' '
    if (x == 2):
        if (grid2[y] == ' '):
            grid2[y] = '*'
        elif (grid2[y] == '*'):
            grid2[y] = ' '
    if (x == 3):
        if (grid3[y] == ' '):
            grid3[y] = '*'
        elif (grid3[y] == '*'):
            grid3[y] = ' '
    if (x == 4):
        if (grid4[y] == ' '):
            grid4[y] = '*'
        elif (grid4[y] == '*'):
            grid4[y] = ' '
    if (x == 5):
        if (grid5[y] == ' '):
            grid5[y] = '*'
        elif (grid5[y] == '*'):
            grid5[y] = ' '
    if (x == 6):
        if (grid6[y] == ' '):
            grid6[y] = '*'
        elif (grid6[y] == '*'):
            grid6[y] = ' '
    if (x == 7):
        if (grid7[y] == ' '):
            grid7[y] = '*'
        elif (grid7[y] == '*'):
            grid7[y] = ' '
    if (x == 8):
        if (grid8[y] == ' '):
            grid8[y] = '*'
        elif (grid8[y] == '*'):
            grid8[y] = ' '
    if (x == 9):
        if (grid9[y] == ' '):
            grid9[y] = '*'
        elif (grid9[y] == '*'):
            grid9[y] = ' '
    if (x == 10):
        if (grid10[y] == ' '):
            grid10[y] = '*'
        elif (grid10[y] == '*'):
            grid10[y] = ' '
    count = 0
    for j in range(0, 9):
        if (grid1[j]) == '*':
            count = count + 1
        if (grid2[j]) == '*':
            count = count + 1
        if (grid3[j]) == '*':
            count = count + 1
        if (grid4[j]) == '*':
            count = count + 1
        if (grid5[j]) == '*':
            count = count + 1
        if (grid6[j]) == '*':
            count = count + 1
        if (grid7[j]) == '*':
            count = count + 1
        if (grid8[j]) == '*':
            count = count + 1
        if (grid9[j]) == '*':
            count = count + 1
        if (grid10[j]) == '*':
            count = count + 1
    print (grid1)
    print (grid2)
    print (grid3)
    print (grid4)
    print (grid5)
    print (grid6)
    print (grid7)
    print (grid8)
    print (grid9)
    print (grid10)
    print (count)
    print ("  ")

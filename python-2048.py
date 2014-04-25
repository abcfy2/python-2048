#!/usr/bin/env python
# encoding: utf-8
"""
The minigame 2048 in python
"""
import random

def init():
    """
    initialize a 2048 matrix. return a matrix list
    """
    matrix = [ 0 for i in range(16) ]
    random_lst = random.sample( range(16), 2 ) # generate 2 different number
    matrix[random_lst[0]] = matrix[random_lst[1]] = 2
    return matrix

def move(matrix,direction):
    """
    moving the matrix. return a matrix list
    """
    mergedList = [] #initial the merged index
    if direction == 'u':
        for i in range(16):
            j = i
            while j - 4 >= 0 and j - 4 not in mergedList:
                if matrix[j-4] == 0:
                    matrix[j-4] = matrix[j]
                    matrix[j] = 0
                elif matrix[j-4] == matrix[j]:
                    matrix[j-4] *=2
                    matrix[j] = 0
                    mergedList.append(j-4)
                j -= 4
    elif direction == 'd':
        for i in range(15,-1,-1):
            j = i
            while j + 4 < 16 and j + 4 not in mergedList:
                if matrix[j+4] == 0:
                    matrix[j+4] = matrix[j]
                    matrix[j] = 0
                elif matrix[j+4] == matrix[j]:
                    matrix[j+4] *=2
                    matrix[j] = 0
                    mergedList.append(j+4)
                j += 4
    elif direction == 'l':
        for i in range(16):
            j = i
            while j % 4 != 0 and j - 1 not in mergedList:
                if matrix[j-1] == 0:
                    matrix[j-1] = matrix[j]
                    matrix[j] = 0
                elif matrix[j-1] == matrix[j]:
                    matrix[j-1] *=2
                    matrix[j] = 0
                    mergedList.append(j-1)
                j -= 1
    else:
        for i in range(15,-1,-1):
            j = i
            while j % 4 != 3 and j + 1 not in mergedList:
                if matrix[j+1] == 0:
                    matrix[j+1] = matrix[j]
                    matrix[j] = 0
                elif matrix[j+1] == matrix[j]:
                    matrix[j+1] *=2
                    matrix[j] = 0
                    mergedList.append(j+1)
                j += 1
    return matrix

def insert(matrix):
    """insert one 2 or 4 into the matrix. return the matrix list
    """
    getZeroIndex = []
    for i in range(16):
        if matrix[i] == 0:
            getZeroIndex.append(i)
    randomZeroIndex = random.choice(getZeroIndex)
    matrix[randomZeroIndex] = 2
    return matrix

def output(matrix):
    """
    print the matrix. return the matrix list
    """
    max_num_width = len(str(max(matrix)))
    demarcation = ( '+' + '-'*(max_num_width+2) ) * 4 + '+' #generate demarcation line like '+---+---+---+'
    print demarcation
    for i in range(len(matrix)):
        if matrix[i] == 0:
            printchar = ' '
        else:
            printchar = str(matrix[i])
        print '|', 
        print '{0:>{1}}'.format(printchar,max_num_width),
        if (i + 1) % 4 == 0:
            print '|'
            print demarcation
    print

def isOver(matrix):
    """is game over? return bool
    """
    if 0 in matrix:
        return False
    else:
        for i in range(16):
            if i % 4 != 3:
                if matrix[i] == matrix[i+1]:
                    return False
            if i < 12:
                if matrix[i] == matrix [i+4]:
                    return False
    return True

def play():
    matrix = init()
    matrix_old = list(matrix)
    while True:
        output(matrix)
        if isOver(matrix) == False:
            if max(matrix) == 2048:
                input = raw_input('The max number is 2048, win the goal! q for quit, others for continue. ')
                if input == 'q':
                    exit()
            while True:
                input = raw_input("Choose which direction? u(p)/d(own)/l(eft)/r(ight), q for quit, b for back(Just one step): ")
                if input in [ 'u', 'd', 'l', 'r' ]:
                    matrix_old = list(matrix)
                    matrix_new = move(matrix,input)
                    break
                elif input == 'b':
                    matrix = list(matrix_old)
                    matrix_new = list(matrix)
                    break
                elif input == 'q':
                    print 'Byebye!'
                    exit()
                else:
                    print 'Input error! Try again.'
            matrix = list(matrix_new)
            if matrix == matrix_old:
                print 'Not chaged. Try another direction.'
            else:
                insert(matrix)
        else:
            print 'Cannot move anyway. Game Over...'
            exit()

if __name__ == '__main__':
    play()

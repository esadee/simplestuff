#decimal to binary converter
import os


def dec2bin(number):
    if number==0:
        return 0
    binary = ''
    while (number!=0):

        if (number%2==0):
            binary=('0'+binary)
        else:
            binary=('1'+binary)

        number = number // 2

    return binary



for x in range(100):
    print('Give the number (Decimal)')

    num = input()

    binary = ''
    number = int(num)

    print ('Decimal '+ str(number) +' is, binnary ' + str(dec2bin(number)) )








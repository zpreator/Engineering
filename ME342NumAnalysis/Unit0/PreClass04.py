def printFloatOrInt(x):
    if float(x).is_integer():
        print('The int using formatting is {0:d}'.format(int(x)))
        print('The int unformatted is ', int(x))
    else:
        print('The float using formatting is {0:5.3f}'.format(float(x)))
        print('The float unformatted is ', float(x))


def main():
    num = input('Enter a number: ')
    printFloatOrInt(num)

main()
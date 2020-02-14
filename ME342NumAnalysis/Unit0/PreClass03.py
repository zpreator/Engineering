def listIntegers(integers):
    index = 0    
    for num in integers:
        evenOrOdd = 'odd'
        if num%2 == 0:
            evenOrOdd = 'even'
        print('The index is {0:2d}, the number is {1:2d}, and it is'.format(index, num), evenOrOdd)
        index = index + 1

def main():
    integers = [2,3,5,6,7,8,3,4]
    listIntegers(integers)


main()
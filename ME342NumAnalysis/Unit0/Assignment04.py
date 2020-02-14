import math

def sqrtUpdate(S,xi):
    """ Returns a new estimated square root """
    return 0.5*(xi+S/xi)

def error(xi,x2):
    """ Returns the error of two values"""
    return abs((x2-xi)/x2)

def BablylonianMethod(S,x0, maxError):
    """ Iterates through the sqrtUpdate and error functions 
    to find a square root of parameter S and stops when maxError
    is reached """
    er = 1.0
    counter = 0
    while(er > maxError):
        xn = sqrtUpdate(S, x0)
        er = error(x0, xn)
        x0 = xn
        counter = counter + 1

    dictionary = {1:xn, 4:counter, 2:er}
    return dictionary

def getDictionaries(S, x0, maxError):
    """ Executes the babylonian method and calculates its error
    against math.sqrt and compiles the data into a dictionary"""
    dictionary = BablylonianMethod(S, x0, maxError)
    dictionary[0] = S
    dictionary[3] = error(math.sqrt(S), dictionary[1])
    return dictionary

def display(listOfDictionaries):
    """ Displays the S, Xn, Er, Ea, and n data when given a list of dictionaries"""
    #  index:   0         1         2          3          4
    print('||   S    ||   Xn   ||   Er    ||   Ea    ||   n    || ')
    for i in listOfDictionaries:
        print('------------------------------------------------------')
        print('||{0:8.4f}||{1:8.4f}||{2:8.3E}||{3:8.3E}||{4:8d}||'.format(i[0], i[1], i[2], i[3], i[4]))

def main():
    """ Main calls the getDictionaries with list comprehension
    to obtain and then display the list of dictionary values"""
    S = [2,3,4,7,12,16,25,36]
    listOfDictionaries = [getDictionaries(num, num/2,0.001) for num in S]
    display(listOfDictionaries)
    

main()
def secant(f, x0, x1, errorMax=1e-6, printIterations = False):
    """ Iterates through the secant method """
    e = errorMax + 1
    n = 0
    pakige = []
    while e > errorMax:
        xnew = x1 - (f(x1)*(x0-x1))/(f(x0)-f(x1))
        x0 = x1
        x1 = xnew
        e = abs((xnew-x0)/xnew)
        n += 1
        pakige.append([n, xnew, f(xnew), e])
        if printIterations:
            print('Iteration number: ', n)
            print('Estimated root: ', xnew)
            print('Evaluation at estimate', f(xnew))
            print('Relative error: ', e)
    return xnew

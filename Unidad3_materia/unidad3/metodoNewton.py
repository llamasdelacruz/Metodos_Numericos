import numpy as np

def F(x):

    f1 = x[0]**2+x[1]**2-1
    f2 = 4*x[0]**2/9+4*x[1]**2-1

    return np.array([f1,f2])

def DF(x):
    return np.array([[2*x[0], 2*x[1]],
                    [8*x[0]/9, 8*x[1]]])


N = 10000
x = np.array([-1,1])

for k in range(N):

    xold = x
    x = np.linalg.solve(DF(x), DF(x)@x-F(x))
    e = np.linalg.norm(x-xold)

    print(k, x, e)

    if(e<1e-10):
        break
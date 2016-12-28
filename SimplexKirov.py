import numpy as np
from scipy.optimize import linprog
import time
import matplotlib as plt

# maximize c^T*x
# A*x<=b
def solve_simplex(n, maxiter):
    start_time = time.clock()
    c = (np.array([10 ** (n - (j + 1)) for j in range(n)])) * -1
    A = np.zeros((n, n))
    for i in range(n):
        for j in range(i):
            A[i][j] = 2 * 10 ** (i - j)
        A[i][i] = 1
    b = np.array([100 ** i for i in range(n)])
    # print "c :",c*(-1),"\n A:", A,"\n b:", b
    res = linprog(c, A_ub=A, b_ub=b, options={"maxiter": maxiter})
    finish_time = time.clock()
    # print 'X = ',res.x, '\nfunction value =',res.fun*(-1), '\nnumber of iterations =',res.nit, '\nsuccess flag:',res.success
    return {
        "x": res.x,  # The solution of the optimization
        "fun": res.fun * (-1),  # Value of objective function
        "nit": res.nit,  # Number of algorithm iterations
        "success": res.success,  # If algorithm succeed (number of iterations doesn't exceed max number),
        "nfev": 0,  # Number of evaluations of the objective functions
        "time": round(1000 * (finish_time - start_time), 2)  # Runtime, ms
    }


def time_iter_plot(arr_time, arr_nit):
    plot(arr_nit, arr_time)
    xlabel('Iteration number')
    ylabel('Time, ms')


arr_time = []
arr_nit = []

for m in range(20):
    simplex = solve_simplex(m, maxiter=100000)
    arr_time.append(simplex.get('time'))
    arr_nit.append(simplex.get('nit'))
    time_iter_plot(arr_time, arr_nit)
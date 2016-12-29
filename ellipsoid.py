import numpy as np
import math as m
from klee_minty import KleeMintyCube


def subgr_norm(g, P):    # calculating subgradient normalizer
    g_t = np.transpose(g)
    prod_first = np.dot(g_t, P)
    prod = np.dot(prod_first, g)
    norm = 1/m.sqrt(prod)
    return norm


def ellipsoid(n, maxiter, A, b, c):
    P_init = n**2*np.identity(n)  # questionable, too stupid to find better alts atm
    x_init = n*[0]  # modifiable, need to fuck around with it
    k = 0
    x = x_init
    P = P_init
    kfin = 0
    while k < maxiter:
        feas_test = []  # template list for feasibility test
        for r in range(len(A)):
            if np.dot(A[r], x) <= b[r]:  # condition of point's feasibility, inefficient
                feas_test.append(True)
            else:
                feas_test.append(False)
        if feas_test == len(feas_test)*[True]:
            sgn = c*subgr_norm(c, P)  # subgrad, normalized
            fbest = np.dot(c, x)  # update the best solution
            alpha = (np.dot(c, x)-fbest)*subgr_norm(c, P)  # set the shift param
        else:
            uf = feas_test.index(False)  # the first violated constraint
            sgn = A[uf]*subgr_norm(c, P)  # subgrad, normalized
            alpha = np.dot(A[uf], x)*subgr_norm(A[uf], P)  # set the shift param
        x_new = x-(1+n*alpha)/(1+n)*np.dot(P, sgn)  # set the new x
        x = x_new  # update x for next runs
        pgmult = np.dot(np.dot(P, np.outer(sgn, sgn)), P)  # matrix mult for ellipse
        P = n**2/(n**2-1)*(1-alpha**2)*(P-2*(1+n*alpha)/((1+n)*(1+alpha))*pgmult)  # new ellipse shape
        k += 1
    return k,x

dim = 6
a = np.identity(dim)
b = np.array(dim*[2])
c = np.array(dim*[1])
ellipsoid(dim, 100, a, b, c)


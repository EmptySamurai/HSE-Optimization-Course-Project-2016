
class MinimizerMixin:

    def solve_klee_minty(self, n, maxiter = 1000):
        """
        :param n: number of varuable in Klee-Minty cube
        :param maxiter: max number of iterations
        :return: map same as scipy.optimize.OptimizeResult
        """

        return {
            "x": [0,0,0], # The solution of the optimization
            "fun": 0, # Value of objective function
            "nit": 0, # Number of algorithm iterations
            "success": True, # If algorithm succeed (number of iterations doesn't exceed max number),
            "nfev": 0, # Number of evaluations of the objective functions
        }

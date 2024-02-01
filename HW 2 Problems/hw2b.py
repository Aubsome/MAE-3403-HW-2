#Chat.gpt was used as a resource to help create this code
import math
def Secant(fcn, x0, x1, maxiter=10, xtol=1e-5):
    """
    As given by the HW,
    Use the Secant Method to find the root of fcn(x) in the neighborhood of x0 and x1.

    Parameters:
    fcn (callable): Function for which the root is to be found.
    x0, x1 (float): Initial guesses for the root in the neighborhood.
    maxiter (int): Maximum number of iterations.
    xtol (float): Tolerance for convergence (exit if |xnewest - xprevious| < xtol).

    Returns:
    float: Final estimate of the root.
    """
    x_prev = x0
    """For the secant method we need two initial guesses to start the iteration.
    Here I am naming those two initial guesses as the previous x, (x_prev) and the current x, (x_curr)."""
    x_curr = x1
    """For the secant method we need two initial guesses to start the iteration.
        Here I am naming those two initial guesses as x_previous and x_current"""

    for _ in range(maxiter):
        """This starts a loop that iterates a maximum of 'maxiter' times"""
        x_new = x_curr - fcn(x_curr) * (x_curr - x_prev) / (fcn(x_curr) - fcn(x_prev))
        """This is just the calculation of the secant method"""

        # Check for convergence
        if abs(x_new - x_curr) < xtol:
            """Checks if the new x value minus the current x value is less than the tolerance.
            If this is true the secant method has converged and the solution is stable."""
            return x_new
        """If the above condition is met the funciton will end here and return the x_new value, because
        the convergence has been done."""

        # Update values for the next iteration
        x_prev = x_curr
        x_curr = x_new
        """If the convergence doesn't happen above the values will continue to be updated until
        Convergence happens or the maximum number of iterations is complete"""

    return x_curr  # Return the final estimate
"""This returns the value of the final estimate after all the iterations. It is the result of the secant method."""

def main():
    """This defines the main function."""
    # Equation 1: x - 3*cos(x) = 0
    fcn1 = lambda x: x - 3 * math.cos(x)
    """This defines a lambda function that represents the equation we were given in the HW
    f(x)=x-3*cos(x)=0"""
    root1 = Secant(fcn1, x0=1, x1=2, maxiter=5, xtol=1e-4)
    """This calls the secant function to operate under these parameters that we have given it."""
    print(f'Root for x - 3*cos(x) = 0: {root1:.6f}')
    """This prints the result for the first equation with the given parameters."""

    # Equation 2: cos(2*x)*x^3 = 0
    fcn2 = lambda x: math.cos(2 * x) * x ** 3
    """This defines a lambda function that represents the equation we were given in the HW
        f(x)=cos(2*x)*x^3=0"""
    root2 = Secant(fcn2, x0=1, x1=2, maxiter=15, xtol=1e-8)
    """This calls the secant function to operate under these parameters that we have given it."""
    print(f'Root for cos(2*x)*x^3 = 0: {root2:.6f}')
    """This prints the result for the first equation with the given parameters."""

    # Equation 3: cos(2*x)*x^3 = 0 (with fewer iterations)
    fcn3 = lambda x: math.cos(2 * x) * x ** 3
    """This defines a lambda function that represents the equation we were given in the HW
        f(x)=cos(2*x)*x^3"""
    root3 = Secant(fcn3, x0=1, x1=2, maxiter=3, xtol=1e-8)
    """This calls the secant function to operate under these parameters that we have given it."""
    print(f'Root for cos(2*x)*x^3 = 0: {root3:.6f}')
    """This prints the result for the first equation with the given parameters."""


if __name__ == "__main__":
    """This checks that the script is running as the main program."""
    main()
    """This calls the main function."""
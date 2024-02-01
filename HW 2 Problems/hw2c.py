#Chat.gpt was used as a resource to help create this code
def GaussSeidel(Aaug, x, Niter=15):
    """
    As given by the HW,
    Use the Gauss-Seidel method to estimate the solution to a set of linear equations Ax = b.

    Parameters:
    Aaug (list of lists): Augmented matrix [A | b] with N rows and N+1 columns.
    x (list): Initial guess vector.
    Niter (int): Number of iterations.

    Returns:
    list: Final solution vector.
    """
    N = len(x)
    """This calculates the number of elements in x and that calculation is called N now."""
    for _ in range(Niter):
        """Do the block of code under this 'niter' times"""
        for i in range(N):
            """Do the block of code under this 'N' times"""
            # Calculate the new value for x[i] using the Gauss-Seidel method
            sum_before = sum(Aaug[i][j] * x[j] for j in range(i))
            """This calculates the sum of the products of the unknowns for j<i.
            This is the sum of the terms with the known values from the previous iteration."""
            sum_after = sum(Aaug[i][j] * x[j] for j in range(i+1, N))
            """This calculates the sum of the products of the unknowns for j >=i+1.
            This is the sum of the terms with the updated values from the current iteration."""
            x[i] = (Aaug[i][-1] - sum_before - sum_after) / Aaug[i][i]
            """This updates i. It subtracts the known and updated values then divides by the x[i] term.
            Ultimately this, (and the last two lines of code), is just the calculation work for the gauss seidel formula."""
    return x
"""Returns the result for x"""

def main():
    """Defines your main function."""
    # First linear system
    Aaug1 = [[3, 1, -1, 2], [1, 4, 1, 12], [2, 1, 2, 10]]
    """This just states our first matrix."""
    x1 = [0.0, 0.0, 0.0]  # Initial guess
    result1 = GaussSeidel(Aaug1, x1)
    """This is running the result for the first matrix by calling the gaussSeidel function
    we made with the given parameters."""
    rounded_result1 = [round(element) for element in result1] #I hated the way the answer looked so I had it round to the nearest whole number.
    print(f'Solution for [3 1 -1, 1 4 1, 2 1 2] [x1, x2, x3] = [2, 12, 10]: {rounded_result1}')
    """Prints the result for the first function."""

    # Second linear system
    Aaug2 = [[1, -10, 2, 4], [3, 1, 4, 12], [9, 2, 3, 4], [-1, 2, 7, 3]]
    """This just states our second matrix."""
    x2 = [0.0, 0.0, 0.0, 0.0]  # Initial guess
    result2 = GaussSeidel(Aaug2, x2)
    """This is running the result for the second matrix by calling the gaussSeidel function
        we made with the given parameters."""
    rounded_result2 = [round(element) for element in result2] #I hated the way the answer looked so I had it round to the nearest whole number.
    print(f'Solution for [1 -10 2 4, 3 1 4 12, 9 2 3 4, -1 2 7 3][x1, x2, x3, x4]=[2, 12, 21, 37]: {rounded_result2}')
    """Prints the result for the second function."""

if __name__ == "__main__":
    """This checks that the script is running as the main program."""
    main()
    """This calls the main function."""

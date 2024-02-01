#Chat.gpt was used as a resource to help create this code
import math
"""This imports the math pycharm module"""

def Probability(PDF, args, c, GT=True):
    """This defines a function we are naming probability.
    It has four parameters:
    PDF which will be a callback function for the gaussian/normal probability density function,
    args which is a tuple containing mu and sigma,
    c is a floating point value (upper limit of integration),
    GT is a boolean indicating
    if we want the probability of x being greater than c (GT=True) or less than c (GT=False)"""

    mu, sigma = args
    """This states that the tuple args has two values.  One is mu the other is sigma."""
    '#Define lower integration limits'
    lower_limit = mu - 5 * sigma
    upper_limit = c

    '#calculate probability using Simpsons 1/3 rule'
    n = 1000  #number of intervals
    h = (upper_limit - lower_limit) / n  #width of each interval
    x_values = [lower_limit + i * h for i in range (n+1)]
    """Creates a list of x values at regular intervals for the integration later (spaced by the interval width)."""

    # Determine integration limits based on GT
    if GT:
        integration_range = range(n) if c <= lower_limit else range(n - 1, -1, -1)
    else:
        integration_range = range(n) if c >= lower_limit else range(n - 1, -1, -1)
    """This if statement sets up the integration range that's used for Simpson's 1/3 rule.
    It determines if we are calculating P(x>c) (GT=True) or P(x<c) (GT=False) and uses the
    correct range for integration."""
    # Apply Simpson's 1/3 rule
    result = h / 3 * sum(PDF((x_values[i], mu, sigma)) for i in integration_range)
    """This calculates the  simpsons equation."""
    return result

def gaussian_pdf(args):
    """This defines the function we are naming gaussian_pdf with the tuple args."""
    x, mu, sigma = args
    """This explains that the tuple has 3 variables x, mu, and sigma."""
    return (1 / (sigma * math.sqrt(2 * math.pi))) * math.exp(-0.5 * ((x - mu) / sigma) ** 2)
    """This returns the value of the gaussian probability density function."""
def main():
    """This defines the main function (this is what actually runs your program)."""
    #test cases
    prob1 = Probability(gaussian_pdf, (100, 12.5), 105, GT=False)
    """This is the first test case it calls the probability function we created with these specific parameters."""
    prob2 = Probability(gaussian_pdf, (100, 3), 100 + 2 * 3, GT=True)
    """This is the second test case it calls the probability functino and specifies the parameters."""

    '#Print results'
    print(f'P(x<105|N(100,12.5))={prob1:.2f}')
    """This prints our first result in the format required by the HW problem."""
    print(f'P(x>{100+2*3}|N(100,3))={prob2:.2f}')
    """This prints our first result in the format required by the HW problem."""

if __name__ == "__main__":
    """This checks that the script is running as the main program."""
    main()
    """This calls the main function."""
# COLLATZ.PY

# The Collatz conjecture is a famous unsolved problem in math that asks if the function
# ![](collatz.png)
# converges on 1 for all initial values of n.
# We're going to implement two functions that will allow us to test given values of n.

# (Source: https://en.wikipedia.org/wiki/Collatz_conjecture)

# Tip: Keep the difference between `/` and `//` in mind.
#Reference: <https://docs.python.org/3/glossary.html#term-floor-division>

def next_value(n):
    """
    If n is even, divide it by two.
    If n is odd, triple it and add one.

    Input:
        n(int)

    Output:
        Next number in the Collatz sequence.
    """
    # REPLACE THIS COMMENT WITH YOUR CODE


def stopping_time(n, max_iterations):
    """
    For a given starting number, determine how many iterations of `next_value`
    it takes to reach 1.

    For example, since next_value(2) == 1

    A single call to next_value, so stopping_time(2, 100) == 1

    But next_value(3) == 10,
        so we call next_value(10) which is 5
        so we call next_value(5) which is 16
        so we call next_value(16) which is 8
        so we call next_value(8) which is 4
        so we call next_value(4) which is 2
        so we call next_value(2) which is 1

    A total of 7 calls to next_value, so stopping_time(3, 100) == 7

    Since the Collatz conjecture is unproven, we don't know that this function
    will terminate. Therefore, the function should quit if it reaches
    max_iterations.

    Input:
        n(int): An initial value, guaranteed to be >= 1.
        max_iterations(int): A maximum number of iterations to try.

    Output:
        The number of iterations it took to reach 1.
        Will return max_iterations if 1 was not reached.
    """
    # REPLACE THIS COMMENT WITH YOUR CODE


# WRITE CODE HERE TO TEST THE CODE YOU WROTE (OR WILL WRITE) ABOVE:

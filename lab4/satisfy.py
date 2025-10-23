# Part 2 - `satisfy` & `satisfy_all`

# 2.1: Complete the function named `satisfy` that takes in two predicate functions (`func1` and `func2`) and a list of integers (`values`).

# The function should return a list of two-element tuples.
# The first component of the tuple should be the integer from `values` and the second is `True` if both predicate functions return `True`, otherwise `False`.

# Example:

# ```python
# >>> from functional.satisfy import satisfy
# >>> satisfy(lambda x: x > 10, lambda y: y < 100, [1, 20, 200])
# [(1, False), (20, True), (200, False)]

# >>> satisfy(lambda x: x > 10, lambda y: y < 100, [])
# []

# >>> satisfy(lambda x: x > 10, lambda y: y < 100, [2])
# [(2, False)]
# ```

def satisfy(func1, func2, values):
    pass







# 2.2: `satisfy_all` takes a list of predicates (`funcs`) and a list of integers (`values`).

# The function should return a list of two-element tuples.
# The first component being an integer from `values` and the second is a list of the return values from calling each predicate function with the integer.

# ```python
# >>> from functional.satisfy import satisfy_all
# >>> funcs = [lambda x: x > 10, lambda y: y < 100]

# >>> satisfy_all(funcs, [1, 20, 200])
# [(1, [False, True]), (20, [True, True]), (200, [True, False])]

# >>> satisfy_all(funcs, [])
# []

# >>> funcs = [lambda x: x > 10, lambda y: y < 100, lambda z: False]
# >>> satisfy_all(funcs, [1, 20, 200])
# [(1, [False, True, False]), (20, [True, True, False]), (200, [True, False, False])]
# ```


def satisfy_all(funcs, values):
    pass

from func2 import addition
def addition_range(start, end):
    """
    >>> for addition in addition_range(0, 5):
    ...    print addition(1)
    1
    2
    3
    4
    5

    >>> print addition_range(5, 0)
    []
    """
    return [addition(val) for val in range(start, end)]
if __name__ == "__main__":
    import doctest
    doctest.testmod()
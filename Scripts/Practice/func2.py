def addition(additional):
    """
    >>> add5 = addition(5)
    >>> add5(3)
    8

    >>> add2 = addition(-2)
    >>> add2(3)
    1
    """
    def inner(integer):
        return integer + additional
    return inner


addition = lambda additional: lambda integer: integer + additional

def summit(*args):
    """
    Returns sum of the args.

    >>> summit(1)
    1

    >>> summit(2, 2)
    4

    >>> summit(1, 2, (3, 4))
    10

    >>> summit(1, ([2,3],5))
    11

    >>> summit(-1, 1.0)
    0.0
    """
    summ = 0
    for x in args:
        if type(x) in (tuple, list):
            for i in x:
                summ+=summit(i)
        else:
            summ=summ+x
    return summ    	

if __name__ == "__main__":
    import doctest
    doctest.testmod()
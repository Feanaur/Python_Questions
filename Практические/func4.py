from collections import Iterable
from func3 import addition_range
from func2 import addition
from func1 import summit

def mymap(funcs, args):
    """
    >>> add0 = addition(0)
    >>> add1 = addition(1)
    >>> add2 = addition(2)
    >>> add5 = addition(5)
    >>> print mymap(add5, [1, 2, 3])
    [6, 7, 8]

    >>> print mymap([add0, add1, add2], [1, 2, 3])
    [(1, 2, 3), (2, 3, 4), (3, 4, 5)]

    >>> print mymap([], [])
    []

    >>> print mymap(summit, [(3, 4, 5, 6, (7,))])
    [25]
    """
    if isinstance(funcs, Iterable):
        return [tuple(f(arg) for arg in args)  for f in funcs]
    else:
        return [funcs(arg) for arg in args]

if __name__ == "__main__":
    import doctest
    doctest.testmod()
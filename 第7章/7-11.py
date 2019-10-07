def f(a, b, *args, **kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
f(1, 2, 3, 4, 5, x = 6, z = 7)
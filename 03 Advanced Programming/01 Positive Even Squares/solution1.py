def positive_even_squares(*args):
    positives = filter(lambda x: x > 0  and x %2 == 0 ,[j for i in list(args) for j in i ])
    squares = map(lambda x: x**2 ,positives)
    return list(squares)
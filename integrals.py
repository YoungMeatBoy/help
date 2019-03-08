#############################
#                           #
#      2019 IU7 BMSTU       # 
#                           #
#  All integrals which can  #
#    be asked on eaxams.    #
#                           #
#    Special thanks to:     # 
#      @maxim_kozlov        #
#                           #
# Written in Pascal style   #
#                           #
#############################

def threeEights(start, stop, splits, f):
    a = start
    b = stop
    m = splits
    h = (b - a) / (m)
    s = f(a) + f(b)

    for i in range(1, m):
        x = a + h * i
        if i % 3 == 0:
            s = s + 2 * f(x)
        else:
            s = s + 3 * f(x)
    s = 3 * s * h / 8
    return s


def leftRectangles(start, stop, f, splits):
    a = start
    b = stop
    n = splits
    h = (b - a) / n
    s = 0
    for i in range(n):
        x = a + h * i
        s += f(x)
    s *= h
    return s


def middleRectangles(start, stop, f, splits):
    a = start
    b = stop
    n = splits
    h = (b - a) / n
    s = 0
    for i in range(n):
        x = a + h * i + h / 2
        s += f(x)
    s *= h
    return s


def rightRectangles(start, stop, f, splits):
    a = start
    b = stop
    n = splits
    h = (b - a) / n
    s = 0
    for i in range(1, n + 1):
        x = a + h * i
        s += f(x)
    s *= h
    return s


def sympson(razb, a, b):
    h = (b - a) / razb
    s = 0
    x = a + h
    while x < b:
        s = s + 4 * f(x)
        x = x + h
        s = s + 2 * f(x)
        x = x + h
    Sympson = h / 3 * (s + f(a) - f(b))
    return Sympson


def trapezum(razb, func=f, a, b):
    h = (b - a) / (razb)
    result = 0.5 * (f(a) + f(b))
    for i in range(1, razb):
        result += f(a + i * h)
    result *= h
    return result

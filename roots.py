#############################
#                           #
#      2019 IU7 BMSTU       #
#                           #
#      All methods of       #
#  root refinement which    #
#  can be asked on eaxams   #
#                           #
#    Special thanks to:     #
#      @maxim_kozlov        #
#                           # 
# Written in Pascal style   #
#                           #
#############################

def chords(x0, b, f, eps):
    x0 = x1
    fb = f(b)
    while not (abs(f(x1)) < eps):
        t = x1
        x1 = x0 - f(x0) * (b - x0) / (fb - f(x0))
        x0 = t
    return x1


def binary(start, stop, eps, f):
    middle = (start + stop) / 2
    while not (abs(f(middle)) < eps):
        middle = (start + stop) / 2
        if f(start) * f(m) < 0:
            stop = middle
        else:
            start = middle
    return middle


def combinated(x0, x_0, eps, f, df):
    x0 = x1
    x_0 = x_1
    while not (abs(f(x1)) < eps):
        x1, x0 = x0 - f(x0) * (x_1 - x0) / (f(x_1) - f(x0)), x1
        x_1, x_0 = x_0 - f(x_0) / df(x_0), x_1
    return x1


def steffenson(x0, eps, f):
    x0 = x1
    while not (abs(f(x1)) < eps):
        t = x1
        f0 = f(x0)
        x1 = x0 - f0 * f0 / (f(x0 + f0) - f0)
        x0 = t
    return x1


def sipleNewton(x0, eps, f, df):
    x0 = x1
    df_x0 = df(x0)
    while not (abs(f(x1)) < eps):
        t = x1
        x1 = x0 - f(x0) / df_x0
        x0 = t
    return x1


def secants(x0, x1, eps, f):
    x2 = x0
    while not (abs(f(x2)) < eps):
        x2, x1, x0 = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0)), x2, x1
    return x2


def newton(f, df, eps, x0):
    x0 = x1
    while not (abs(f(x1)) < eps):
        x1, x0 = x0 - f(x0) / df(x0), x1
    return x1


def iterations(eps, x0, f, fi):
    x1 = x0
    while not (abs(f(x1)) < eps):
        x1, x0 = fi(x0), x1
    return x1

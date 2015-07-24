import sys
from math import sqrt


def plus_epsilon_identity(x, epsilon):
    return x + epsilon == x


def eps(x):
    e = float(max(sys.float_info.min, abs(x)))
    while not plus_epsilon_identity(x, e):
        last = e
        e = e / 2.
    return last


def finite_difference(f, x, h=None):
    if not h:
        h = sqrt(eps(1.0)) * max(abs(x), 1.0)
    return (f(x+h) - f(x)) / h


def error(f, df, x, h=None):
    return abs(finite_difference(f, x) - df(x))


def error_rate(f, df, x, h=None):
    return error(f, df, x) / abs(df(x))


def complex_step_finite_diff(f, x):
    h = sys.float_info.min
    return (f(x+h*1.j)).imag / h


def cerror(f, df, x):
    return abs(complex_step_finite_diff(f, x) - df(x).real)


def cerror_rate(f, df, x):
    return cerror(f, df, x) / abs(df(x))

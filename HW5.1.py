"""
Created on 7/30/20

@author: jordanshomefolder
"""
# just implement giveen code for bc - use euler to solve ode and output at t1
#     solve up to t1, then output
#     go back by h
#     r i given parameter - growth rate
# change for c - like trap rule, only thing that changes is going from t to t+h
#     building array, appending, while loop etc is same

# Euler's method (scalar ODE) example code
import numpy as np
import matplotlib.pyplot as plt


def pop(f, t0, t1, y0, h):
    y = y0
    yvals = [y]
    tvals = [t0]
    t = 0
    t += t0  # set current time
    while t < t1 - 1e-12:  # (avoids rounding error where t misses b slightly)
        if t0 >= t1:
            t += h
        if t0 < t1:
            t -= h
        x = t + h / 2
        f1 = f(t, y)
        f2 = f(x, y + f1 / 2)
        f3 = f(x, y + f2 / 2)
        f4 = f(t + h, h * f3)
        y = y + (h / 6) * (f1 + 2 * f2 + 2 * f3 + f4)
        yvals.append(y)
        tvals.append(t)

    return tvals, yvals


# hw 5: euler's method, revised example code


# ------------------------------------------------------
# Example code (edited from the lecture code)
# You can use fwd_euler as a starting point for rk4
# and euler_conv, euler_plot as a starting point for plots/errors

def fwd_euler(f, a, b, y0, h):
    """ Forward Euler with fixed step size using a while loop."""
    y = y0
    t = a
    yvals = [y]
    tvals = [t]
    while t < b - 1e-12:
        y += h * f(t, y)
        if a < b:
            t += h
        if a > b:
            t -= h
        yvals.append(y)
        tvals.append(t)

    return tvals, yvals


def efunc(t):
    """ example ODE function """
    return (1 + np.exp(-t)) ** (-1)


def pop_func(r, y):
    return r * y * (1 - y)


# -----------------------------------------------------------------
# example code [adapted from lecture] for euler's method for reference
def euler_plot():
    """ example: solve and plot solution with Euler's method """
    h = 0.5
    y0 = 0.5
    r = 1
    t0 = 0
    a = t0
    b = 1
    t1 = b

    s = np.linspace(0, 1, 200)
    exact = efunc(s)
    t, y = fwd_euler(pop_func, a, b, y0, h)
    r, k = pop(pop_func, t0, t1, y0, h)
    plt.figure(figsize=(3, 2.5))
    plt.plot(s, exact, '-k')  # plot exact
    plt.plot(t, y, '--.b', markersize=12, label='fwdeuler')
    plt.plot(r, k, '--.r', markersize=12, label='RK4')
    # plot approx.
    plt.xlabel('t')
    plt.ylabel('y')
    # plt.savefig('name.pdf', bbox_inches='tight')
    plt.show()


# def euler_conv():
#     """ calculate the error at t=b for various h's and plot """
#     m = 9
#     hvals = [(0.25)*2**(-k) for k in range(m)]
#     y0 = 1
#     b = 1
#
#     def exact(t):
#         return y0*np.exp(t**2)
#
#     err_endpoint = [0]*m
#     for k in range(m):
#         t, y = fwd_euler(efunc, 0, b, y0, hvals[k])
#         err_endpoint[k] = abs(y[-1] - exact(b))
#     plt.figure(figsize=(3, 2.5))
#     plt.loglog(hvals, err_endpoint, '.--k')
#
#     # also create a reference line (manually adjusting the coefficient)
#     r = [2*h for h in hvals]
#     plt.loglog(hvals, r, '--r', markersize=8)
#     plt.legend(['t=b err', 'slope 1'])
#     plt.xlabel('h')
#     plt.show()
print(euler_plot())

# Q2.2

import math


def f_x(x):
    return (x - math.tan(x))


def g_x(x):
    return (x ** 2) - (6 * x * math.sin(x)) +  (2*(math.sin(x))) ** 2


def bisection(func, a, b, max_iter, tol_x, tol_f):
    count = 0
    func_a = func(a)
    func_b = func(b)
    if ((func_a * func_b) > 0):
        return ("inconsistent initial values")
    delta = b - a
    for i in range(max_iter):
        count += 1
        delta = float(delta / 2)
        c = float(a) + delta
        func_c = func(c)

        if (abs(delta) < tol_x or abs(func_c) < tol_f):
            return ("(" + str((c)) + ")" + " within " + str(count) + " iterations")

        if (func_a * func_c < 0):
            b = c
            func_b = func_c
        else:
            a = c
            func_a = func_c
    return ("Too many iterations")

#I answerd here the Q2.3 :
#Number of iteration is 24 and the value is 4.667005472080987e-07
# Q2.3
print('\n' + "Q2.3")

print("Root of f(x)=x^2-6xsinx+(2sinx)^2 in (2,3) is approximately:- " + bisection(g_x, 2, 3, 30, 10 ** -7, 10 ** -7) +
      ".The value of f in that point is " +
      str(g_x(2.618001163005829)))

# Q2.4
print('\n' + "Q2.4")

print("Root Number 1 of f(x)=x-tan(x) is approximately:- " + bisection(f_x, -3, -4.5, 24, 10 ** -7, 10 ** -7))
print("Root Number 2 of f(x)=x-tan(x) is approximately:- " + bisection(f_x, -7.5, -7.8, 23, 10 ** -7, 10 ** -7))
print("Root Number 3 of f(x)=x-tan(x) is approximately:- " + bisection(f_x, 3, 4.5, 24, 10 ** -7, 10 ** -7))
print("Root Number 4 of f(x)=x-tan(x) is approximately:- " + bisection(f_x, 7.5, 7.8, 23, 10 ** -7, 10 ** -7))

# Q2.5
print('\n' + "Q2.5")


def newton(func, x, max_iter, tol_f):
    count = 0
    while (count != max_iter):
        deri_func = ((func(x + 10 ** -7) - func(x)) / 10 ** -7)
        x = x - (func(x) / deri_func)
        if (abs(func(x)) < tol_f or abs(func(x)) == tol_f):
            return ("(" + str(x) + ")" + " "+str(count))
        count += 1
    return ("Maximum number of iterations has been exceeded")


print("Example for newton method at f(x)=arctan(x): " + newton(math.atan, 0.5, 10, 10 ** -7))


# Q 2.6

def h_x(x):
    return (x ** 3 - x ** 2 - 2)


print('\n' + "Q2.6")

# A
print("Root of f(x)=x^3-x^2-2 in (1,2) by bisection is approximately:- " + bisection(h_x, 1, 2, 11, 10 ** -3, 10 ** -3))
# B
print("Root of f(x)=x^3-x^2-2 at initial value 1 by newton method is " + newton(h_x, 1, 100, 10 ** -10))
print("Root of f(x)=x^3-x^2-2 at initial value 2 by newton method is " + newton(h_x, 2, 100, 10 ** -10))
print("Root of f(x)=x^3-x^2-2 at initial value 0.5 by newton method is " + newton(h_x, 0.5, 100, 10 ** -10))
print("Root of f(x)=x^3-x^2-2 at initial value 1000 by newton method is " + newton(h_x, 1000, 100, 10 ** -10))
print("Root of f(x)=x^3-x^2-2 at initial value 500 by newton method is " + newton(h_x, 500, 100, 10 ** -10))


# Q2.7

def root_newton(n, x, r, max_iter, tol_r):
    count = 0
    while (count < max_iter):
        root = r ** n - x
        der_root = n * (r ** (n - 1))
        ans = r - (root / der_root)
        if (abs(r - ans) < tol_r):
            return ans
        r = ans
        count += 1


def root_func(n, x):
    return root_newton(n, x, 5, 50, 10 ** -10)


print('\n' + "Q2.7")
print("The third root of 5 is approximately: " + str(root_func(3, 5)))
print("The fifth root of 200 is approximately:" + str(root_func(5, 200)))

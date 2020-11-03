"""
Fermat’s Last Theorem says that there are no positive integers a, b, and c such that

a^n + b^n = c^n 

for any values of n greater than 2.

Write a function named check_fermat that takes four parameters — a, b, c and n — and
checks to see if Fermat’s theorem holds. If n is greater than 2 and a^n + b^n = c^n
the program should print, “Holy smokes, Fermat was wrong!” Otherwise the program
should print, “No, that doesn’t work.”

Write a function that prompts the user to input values for a, b, c and n, converts
them to integers, and uses check_fermat to check whether they violate Fermat’s theorem.
"""

def check_fermat(a, b, c, n):
    if n <= 2:
        print("Fermat's theorem is only relevant for values of n greater than 2.")
    elif (a ** n + b ** n) == c ** n:
        print('Holy smokes, Fermat was wrong!')
    else:
        print("No, that doesn't work.")

def user_test():
    print("Please provide four values to check Fermat's theorem: a, b, c, and n.")
    a = int(input('Enter a value for a: '))
    b = int(input('Enter a value for b: '))
    c = int(input('Enter a value for c: '))
    n = int(input('Enter a value for n: '))
    print()
    print('Testing to see if', str(a)+'^'+str(n), '+', str(b)+'^'+str(n), '=', str(c)+'^'+str(n), '...')
    check_fermat(a, b, c, n)

user_test()


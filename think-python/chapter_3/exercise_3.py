# Note: This exercise should be done using only the statements and other features we have
# learned so far.
#
# 1. Write a function that draws a grid like the following:
#   + - - - - + - - - - +
#   |         |         |
#   |         |         |
#   |         |         |
#   |         |         |
#   + - - - - + - - - - +
#   |         |         |
#   |         |         |
#   |         |         |
#   |         |         |
#   + - - - - + - - - - +
#
# 2. Write a function that draws a similar grid with four rows and four columns.

def do_twice(func):
    func()
    func()

def do_four(func):
    do_twice(func)
    do_twice(func)

def print_row_segment():
    print('- - - - +',end=' ')

def print_col_segment():
    print('        /',end=' ')

def print_row():
    print('+', end=' ')
    do_four(print_row_segment)
    print()

def print_cols():
    print('/', end=' ')
    do_four(print_col_segment)
    print()

def print_strip():
    print_row()
    do_four(print_cols)

do_four(print_strip)
print_row()
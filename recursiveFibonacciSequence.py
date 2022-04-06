"""
Author: Lani Hurley
Date: 3/28/22
Filename: recursiveFibonacciSequence.py
Python program demonstrates the Fibonacci sequence using a recursive function.
The term is calculated like this: X(n) = X(n-1) + X(n-2) * Fibonacci Sequence 'Rule'
Where x(n) is the term number "n"
      x(n-1) is the previous term (n-1)
      x(n-2) is the term before that (n-2)
"""


def r_fibo(n):
    if n <= 1:
        return n
    else:
        return r_fibo(n - 1) + r_fibo(n - 2)


# Replace the variable int number with the amount of terms desired
nTerms = 10  # ***Enter the amount of terms you want here!

# check if the number of terms is valid
if nTerms <= 0:
    print("Please enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(nTerms):
        print(r_fibo(i))

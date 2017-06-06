#fibonacci code for Swift Navigation
import sys

"""the fib_nth function returns the nth number in the fibonacci series
n is the argument supplied to the function"""
def fib_nth(n):
    if n == 1 or n == 2:
        return 1   
    return (fib_nth(n-1) + fib_nth(n-2))

"""the isPrime function checks if a number-supplied as argument- is prime
or not. 1 is not considered a prime"""
def isPrime(n):
    numDivisors = 1
    if n == 1:
        return False
    elif n == 2:
        return True
    for i in range(2,n,1):
        if n%i == 0:
            numDivisors += 1
    if numDivisors > 1:
        return False
    else:
        return True
    
N=input('Enter a number: ')
try:
    N = int(N)
except ValueError:
    print('Invalid Input')
    sys.exit()

if int(N) < 1:
    print('Invalid Input')
    
"""The following checks if a fibonacci number is divisible by 15, 3, 5
and if it's a prime number. Different strings are printed depending on
the case. If non of the conditions satisfy, the number is printed.
It must be noted that a number could satisfy more than one condition, in
which case as many strings are printed"""    
for i in range(1, N+1, 1):
    flag = True
    num = fib_nth(i)
    print()
    if num%3 == 0 and num%5 == 0:
        print ('FizzBuzz')
        flag = False
    if num%3 == 0:
        print ('Buzz')
        flag = False
    if num%5 == 0:
        print ('Fizz')
        flag = False
    if isPrime(num) == True:
        print ('BuzzFizz')
        flag = False
    if flag:
        print (num)
    
    


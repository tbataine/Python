"""
Write a Python program that prompts the user to enter a number,
 and then prints the number of prime numbers that exist up to the number that was entered.

The solution to this problem should be uploaded within a file prime_numbers.py
"""
def is_prime(n: int) -> bool:
    if n <= 1:
        return False
    if n <=3:
        return True
    if n%2 == 0 or n%3 == 0:
        return False
    x=5
    while x * x <=n:
        if n%x == 0 or n%(x+2) == 0:
            return False
        i +=6
    return True   


y= int(input("Please enter a number: "))
if is_prime(y):
    print(f"{y} is a prime number!")
else:
    print(f"{y} is not a prime number!")

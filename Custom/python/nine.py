# Armstrong number is a number that is equal to the sum of its own digits each raised to the power of the number of digits.
def is_armstrong(n):
    digits = [int(d) for d in str(n)]
    num_digits = len(digits)
    return sum(d ** num_digits for d in digits) == n


print(is_armstrong(153))  
print(is_armstrong(9474)) 
print(is_armstrong(123))  
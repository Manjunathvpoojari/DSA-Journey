# Perfect number

def is_perfect(n):
    if n < 2:
        return False
    divisor_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisor_sum == n

print(is_perfect(6))       
print(is_perfect(28))      
print(is_perfect(10))       
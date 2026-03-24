# GCD — Euclidean Algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# LCM — using GCD
def lcm(a, b):
    return (a * b) // gcd(a, b)
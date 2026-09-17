def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(35, 91))
print(gcd(91, 35))
print(gcd(13, 39))
# Armstrong number:
# The number, when we sum the digit exponential of its length, it will be equal to the number itself.
# Example:
# 153 = 1**3 + 5**3 + 3**3 = 153
# 1345 = 1**4 + 3**4 + 4**4 + 5**4 != 1345 (not armstrong number)


def is_armstrong(n):
    num = n
    exp = len(str(n))
    total = 0
    while num > 0:
        digit = num % 10
        total += digit ** exp
        num = num // 10
    return total == n



print(is_armstrong(153))
print(is_armstrong(1345))

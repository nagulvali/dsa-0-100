# Reverse a number
# Time complexity: O(log N)

def reverse_number(n):
    reversed_num = 0
    while n > 0:
        reversed_num = reversed_num * 10 + n % 10
        n = n // 10
    return reversed_num

print(reverse_number(12345678910))



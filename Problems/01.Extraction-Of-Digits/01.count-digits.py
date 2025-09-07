# count digits

# Method 1
# Time Complexity: O(Log N)
# Space Complexity: O(1)

def count_digits(num):
    count = 0
    while num > 0:
        count += 1
        num = num // 10
    return count

print(count_digits(12345678910))


# Method 2
# Time Complexity: O(1)
# Space Complexity: O(1)

import math

def count_digits_1(num):
    return int(math.log(num, 10) + 1)

print(count_digits_1(12345678910))
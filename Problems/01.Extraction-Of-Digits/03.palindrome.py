# Check palindrom number

def is_palindrome(n):
    reversed_num = 0
    num = n
    while num > 0:
        reversed_num = reversed_num*10 + num%10
        num = num//10

    # print(n)
    # print(reversed_num)

    return int(reversed_num) == int(n)


print(is_palindrome(12345678910))
print(is_palindrome(1221))
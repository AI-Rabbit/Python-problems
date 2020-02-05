# p37.py


def is_plalindrome(string):
    return string == ''.join(list(reversed(string)))


str1 = input()
if is_plalindrome(str1):
    print('Yes')
else:
    print('No')

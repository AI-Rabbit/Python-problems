# p43.py
str1 = input().split()
str1.reverse()


def exp():
    s = str1.pop()
    if s[0] == '+':
        return exp() + exp()
    elif s[0] == '-':
        return exp() - exp()
    elif s[0] == '*':
        return exp() * exp()
    elif s[0] == '/':
        return exp() / exp()
    else:
        return float(s)


print(int(exp()))

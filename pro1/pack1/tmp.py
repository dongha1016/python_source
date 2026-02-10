def mod(a, b):
    return a/b

try:
    c = mod(3, 2)
    print(c)
    c1 = mod(3, 0)
    print(c1)
except ZeroDivisionError as e:
    print("안되는 이유: ", e)
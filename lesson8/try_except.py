x = 0
try:
    y = 1 / x
except ZeroDivisionError:
    print("You can't divide by zero!")
    y = 0
print(y)

x = "hello"
print(x + 1)

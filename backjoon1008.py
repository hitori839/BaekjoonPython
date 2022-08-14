a, b = input('').split()
a = float(a)
b = float(b)

c = round(a/b, 32)
print("{:.32f}".format(c))

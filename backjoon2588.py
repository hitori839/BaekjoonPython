a = input('')
b = input('')

a = int(a)
b = int(b)

b1 = b % 10
b1 = int(b1)
b2 = ((b - b1) % 100) / 10
b2 = int(b2)
b3 = (b - b1 - b2) / 100
b3 = int(b3)

print(a * b1)
print(a * b2)
print(a * b3)
print(a * b)

n = int(input("Enter the number : "))
a = 0
b = 1
c = 0
i = 1
print(a)
print(b)
while i<=n:
    c = a + b
    a = b
    b = c
    print (c)
    i = i + 1

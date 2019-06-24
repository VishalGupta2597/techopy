a = int(input("Enter first no. : "))
b = int(input("Enter second no. : "))
c = int(input("Enter third no. : "))
d = int(input("Enter fourth no. : "))

print(" a = "  , a , " b = " , b , " c = " , c , " d = " , d)

if a > b and a > c and a > d:
    print(a, "is greatest ")
elif b > a and b > c and b > d:
    print(b, "is greatest ")
elif c > a and c > b and c > d:
    print(c, "is greatest ")
elif d > a and d > b and d > c:
    print(d, "is greatest ")
else:
    print("All numbers are equal")

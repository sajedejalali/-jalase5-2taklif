#moadele_2 = ax * x + bx + c = 0

import math

a = float(input("enter a :"))
b = float(input("enter b :"))
c = float(input("enter c :"))

if a == 0:
    result = -(c / b)
    print("x = ", result)

else :
    rad = float(math.sqrt((b * b) - (4 * a * c)))
    x1 = int((-b + rad) / (2 * a))
    x2 = float((-b - rad) / (2 * a))
    result1 = x1
    result2 = x2
    print("x1 = ", result1, "  and   x2 = ", result2)

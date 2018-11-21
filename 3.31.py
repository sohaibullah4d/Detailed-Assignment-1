print("MUHAMMAD SOHAIB - 18B-054-CS - section A")

print("\t\t\t PROBLEMS: 3.31")
x = eval(input('Enter X:'))
y = eval(input('Enter Y:'))
r = 8

import math
calculation = math.sqrt(x**2 + y**2)

if calculation <= r:
    print('It is in!')
else:
    print('It is not in')

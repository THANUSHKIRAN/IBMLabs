import cmath
a=int(input())
b=int(input())
c=int(input())

d=(b**2)-(4*a*c)
x=(-b+ cmath.sqrt(d))/(2*a)
y=(-b-cmath.sqrt(d))/(2*a)
print(x)
print(y)
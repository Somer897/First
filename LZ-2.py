import math
a = float(input())
b = float(input())
c = float((float(a)**2 + float(b)**2)**0.5)
print("Гипотенуза: " ,c)
if a<b:
   d= float(a) / float(c)
else :
   d = float(b) / float(c)
print('Sin=',d )
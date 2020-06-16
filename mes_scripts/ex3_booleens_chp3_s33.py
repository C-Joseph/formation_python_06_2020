#!/usr/bin/env python3
v=True; f=False
a = v and f
b = v or f
c = not v
d = not f
e = v==f
f = not 0
g = not 0.01
h = not 1
i = v or f and f
j = (v or f) and f
print(a,b,c,d,e,f,g,h,i,j)

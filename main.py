from random import *

q = []
n = 10
for i in range(n):
    m = 5
    for i in range(m):
        q.append(choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"]))
        q.append(randint(1,20))
        if randint(1,100) > 60:
            q.append("x")
    q.append("=")
    for i in range(m):
        q.append(choice(["+", "-", "+", "-", "+", "-", "+", "-", "+", "-", "+", "-"]))
        q.append(randint(1,20))
        if randint(1,100) > 40:
            q.append("x")
    for s in q:
        print(s,end="")
    q.clear()
    print()

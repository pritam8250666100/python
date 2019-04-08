x={"apple","banana","cherry"}
y={"apple","facebook","orkut"}
x.intersection_update(y)
print(x)

y={"a","b","c"}
x={"f","e","d","c","b","a"}
z=x.issuperset(y)
print(z)

x={"Apple","banana","cherry"}
y={"apple","facebook","orkut"}
z=x.symmetric_difference(y)
print(z)

x={"apple","banana","cherry"}
y={"apple","facebook","orkut"}
x.update(y)
print(x)

x={"apple","banana","cherry"}
y={"apple","facebook","orkut"}
z=x.union(y)
print(z)

x={"apple","banana","cherry"}
y={"apple","facebook","orkut"}
z=x.isdisjoint(y)
print(z)

a={"apple","banana","cherry"}
b={"google","facebook","orkut"}
c=a.isdisjoint(b)
print(c)

x={"a","b","c"}
y={"f","e","d","c","b","a"}
z=x.issubset(y)
print(z)

x={"a","b","c"}
y={"f","e","d"}
z=x.issubset(y)
print(z)

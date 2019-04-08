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


a=[]
b=()
c={}
print(type(a))
print(type(b))
print(type(c))



sch={
    "name":"pritam",
    "dept":"IT",
    "age":"18"
    }
print("student name is "+sch["name"])
print("department name is "+sch["dept"])
print(sch.keys())
print(sch.values())
for x in sch:
    print(x+"->"+sch[x])
sch["gender"]="male"
print(sch)

if "age" in sch:
    print("yes, age is a key of sch")



sch.pop("age")
print(sch)

x={'pqr','abc','xyz'}
y=0

sch=dict.fromkeys(x,y)
print(sch)


x=5
if x%2==0:
    print("even")
else:
    print("odd")
























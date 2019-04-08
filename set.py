s=["BMW","BBT","VFW"]
for z in s:
    print(z)
s.append("FORD")
print(s)
s.remove("BMW")
print(s)
if "BBT" in s:
    print("yes it does")
s[0]="bugatti"
print(s)
print(len(s))
x=432
x=s.copy()
print(x)
y=(s.count("BMW"))
print(y)
print(s[2])

b=("abc","xyz","BMW")
print(b[2])
print(b*3)
print(len(b))

c={"ggg","rex","abc","xyz","BMW"}
c.add("kkr")
print(c)
c.remove("rex")
print(c)
c.pop()
print(c)
d={"ggg","rex","abc","xyz","BMW"}
e={"csk","srh","rr","abc"}
d.update(e)
print(d)
z=d.difference(e)
print(z)
d.intersection(e)
print(d)
d.difference_update(e)
print(d)
d.intersection_update(e)
print(d)

import mod
name=input("enter a name: ")
mod.displaymsg(name)



from calc import multi
a=int(input("enter a no.: "))
b=int(input("enter a no.: "))
print("multiply= ",multi(a,b))



from calc import sum
a=int(input("enter a no.: "))
b=int(input("enter a no.: "))
print("sum= ",sum(a,b))


from calc import divide
a=int(input("enter a no.: "))
b=int(input("enter a no.: "))
print("divide= ",divide(a,b))



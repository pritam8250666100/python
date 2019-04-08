temp=[10,-20,-289,100]
def c_to_f(c):
    if c<-273.15:
        print("does not exist")
    else:
        f=c*9/5+32
        return f
for t in temp:
    print(c_to_f(t))


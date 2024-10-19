x={1:"one",2:"two"}
x["first"]="one"
print(x)

x[("Delorme","Ryan",1995)]=(1,2,3)
print(list(x.keys()))

print(x[1])

print(x.get(1,"not available"))

print(x.get(4,"not available"))

print(x)
a=[1,2,3,4,5]
sum=0
for i in range(5):
    a[i]=sum+a[i]
    print("i",i, "a[i]", a[i])

print("sum",sum)
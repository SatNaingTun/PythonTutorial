item_list=[3,"string1",23,14,"string2",49,64,70]
for x in item_list:
    if not isinstance(x,int):
        continue
    if not x % 7:
        print("found and integer divisible by seven: %d"%x)
        break
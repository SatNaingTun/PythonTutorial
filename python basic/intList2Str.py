# def list2string(lst):
#     output=''
#     # delimeter=','
#     for i in lst:
#         output=output+','+str(i)
        
#     return output

list2string = lambda lst: ','.join(str(i) for i in lst)

lst=[1,2,3,4,5]
print(list2string(lst))
#sets in python, sets have no dupe values 
sets={1,2,3,3,4,543,5,5,5,5,5,5,3,211,2,1,23,12,12,}
type(sets)
count =0
for _ in sets:
    count+=1
print (count)
for x in sets:
    print(x,end=" ")
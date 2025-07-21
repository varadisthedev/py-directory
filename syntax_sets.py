#sets in python , are enclosed in {}
b={1,2,4,4,3,5,3,21,21,2,1}
d={2,1,4,2,5,6,6,6,4,32,3,2,3,2,1}
print(b.intersection(d))
print(b.union(d))
count=0 
for _ in b:
    count+=1
print(count)

#in range loops 
for i in range(0,7): # wont include 7, start with 0 
    print(i,end="")
print("\n")

for i in range(5):
    print("hello ",end="")

#zip in python 
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
zipped_object = zip(list1, list2) # created a zip object 
print(list(zipped_object)) #converting to a list for 

# so far so much 
my_list = [1, 2, 3, 4]
my_set = {"a", "b", "c", "d", "e"}
my_tuple = (1, 2, 1, 21, 2, 1, 2, 12, 1, 2)
my_dict = {1: "varad", 2: "raj", 3: "rani"}


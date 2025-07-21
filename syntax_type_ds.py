#use of type() in python 
print(type(12.1))
print(type((12,1)))
print(type({12,1}))
print(type(("hello")))

#dictionies in python are like a hash map  { key , value}
dict ={"varad":12,
       "rani":11,
       "devarshi":34,
       "sharvari":23
       }
print(dict["varad"]) # to print the value of string varad
for key,value in dict.items():
    print(f"{key} has the vaulue: {value}")


#list in python 
list= ['varad', 'devarshi','rohan','aniket','ramayan']
print(list[0])
print(list[-2]) # list can have negative indices, it wraps around the array 
print('varad' in list)
list=list*3
print(list)
#pop the entire list 
while list: list.pop()
print(list)
list.append("hello")
list.append("world")
print(list)

#python f string ?
list2=['varad', 'devarshi','rohan','aniket','ramayan']
print(f'hello there, this is a f string , my name is {list2[0] } ') # must be wrapped inside a print(), the {} statements are evaluated first
print(f"\nhello, this is an f string , {list2[-2]}, and this is a var of type {type("hello")}") 


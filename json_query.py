import json 
my_data={1:"varad",2:"raut",3:"sharvari",4:"hello"}
print(json.dumps(my_data))

# json key cant be tuples
test={(1,2):"hello",4:"hello there"}
#json.dumps(test) # this will give an eror
print(json.dumps(test, skipkeys=True))


# converting useful info to json string 
data={
    "name":"varad",
    "age":19,
    "hobby": "gym",
    "crush":0,
    "is_student": True,
    "skills": ["DSA","js","Python"]
}
printme=json.dumps(data,indent=4)
print(f"\n\n\n{printme}")



# adding text to a file, a json file using json.dump()
with open("data.json", "w") as f:
    json.dump(data, f, indent=4) # expects a python object and not a json string
    print(f"data added to the json file sucessfully!")

#reading from a json file 
with open("fruits.json","r") as r:
    data_loaded= json.load(r)
    print(f"the value of key fruit is {data_loaded["fruit"]}")
    print(f"the value of key size is {data_loaded["size"]}")

#nested json 
with open("example_2.json","r") as read:
    reader=json.load(read)
    print(f"\n\nthe question one is:  {reader["quiz"]["sport"]["q1"]["question"]}")
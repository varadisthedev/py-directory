arr={'1':1,'2':4,'5':25,'7':49}
print(arr.keys())
print(arr.values())


# approach 2 
print(arr)

# que 2 Library Management System (Basic)
#You are building a small part of a library system.
# Create a Python script where a list stores the names of borrowed books.
# Ask the user to input the name of a book they want to borrow. 
# If it's already borrowed, inform them; otherwise, add it to the list.

list=["encyclo","parrottales","rio"]
user=input("enter the name of book you borrowed: ") 
if user in list:
    print("book is already borrowed by someone ")
else:
    print("registed by your name!")
    list.append(user)



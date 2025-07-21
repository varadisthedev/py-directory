#python walrus operator
print(var:="hello world!");
var2="varad"
print("hello",var2,",",var)

#string cocatination
var3="helo"*4
print(var3)

#arrays and loops 
arr=["apple","banana","kiwi"]
for x in arr:
    print(x,end="-") #the default end is newline char 
    print(".",end="")

#use of sep 
print("\n")
print("varad","ankita","sharvari","devarshi","abhas","aditi","rani",sep=" op, ")

#input in python 
print("enter your damn name: ")
my_var=input();
print("entereed name is: ",my_var)
print('Hi, {}'.format(my_var))

#input with a default message
var=input("hello there, whats your college's name? :")
print(var)

#function in python 
def print_newline():
    print("\n")
    return 1;
print("hello",print_newline(),"how are you?")

#using of len with if else
password="*ComboInter123Galatic#$"
if(len(password)>8):
    print("password accepted")
else:
    print("pass too short. ")

#type casting in python
a="123"
az=int(a);
if az>121:
    print("type casting sucess")
else:
    print("failed")
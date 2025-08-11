def check_stack_isEmpty(stk): 
  if stk==[]:
    return True
  else:
   return False
top = None
s=[1,2,3,4]
def push(stk,e): 
  stk.append(e)
  top =len(stk)-1
def main_menu():
 while True:
    print("Stack Implementation")
    print("1 - Push")
    print("2 - Pop")
    print("3 - Peek") 
    print("4 - Display") 
    print("5 - Exit")
ch = int(input("Enter the your choice:"))
if ch==1:
    el = int(input("Enter the value to push an element:"))
    push(s,el)
elif ch==2:
    e=pop_stack(s)
    if e=="UnderFlow":
     print("Stack is underflow!")
    else:
     print("Element popped:")
elif ch==3:
      e=pop_stack(s)
      if e=="UnderFlow":
        print("Stack is underflow!")
      else: print("The element on top is:")
elif ch==4:
    isplay(s) 
elif ch==5:
    sys.exit()
else:
  print("Sorry, You have entered invalid option")

def display(stk):
  if check_stack_isEmpty(stk): 
   print("Stack is Empty")
  else:
    top = len(stk)-1 
    print(stk[top],"-Top")
    for i in range(top-1,-1,-1): print(stk[i])

def pop_stack(stk):
  if check_stack_isEmpty(stk):
      return "UnderFlow"
  else:
    e = stk.pop()
    if len(stk)==0:
        top = None
    else:
        top = len(stk)-1
    return e

def peek(stk):
  if check_stack_isEmpty(stk):
      return "UnderFlow"
  else: top = len(stk)-1 
  return stk[top]

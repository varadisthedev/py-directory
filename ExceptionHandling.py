# basic python exception and handling it 
try:
    num=10/0
    print("div by 0 is not possible")
except ZeroDivisionError:
    print("you cant divide by zero!")
except Exception as e:
    print(f"caught the exception: {e} not possible")
finally:
    print("exception handling works in simple terms, you make a try block to run a code\n"
          "except block to catch a code and a finally block to make a part of code run regardless")
    


# creating a fucntion and a custom exception 
def set_password(password):
    if len(password)<8:
        raise ValueError("Password should be atleast 8 digit long!")
    else:
        print("Password set sucessfully!")

try:
    set_password("123")
except ValueError as e:
    print(f"Error setting password: {e}")

import os 
import os.path 


# os.getcwd()  | to get the current working directry where all functions and operations are being operated
print(os.getcwd())


# os.chdir('../') | to move up, one directry, this shifts workign of all commands up, one directory and not just for the os module 
os.chdir('../')
print(os.getcwd())
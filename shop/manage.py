"CRUD"
#creat
#read
#update
#delete

from products import create, read

while True:
    oper = input("c/r/u/d:")
    if oper == 'c':
        create()
    elif oper == 'r':
        read()


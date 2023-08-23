#this is how we create function in python with no argument 
def printgm():
    print("good morning!")

printgm()
print("\n")

# this is how we create function with one argument
def wish(name):
    print(name,"good morning sir")

a = input("enter your name \n")
wish(a)
print('\n')

# this is how we create function with two argument
def sum(a,b):
    c = a+b
    print("the sum is",c)
d= int(input("enter the number for a\n"))
e=int(input("enter the another number for b\n"))
sum(d,e)

#this is how we set defalut value
def pi(pi=3.14):
    print("the value of pi is :-",pi)

pi()

#Any number of arguments: *args
def mynumber(*args):
    for item in args:
        print(item)

mynumber(10,12,34,43,45,65)
mynumber([12,43,45,65,78,98])


#exception handling use to make our program run fluently
#in exception handling we use try and except key word lets see the use in code
try:
    i = 30/0
    print(i)
except:
    print("number is divided by zero")    

'''Good practice it to specify the type of exception we are trying to catch,
which helps a lot when debugging the code later.
If you know a block of code can throw an IndexError, specify it in the
except:'''

try:
    car = ["maruti","hummer","nano"]
    print(car[3])
except IndexError:
    print("there is no such index")

# use of else with try and except operation
try:
    car = "my car name is honda civic"
    print(car)
except:
    print("there is an error")
else:
    print("no error")    

#raise operatio, The raise command allows you to manually raise an exception.    
# try:
#     raise IndexError("this index is not allowed")#this is how we use raise operation in exception handling
# except:
#     print("print the right index")
#     raise #donot forget to close the raise with raise key word

# finally operation with exception handling
'''The finally block is executed independently of exceptions being raised
or not.'''

#if you want to see the output then comment the line number 30,31,32,33,34
try:
    print(my-first-name)
except NameError:
    print("name not found")
finally:
    print("finally you are block")

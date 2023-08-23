'''The dictionary doesn't guarantee the order of the elements and it is
mutable.
One important characteristic of dictionaries is that you can set your
customized access keys for each element.'''
# Initialization of a Dictionary
#it is initialize by the help of curly braces
dict = {}#this is a empty dictionary
dict1 = {"apple":"fruit","mohan":"human being","Anomynous":"ethical hacker"}#dictnory which is having the value
#there are several way to access dictinory
print(dict1)#:- first way
print("\n")
#suppose you want to access the value of particular word present inside the dictinory
print(dict1["Anomynous"])#this is how we access the value of any word which is peresent inside the dictionary
print("\n")
#we can also print the value of dictinory by the help of for loop
for items in dict1:
    print(items) #drawback is we get the items only not the value by this command
    print(dict1[items])#now we get both value as well as items
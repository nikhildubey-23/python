'''A tuple is similar to a list: it's ordered, and allows repetition of items.
There is just one difference: a tuple is immutable.
Immutability, if you remember, means you can't change a tuple after its
creation. If you try to add an item or update one, for instance, the Python
interpreter will show you an error. we create the tupple by the help of prenthises bracket'''
bestfriends = ("mohan","vinit","4number","mauli","preeti","abhinay","laptop","my self")
#the only one thing we can perform with tupple if retriving
print(bestfriends[1])#this is how we retrive by index
print("\n")
i = 0
for item in bestfriends:#and this is how we retrive all by for loop
    print(item)




'''yes it is true that we cannot update the tupple but if we want we can do anything'''
#so we have a tupple
bestfriends = ("mohan","vinit","4number","mauli","preeti","abhinay","laptop","my self")
#now we convert this tupple into a list
friends  = list(bestfriends)
#adding new member 
friends [7] = "Anomynous"
bestfriends = tuple(friends)
print(bestfriends)
'''this is how we can manipulate the code'''
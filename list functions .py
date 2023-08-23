# in python there are many function in list but we see wich are most commonly used 
'''funtion 1 = append() , this function use to add the another value in the last index of the list 
    function 2 = insert(),this function use to take the index value were you want to insert the data or you can say value and that value
    funtion 3 = remove(),as by the name we can  understand this function is use to revome the value present inside the list
    function 4 = clear() , this function use to delete valu of complete list 
    '''
# lets see all the function one by one 
friends = ['nidhi','sohan','dev','aditya','preeto']#let we have a list of friends
print("before appling the append function the result will be\n",friends,"\n")
friends.append("anomynous")
print("after appling the append function the result will be\n",friends,"\n")
print("before appling the insert function the result will be",friends,"\n")
friends.insert(0,"neha")
print("after appling the insert function the result will be\n",friends,"\n")
print("before appling the remove function the result will be\n",friends,"\n")
friends.remove("neha")
print("after appling the remove function the result will be\n",friends,"\n") 
print("before appling the clear function the result will be\n",friends,"\n")
friends.clear()
print("after appling the clear function the result will be\n",friends,"\n")

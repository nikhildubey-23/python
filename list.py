'''A list has its items ordered and you can add the same item as many
times as you want.'''
# in python list is a type of array as we have in other programing language
friends = ["rohit","mohit","sohit"]#this is how we create list in python by the help of pair of square bracket
enemy = ["whole","world"]
# print(enemy[0])
for i in range(len(friends)):#as we did earlier same we did here len()function id used to know the lenght of any value present in any variable , even we can directly give the string which you want to know the lenght 
    print(i+1,friends[i])#printing the value of list present in friends varibale
for j in range(len(enemy)):
    print(j+1,enemy[j])#print the value of enemy 

# ******************************example how we use lenght direct with value ************************
print("printing the length of string","\n",len("i love my india"))

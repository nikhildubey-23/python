# we create any file by the help of open function
file = open("hello.txt","w")
#suppose we want to write anything inside the file so we use the command 
file.write("hello my name is \n")
file.write("anomynous\n")
file.close()
file = open("hello.txt",'r')#r attribute we use for to read the contant inside the file
print(file.read())#we use read function to read the complete content of the file
#if you want to read the line of the file then we have to use the function readline()
print(file.readline()) # if you want to see the output then you have to comment the line number 8 completly



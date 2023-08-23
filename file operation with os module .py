#for doing operation with os module we have to import that
#here we see the 3 major function of os module that is delete,rename,and checking the 
#content present or not
from shutil import copyfile
import os
# suppose we created file by the name of gust
gust = open("gust.txt",'x')
 # for creataing file
#after sometime we realise that what we created it is just useless so forto delete that file we have a function in os module that is remove
# os.remove("gust.txt") #for deleting file , if you want to see the output of this line you have to comment the complete line number 5 if you dont do then you get the error
#if we wnat to rename that file so for that we have  a function in os module that is rename
#os.rename("gust.txt","friends.txt")
#if you want to see the output then first comment the line number five then un comment line number 10
#now we check if file realy exists or not , for that we have a function os.path.exists in os module
if os.path.exists("friends.txt"):
    print("yes it exists")
else:
    print("donot exists")

#suppose you want to copy the content written in one file into another file for that we use shutil module which we have to import
copyfile("gust.txt","friends.txt")
#for to see the output you have to comment the line number seever
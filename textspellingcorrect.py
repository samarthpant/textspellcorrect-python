# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 13:03:01 2020

@author: Samarth Pant
"""

from textblob import TextBlob

file1=open("textspellingcorrect.txt","r+")


a=file1.readlines()
#above line returns a list so we convvert the list to string using isttostring function..
def listToString(s):  
    
    # initialize an empty string 
    str1 = ""  
    
    # traverse in the string   
    for ele in s:  
        str1 += ele   
    
    # return string   
    return str1  
c=listToString(a)  

print("Orginal file :"+str(c))

#correct is a textblob clss that will automatically correct all the spelling mistakes..

b=TextBlob(c)
print("Corrected Text:"+str(b.correct()))
file1.close()

d=open("textspellingcorrect.txt","w")
d.write(str(b.correct()))
d.close()

# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:41:05 2019

@author: kmh02
"""

import collections as col
file = 'northwind.txt'

with open (file,'r') as word_list:
    total = word_list.read()
    words= total.split()
    
#lettercount = []
#for w in total:
#    lettercount.append(total.count(w))
#    print (w, lettercount[-1])
    
   
# words separated 
wordcount=[]
for w in words: #could also use enumerate, then use i 
#for i,w in enumerate(lines):
   wordcount.append(words.count(w))
   print (w,wordcount[-1])

    
counter = col.Counter()

for let in total:
    counter[let]+=1 
print (counter)
    
    
    #with enumerate, would use i instead of -1
    #zip allows being able to print both together 

"""
Assignment to count words in string, and then count frequencies of letters.
Best method of counting is with collection, not nested for loops. 
Can use the commented out lettercount, but that doesnt assign the value to the letter.
If use lettercount list, can use zip method to pull both letter and value together. 

 
    
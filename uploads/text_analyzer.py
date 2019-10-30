# -*- coding: utf-8 -*-
"""
Created on Tue Mar 26 06:16:48 2019

@author: APU
"""

word = "   abcee hje ethjd"
print (word)

word.strip()
print (word)

word.replace(' ', '')
print (word)

print(word.split('ee'))

# first get all lines from file
with open('E:/TTU/ML Projects/text.txt', 'r') as f:
    lines = f.readlines()

# remove spaces
lines = [line.replace(' ', '') for line in lines]

# finally, write lines in the file
with open('E:/TTU/ML Projects/file.txt', 'w+') as f:
    f.writelines(lines)
    
with open('E:/TTU/ML Projects/file.txt', 'r') as f:
    no_space_line = f.read()
    
no_space_line = no_space_line.split('bm')

with open('E:/TTU/ML Projects/segment.txt', 'w') as f:
    for seg in no_space_line:
        print (len(seg))
        f.write("%s\n" % seg)

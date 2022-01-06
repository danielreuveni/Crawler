#/*************************
#* Daniel Reuveni
#* 207982869
#* 01
#* ass07
#**************************/

import re
import csv

#initialize the list and dictionary
d = {}
l=[]

#/************
#* Function Name:  crawler
#* Input: name of the file
#* Output: dictionary with links to other files in the real file
#* Function Operation: find the name of the fules in the links, put in dictionary, and go with recursion to the next file
#*************/

def crawler(file):
    text = open(file, "rt")
    text = (text.read())
    #find the names of the files from the links
    result = re.findall(r'<a href=(.*?)/a>', text)
    str = ''.join(result)
    result = re.findall(r'"(.*?).html">', str)
    l=[]

    #loop: insert the names of the files into the dictionary and sort them
    for i in range(len(result)):
        if result[i] not in l:
            l.insert(i, result[i] + '.html')
            l.sort()
            d[file] = l
    # in case of name that exist, the file will be exist 1 time only 
    if len(result) == 0 :
       l=[]
       d[file] = l

    #file.close()

    #add the endind: ".html" to the name of the file
    for i in range(len(result)):
      if (result[i] + '.html') in d:
          #stop condition
         return 0
      else:
          #the recursion
         crawler(result[i] + '.html')

file = input("enter source file:\n")
#the call to recursion
crawler(file)
#crease a csv file
with open('results.csv', 'w') as f:
    for key in d.keys():
        str = ','.join(d[key])
        f.write("%s,%s\n" % (key,str))
file = input("enter file name:\n")
print(d[file])









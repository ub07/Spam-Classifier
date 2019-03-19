allwords = []
import os
import glob
import pandas
os.chdir("E:\Spam Classifier")

#load and concatenate all the emails in ine string
Files= [f for f in glob.glob("data\\*\\*.txt")]
for f in Files:
    file = open(f,"r")
    words = file.read().split()
    for w in words:
        allwords.append(w)
 
#count the strings       
result = pandas.value_counts(allwords)[:2500]   
     
#write in Dictionary.txt file
rname = list(result.index)
file = open("dictionary.txt","w+")
for i in range(len(result)):
    file.write("%d. %s %d\n"%(i+1,rname[i],result[i]))
file.close()    
    

    
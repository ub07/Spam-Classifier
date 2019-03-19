import get_dictionary_list as gl
import glob
import pandas as pd
dictionary_list = gl.get_dictionary_lists()

#Train Feature
#Train Label

doc_Id = 1
columns = ["doc_Id","word","Count"]
featureTrain = pd.DataFrame(columns = columns)
labelTrain = []
j=0

Files= [f for f in glob.glob("data\\nonspam-train\\*.txt")]
for f in Files:
    file = open(f,"r").read().split()
    for i in range(len(dictionary_list)):
        word  = dictionary_list[i]
        count = file.count(word)
        if count>0:
            featureTrain.loc[j] = [doc_Id,i+1,count]
            j=j+1
    labelTrain.append(0)
    doc_Id = doc_Id+1
    if doc_Id>50:
        break
  
Files= [f for f in glob.glob("data\\spam-train\\*.txt")]
for f in Files:
    file = open(f,"r").read().split()
    for i in range(len(dictionary_list)):
        word  = dictionary_list[i]
        count = file.count(word)
        if count>0:
            featureTrain.loc[j] = [doc_Id,i+1,count]
            j=j+1
    labelTrain.append(1)
    doc_Id = doc_Id+1
    if doc_Id>100:
        break      
    
file = open("train-features.txt","w+")
for i in range(len(featureTrain)):
    file.write("%d %d %d\n"%(featureTrain["doc_Id"][i],featureTrain["word"][i],featureTrain["Count"][i]))
file.close() 

file = open("train-labels.txt","w+")
for i in range(len(labelTrain)):
    file.write("%d\n"%(labelTrain[i]))
file.close() 

#Test Feature
#Test label

doc_Id = 1
columns = ["doc_Id","word","Count"]
featureTest = pd.DataFrame(columns = columns)
labelTest = []
j=0

Files= [f for f in glob.glob("data\\nonspam-test\\*.txt")]
for f in Files:
    file = open(f,"r").read().split()
    for i in range(len(dictionary_list)):
        word  = dictionary_list[i]
        count = file.count(word)
        if count>0:
            featureTest.loc[j] = [doc_Id,i+1,count]
            j=j+1
    labelTest.append(0)
    doc_Id = doc_Id+1
    
  
Files= [f for f in glob.glob("data\\spam-test\\*.txt")]
for f in Files:
    file = open(f,"r").read().split()
    for i in range(len(dictionary_list)):
        word  = dictionary_list[i]
        count = file.count(word)
        if count>0:
            featureTest.loc[j] = [doc_Id,i+1,count]
            j=j+1
    labelTest.append(1)
    doc_Id = doc_Id+1
       
    
file = open("test-features.txt","w+")
for i in range(len(featureTest)):
    file.write("%d %d %d\n"%(featureTest["doc_Id"][i],featureTest["word"][i],featureTest["Count"][i]))
file.close() 

file = open("test-labels.txt","w+")
for i in range(len(labelTest)):
    file.write("%d\n"%(labelTest[i]))
file.close() 


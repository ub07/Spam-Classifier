import numpy as np
numTrainDocs = 100
numTokens = 2500

#Load Train Email Features
file = open("train-features.txt","r").readlines()
train_matrix = np.zeros((numTrainDocs,numTokens))
for f in file:
    temp = f.split()
    train_matrix[int(temp[0])-1,int(temp[1])-1] = int(temp[2])
    
#Load Train Labels
train_labels = [int(n) for n in open("train-labels.txt","r").read().split()]

#Find spam and nonspam emails indexes
spam_indices =[i for i, x in enumerate(train_labels) if x==1]
nonspam_indices = [i for i, x in enumerate(train_labels) if x==0] 

#Number of words for each mail
email_lengths = np.sum(train_matrix,axis=1) 

#Count number of words in spam and nonspam emails
spam_wc = sum(email_lengths[spam_indices])
nonspam_wc = sum(email_lengths[nonspam_indices])

#Impact of each word of the dictionary in spam and nonspam
prob_token_spam = (np.sum(train_matrix[spam_indices,:],axis=0)+1)/(spam_wc+numTokens)
prob_token_nonspam = (np.sum(train_matrix[nonspam_indices,:],axis=0)+1)/(nonspam_wc+numTokens)

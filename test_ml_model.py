#Test Data
import training_ml_model as tr_m
import numpy as np
numTokens =2500

file = open("test-features.txt","r").readlines()
numTestDocs = int(file[-1].split()[0])
test_matrix = np.zeros((numTestDocs,numTokens))
for f in file:
    temp = f.split()
    test_matrix[int(temp[0])-1,int(temp[1])-1] = int(temp[2])

output = np.zeros((numTestDocs,1))

prob_spam = len(tr_m.spam_indices)/tr_m.numTrainDocs

log_a = np.dot(test_matrix,np.log(tr_m.prob_token_spam)) + np.log(prob_spam)
log_b = np.dot(test_matrix,np.log(tr_m.prob_token_nonspam)) +np.log(1-prob_spam)

output = log_a>log_b;

test_labels = [int(n) for n in open("test-labels.txt","r").read().split()]

wrong_classification =  sum(output^test_labels)
 
error = wrong_classification/numTestDocs 
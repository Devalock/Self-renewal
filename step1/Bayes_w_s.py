# -*- coding: utf-8 -*-
from sklearn.model_selection import LeaveOneOut
import numpy as np
from sklearn import svm
from scipy import stats
import random
import sys
from sklearn.naive_bayes import GaussianNB
from sklearn.model_selection import RepeatedKFold
from sklearn.metrics import roc_auc_score, f1_score, recall_score, precision_score, matthews_corrcoef, accuracy_score
import warnings
warnings.filterwarnings("ignore")

def performance_measure(y_actual, y_hat):
    TP = 0
    FP = 0
    TN = 0
    FN = 0

    for i in range(len(y_hat)):
        if y_actual[i] == y_hat[i] == 1:
            TP += 1
        if y_hat[i] == 1 and y_actual[i] == 0:
            FP += 1
        if y_hat[i] == y_actual[i] == 0:
            TN += 1
        if y_hat[i] == 0 and y_actual[i] == 1:
            FN += 1
    sensitivity = TP / (TP + FN)
    specificity = TN / (TN + FP)
    # pos_pred_val = TP/ (TP+FP)
    # neg_pred_val = TN/ (TN+FN)

    # return sensitivity, specificity, pos_pred_val, neg_pred_val
    return sensitivity, specificity


direct=sys.argv[1]
#matrix = np.loadtxt(direct + 'CVinput.txt',dtype=bytes).astype(str)
matrix = np.loadtxt(direct + 'CVinput.txt')
feature = np.array(matrix[:,1:])
tag = np.array(matrix[:,0])

re=10
kf = RepeatedKFold(n_splits=5, n_repeats=re,random_state=10086)
sum_auc = 0
'''
sum_recall = 0
sum_precision = 0
sum_f1 = 0
sum_acc = 0
sum_mcc = 0
'''
judge_final = np.zeros((101,8))
info = {}
for train, test in kf.split(feature):
	model_train = feature[train]
	model_test = feature[test]
	model_train_tag = tag[train]
	model_test_tag = tag[test]

	clf = GaussianNB()

	clf.fit(model_train, model_train_tag) 

	predict_prob_y = clf.predict_proba(model_test)
	#print (test)
	for ind in range(0,len(test)):
		if test[ind] in info:
			sump=info[test[ind]]+np.array(predict_prob_y)[:,1][ind]
			info[test[ind]]=sump
		else:
			info[test[ind]]=np.array(predict_prob_y[:,1])[ind]
	test_auc = roc_auc_score(model_test_tag,predict_prob_y[:,1])
	sum_auc += test_auc
	#print test_auc

	recall = 0
	precision = 0
	f1 = 0
	acc = 0
	mcc = 0
	#prediction = clf.predict(model_test)
	judge = []
	
	for cutoff in range(0, 101):
		prediction = []
		judge_p = []
		for i in predict_prob_y[:, 1]:
			if i>cutoff*0.01:
				i=1
			else:
				i=0
			prediction.append(i)
		'print (len(prediction),len(model_test_tag))'
		'''
		sum_recall += recall_score(model_test_tag, prediction)
		sum_precision += precision_score(model_test_tag, prediction)
		sum_f1 += f1_score(model_test_tag, prediction)
		sum_acc += accuracy_score(model_test_tag, prediction)
		sum_mcc += matthews_corrcoef(model_test_tag, prediction)
		'''

		recall = recall_score(model_test_tag, prediction)
		precision = precision_score(model_test_tag, prediction)
		sensitivity = performance_measure(model_test_tag, prediction)[0]
		specificity = performance_measure(model_test_tag, prediction)[1]
		f1 = f1_score(model_test_tag, prediction)
		acc = accuracy_score(model_test_tag, prediction)
		mcc = matthews_corrcoef(model_test_tag, prediction)

		judge_p.append(0.01*cutoff)
		judge_p.append(recall)
		judge_p.append(precision)
		judge_p.append(f1)
		judge_p.append(acc)
		judge_p.append(mcc)
		judge_p.append(sensitivity)
		judge_p.append(specificity)
		judge.append(np.array(judge_p))
	#print (np.array(judge).shape,judge_final.shape)
	#print (judge[0],judge_final[0])
	judge_final += np.array(judge)
np.savetxt(direct + 'Bayes_CVroc_w_s.txt', np.array(judge_final)/(5*re), fmt='%.3f',delimiter='\t')
with open(direct + 'Bayes_CVroc_w_s.txt',"a") as f_out:
	f_out.write('%.3f\t' %(sum_auc/(5*re)))

f = open(direct + 'Bayes_CVProb.txt','w')
for key in sorted(info.keys()):
	f.write('{:.3f}'.format((info[key])/re) + '\n')
f.close()

# -*- coding: utf-8 -*-
from sklearn.model_selection import LeaveOneOut
import numpy as np
from sklearn import svm
from scipy import stats
import random
import sys
from sklearn.ensemble import RandomForestClassifier
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


direct = sys.argv[1]
# matrix = np.loadtxt(direct + 'CVinput.txt',dtype=bytes).astype(str)
matrixT = np.loadtxt(direct + 'CVinput.txt')
featureT = np.array(matrixT[:,1:])
tagT = np.array(matrixT[:,0])

matrixI = np.loadtxt(direct + 'Intestinput.txt')
featureI = np.array(matrixI[:,1:])
tagI = np.array(matrixI[:,0])

sum_auc = 0
re = 10
judge_final = np.zeros((101, 8))

for r in range(1, 11):
    model_train = featureT
    model_test = featureI
    model_train_tag = tagT
    model_test_tag = tagI

    clf = RandomForestClassifier(n_estimators=500)
    clf.fit(model_train, model_train_tag) 

    predict_prob_y = clf.predict_proba(model_test)
    
    test_auc = roc_auc_score(model_test_tag,predict_prob_y[:,1])
    sum_auc += test_auc

    recall = 0
    precision = 0
    f1 = 0
    acc = 0
    mcc = 0
    # prediction = clf.predict(model_test)
    judge = []

    for cutoff in range(0, 101):
        prediction = []
        judge_p = []
        for i in predict_prob_y[:, 1]:
            if i > cutoff * 0.01:
                i = 1
            else:
                i = 0
            prediction.append(i)

        recall = recall_score(model_test_tag, prediction)
        precision = precision_score(model_test_tag, prediction)
        sensitivity = performance_measure(model_test_tag, prediction)[0]
        specificity = performance_measure(model_test_tag, prediction)[1]
        f1 = f1_score(model_test_tag, prediction)
        acc = accuracy_score(model_test_tag, prediction)
        mcc = matthews_corrcoef(model_test_tag, prediction)

        judge_p.append(0.01 * cutoff)
        judge_p.append(recall)
        judge_p.append(precision)
        judge_p.append(f1)
        judge_p.append(acc)
        judge_p.append(mcc)
        judge_p.append(sensitivity)
        judge_p.append(specificity)
        judge.append(np.array(judge_p))
    judge_final += np.array(judge)
np.savetxt(direct + 'RF_Inroc_w_s.txt', np.array(judge_final)/re, fmt='%.3f',delimiter='\t')
with open(direct + 'RF_Inroc_w_s.txt', "a") as f_out:
    f_out.write('%.3f\t' %(sum_auc/re))

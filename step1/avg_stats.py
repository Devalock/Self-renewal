#! /usr/bin/env python3
import os
import time
from collections import defaultdict
dir = "/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/"
methods = ["RF", "SVM", "Bayes", "Neural", "LGBM"]
feas = ["RNA-seq", "ATAC", "RNAPII", "H3K27ac", "H3K4me1", "H3K4me3", "H3K9me3", "H3K27me3", "CTCF", "Smc1", "Smc3", "YY1", "Oct4", "Sox2", "Nanog", "mergeFeature"]
names = locals()


def add_list(L1, L2):
    L3 = list()
    if len(L1) == 0:
        L3 = L2
    elif len(L1) == len(L2):
        for i in range(len(L1)):
            L3.append(float(L1[i]) + float(L2[i]))
    return L3


def divide_list(L1, num):
    L2 = list()
    for i in L1:
        L2.append(round(i / num, 3))
    return L2


with open("auc_CV_difMethod.txt", "w")as f0, open("auc_In_difMethod.txt", "w")as f1:
    for method in methods:
        names["d_rec_CV_%s" % method], names["d_rec_In_%s" % method] = defaultdict(list), defaultdict(list)
        names["d_auc_CV_%s" % method], names["d_auc_In_%s" % method] = 0, 0
        with open("%s_CV_stats.txt" % method, "w")as f2, open("%s_In_stats.txt" % method, "w")as f3:
            f0.write(method)
            f1.write(method)
            for i in range(1, 101):
                with open((dir % i) + "mergeFeature/%s_CVroc_w_s.txt" % method)as f:
                    lines = f.readlines()
                    for v in range(0, 101):
                        names["d_rec_CV_%s" % method][v] = add_list(names["d_rec_CV_%s" % method][v], lines[v].strip().split("\t"))
                    auc = float(lines[101].strip())
                    names["d_auc_CV_%s" % method] += auc
                    f0.write("\t%s" % round(auc, 3))
                with open((dir % i) + "mergeFeature/%s_Inroc_w_s.txt" % method)as f:
                    lines = f.readlines()
                    for v in range(0, 101):
                        names["d_rec_In_%s" % method][v] = add_list(names["d_rec_In_%s" % method][v], lines[v].strip().split("\t"))
                    auc = float(lines[101].strip())
                    names["d_auc_In_%s" % method] += auc
                    f1.write("\t%s" % round(auc, 3))
            f0.write("\n")
            f1.write("\n")
            for i in range(0, 101):
                f2.write("\t".join(list(map(str, divide_list(names["d_rec_CV_%s" % method][i], 100)))) + "\n")
                f3.write("\t".join(list(map(str, divide_list(names["d_rec_In_%s" % method][i], 100)))) + "\n")
            f2.write("%s\n" % (round(names["d_auc_CV_%s" % method] / 100, 3)))
            f3.write("%s\n" % (round(names["d_auc_In_%s" % method] / 100, 3)))

with open("Methods_stats_0.5.txt", "w")as f0, open("Methods_ROC.txt", "w")as f1:
    f1.write("Method\tFPR\tTPR\n")
    f0.write("\t".join(["method", "Recall_CV", "Precision_CV", "F1_CV", "ACC_CV", "MCC_CV", "AUC"]) + "\n")
    for method in methods:
        f0.write("%s\t" % method)
        with open("%s_CV_stats.txt" % method)as f2, open("%s_In_stats.txt" % method)as f3:
            lines2 = f2.readlines()
            for line in lines2[:101]:
                Recall, specificity = line.strip().split("\t")[1], line.strip().split("\t")[-1]
                f1.write("%s\t%s\t%s\n" % (method, round(1 - float(specificity), 3), Recall))
            the_line = lines2[50]
            Recall_CV, Precision_CV, F1_CV, ACC_CV, MCC_CV = the_line.strip().split("\t")[1:6]
            AUC_CV = lines2[101].strip()

            lines3 = f3.readlines()
            #for line in lines3:
            #    Recall, specificity = line.strip().split("\t")[1], line.strip().split("\t")[-1]
            #    f1.write("%s\t%s\t%s\n" % (method, 1 - float(specificity), Recall))
            the_line = lines3[50]
            Recall_In, Precision_In, F1_In, ACC_In, MCC_In = the_line.strip().split("\t")[1:6]
            AUC_In = lines3[101].strip()
        f0.write("%s (%s)\t%s (%s)\t%s (%s)\t%s (%s)\t%s (%s)\t%s (%s)\n" % (Recall_CV, Recall_In, Precision_CV, Precision_In, F1_CV, F1_In, ACC_CV, ACC_In, MCC_CV, MCC_In, AUC_CV, AUC_In))


with open("auc_CV_difFeature.txt", "w")as f0, open("auc_In_difFeature.txt", "w")as f1:
    for fea in feas:
        names["d_rec_CV_%s" % fea], names["d_rec_In_%s" % fea] = defaultdict(list), defaultdict(list)
        names["d_auc_CV_%s" % fea], names["d_auc_In_%s" % fea] = 0, 0
        with open("%s_CV_stats.txt" % fea, "w")as f2, open("%s_In_stats.txt" % fea, "w")as f3:
            f0.write(fea)
            f1.write(fea)
            for i in range(1, 101):
                with open((dir % i) + "%s/RF_CVroc_w_s.txt" % fea)as f:
                    lines = f.readlines()
                    for v in range(0, 101):
                        names["d_rec_CV_%s" % fea][v] = add_list(names["d_rec_CV_%s" % fea][v], lines[v].strip().split("\t"))
                    auc = float(lines[101].strip())
                    names["d_auc_CV_%s" % fea] += auc
                    f0.write("\t%s" % round(auc, 3))
                with open((dir % i) + "%s/RF_Inroc_w_s.txt" % fea)as f:
                    lines = f.readlines()
                    for v in range(0, 101):
                        names["d_rec_In_%s" % fea][v] = add_list(names["d_rec_In_%s" % fea][v], lines[v].strip().split("\t"))
                    auc = float(lines[101].strip())
                    names["d_auc_In_%s" % fea] += auc
                    f1.write("\t%s" % round(auc, 3))
            f0.write("\n")
            f1.write("\n")
            for i in range(0, 101):
                f2.write("\t".join(list(map(str, divide_list(names["d_rec_CV_%s" % fea][i], 100)))) + "\n")
                f3.write("\t".join(list(map(str, divide_list(names["d_rec_In_%s" % fea][i], 100)))) + "\n")
            f2.write("%s\n" % (round(names["d_auc_CV_%s" % fea] / 100, 3)))
            f3.write("%s\n" % (round(names["d_auc_In_%s" % fea] / 100, 3)))


with open("Features_stats_0.5.txt", "w")as f0:
    f0.write("\t".join(["method", "Recall_CV", "Precision_CV", "F1_CV", "ACC_CV", "MCC_CV", "AUC"]) + "\n")
    for fea in feas:
        f0.write("%s\t" % fea)
        with open("%s_CV_stats.txt" % fea)as f2, open("%s_In_stats.txt" % fea)as f3:
            lines2 = f2.readlines()
            the_line = lines2[50]
            Recall_CV, Precision_CV, F1_CV, ACC_CV, MCC_CV = the_line.strip().split("\t")[1:6]
            AUC_CV = lines2[101].strip()

            lines3 = f3.readlines()
            the_line = lines3[50]
            Recall_In, Precision_In, F1_In, ACC_In, MCC_In = the_line.strip().split("\t")[1:6]
            AUC_In = lines3[101].strip()
            f0.write("%s (%s)\t%s (%s)\t%s (%s)\t%s (%s)\t%s (%s)\t%s (%s)\n" % (Recall_CV, Recall_In, Precision_CV, Precision_In, F1_CV, F1_In, ACC_CV, ACC_In, MCC_CV, MCC_In, AUC_CV, AUC_In))

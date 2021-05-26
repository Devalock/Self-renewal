#! /usr/bin/env python3
import os

feas = ["RNA-seq", "ATAC", "RNAPII", "H3K27ac", "H3K4me1", "H3K4me3", "H3K9me3", "H3K27me3", "CTCF", "Smc1", "Smc3", "YY1", "Oct4",
        "Sox2", "Nanog", "mergeFeature"]
for fea in feas:
    os.system("perl ./Bayes_run.pl %s &" % fea)
    os.system("perl ./Neural_run.pl %s &" % fea)
    os.system("perl ./SVM_run.pl %s &" % fea)
    os.system("perl ./XGboost30.pl %s &" % fea)

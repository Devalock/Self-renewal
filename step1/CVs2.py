#! /usr/bin/env python3
import os

feas = ["RNA-seq", "ATAC", "RNAPII", "H3K27ac", "H3K4me1", "H3K4me3", "H3K9me3", "H3K27me3", "CTCF", "Smc1", "Smc3", "YY1", "Oct4",
        "Sox2", "Nanog", "loops_count_15k", "anchor_RNAPII_15k", "anchor_H3K27ac_15k", "loops_count_30k", "anchor_RNAPII_30k", "anchor_H3K27ac_30k", "mergeFeature"]
for fea in feas:
    os.system("perl ./LGBMboost_run.pl %s &" % fea)

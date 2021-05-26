#! /usr/bin/env python3
import os
d = dict()
with open("/data3/pghzeng/self_renewal/Model/RawData/v3.final.selected_all_TID.signals.rm_loop.txt")as f:
    header = f.readline()
    lines = f.readlines()
    for line in lines:
        TID = line.split("\t")[0]
        res = line.strip().split("\t")[1:]
        d[TID] = res

feas = ["RNA-seq", "ATAC", "RNAPII", "H3K27ac", "H3K4me1", "H3K4me3", "H3K9me3", "H3K27me3", "CTCF", "Smc1", "Smc3", "YY1", "Oct4", "Sox2", "Nanog", "mergeFeature"]

fea = "RNA-seq"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, d[TID][56]))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, d[TID][56]))

fea = "ATAC"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][0:4])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][0:4])))

fea = "RNAPII"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][4:8])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][4:8])))

fea = "H3K27ac"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][8:12])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][8:12])))

fea = "H3K4me1"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][12:16])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][12:16])))

fea = "H3K4me3"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][16:20])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][16:20])))

fea = "H3K9me3"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][20:24])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][20:24])))

fea = "H3K27me3"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][24:28])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][24:28])))

fea = "CTCF"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][28:32])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][28:32])))

fea = "Smc1"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][32:36])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][32:36])))

fea = "Smc3"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][36:40])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][36:40])))

fea = "YY1"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][40:44])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][40:44])))

fea = "Oct4"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][44:48])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][44:48])))

fea = "Sox2"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][48:52])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][48:52])))

fea = "Nanog"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][52:56])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID][52:56])))

fea = "mergeFeature"
for i in range(1, 101):
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/CV.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/CVinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID])))
    with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/Intest.txt" % i)as f:
        with open("/data3/pghzeng/self_renewal/Model/ML/all2/repeat/%s/%s/Intestinput.txt" % (i, fea), "w")as f1:
            lines = f.readlines()
            for line in lines:
                TID = line.split("\t")[0]
                status = line.split("\t")[1].strip()
                f1.write("%s\t%s\n" % (status, "\t".join(d[TID])))

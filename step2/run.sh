mkdir /data3/pghzeng/self_renewal/Model/ML/PHApply2/
mkdir /data3/pghzeng/self_renewal/Model/ML/PHApply2/train

# use juns

for i in $(seq 1 100)
do
perl a0_trainModel.pl $i
done

perl a4_merge_features.pl

for i in $(seq 1 100)
do
perl a5_testModel.pl $i
done

perl a6_ProbAvg.pl

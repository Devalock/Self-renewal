#for i in $(seq 1 100)
#do
#perl ./1_pos_neg.pl $i
#done
#
#for i in $(seq 1 100)
#do
#perl ./4_singleFeaturesForRNAtoLoop-gene-4cluster.pl $i
#done
#
#./CVs.py
#./CVs2.py  # use juns
#
for i in $(seq 1 100)
do
mv /data3/pghzeng/self_renewal/Model/ML/all2/repeat/$i/mergeFeature/CVroc.txt /data3/pghzeng/self_renewal/Model/ML/all2/repeat/$i/mergeFeature/CVrocRF.txt
mv /data3/pghzeng/self_renewal/Model/ML/all2/repeat/$i/mergeFeature/CVProb.txt /data3/pghzeng/self_renewal/Model/ML/all2/repeat/$i/mergeFeature/CVProbRF.txt 
done

perl 1_avg_diffenrent_MLmethods.pl #/data3/pghzeng/self_renewal/Model/ML/all2/repeat/ROC

for i in $(seq 1 100)
do
mv /data3/pghzeng/self_renewal/Model/ML/all2/repeat/$i/mergeFeature/CVrocRF.txt /data3/pghzeng/self_renewal/Model/ML/all2/repeat/$i/mergeFeature/CVroc.txt
mv /data3/pghzeng/self_renewal/Model/ML/all2/repeat/$i/mergeFeature/CVProbRF.txt /data3/pghzeng/self_renewal/Model/ML/all2/repeat/$i/mergeFeature/CVProb.txt
done
perl 3_avg_evaluation.pl


./4_singleFeaturesForRNAtoLoop-gene-4cluster.py
./stats.py
./stats2.py # use juns
./Intest.py
./Intest2.py # use juns

./avg_stats.py

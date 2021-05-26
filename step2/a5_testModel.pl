use warnings;
use strict;

my $abs1_dir="/data3/juns/phase/";
my $abs2_dir="/data3/pghzeng/self_renewal/Model/";
my $re=$ARGV[0];
my $python=$abs1_dir."program/PHApply/Intest-apply-test.py";

my $f1_dir=$abs2_dir."ML/PHApply2/train/$re/mergeFeature/";
my $f2_dir=$abs2_dir."ML/PHApply2/test/mergeFeature/";
system "python $python $f1_dir $f2_dir $re";
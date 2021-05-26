use warnings;
use strict;

my $abs_dir="/data3/pghzeng/self_renewal/Model/";
my $re=$ARGV[0];
my $model="mergeFeature";#mergeFeatureNew
my $dir=$abs_dir."ML/all2/repeat/$re/";

my $o_dir=$abs_dir."ML/PHApply2/train/$re/";
mkdir $o_dir;
my $train_dir=$o_dir."$model/";
mkdir $train_dir;

my %hash=();
my $n=0;
open(IN,"$dir"."CV.txt") or die "$!";
while (<IN>)
{
    chomp;
    $n++;
    $hash{$n}=$_;
}
close IN;

open(IN,"$dir"."Intest.txt") or die "$!";
while (<IN>)
{
    chomp;
    $n++;
    $hash{$n}=$_;
}
close IN;

open(OUT,">$train_dir"."list.txt") or die "$!";
foreach my $key (sort {$a<=>$b} keys %hash)
{
    print OUT $hash{$key},"\n";
}
close OUT;

open(OUT,">$train_dir"."CVinput.txt") or die "$!";
open(IN,"$dir"."$model/CVinput.txt") or die "$!";
while (<IN>)
{
    chomp;
    print OUT $_,"\n";
}
close IN;

open(IN,"$dir"."$model/Intestinput.txt") or die "$!";
while (<IN>)
{
    chomp;
    print OUT $_,"\n";
}
close IN;
close OUT;

my $python="/data3/juns/phase/program/PHApply/Intest-apply-train.py";
my $f_dir=$abs_dir."ML/PHApply2/train/$re/$model/";

system "python $python $f_dir";

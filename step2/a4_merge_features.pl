use warnings;
use strict;

my $abs_dir="/data3/pghzeng/self_renewal/Model/";
my $f_dir=$abs_dir."ML/PHApply2/test/";
mkdir $f_dir;
my $o_dir=$f_dir."mergeFeature/";
mkdir $o_dir;
my %hash=();

my $in_dir=$f_dir."mergeFeature/";
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";

open(FA, "/data3/pghzeng/self_renewal/Model/RawData/v3.final.selected_all_TID.signals.rm_loop.txt") or die "$!";
while (<FA>)
{
    chomp;
    s/\s+$//g;
    next if /^TID/;
    my @item=split/\s+/;
    my @ref=@item[1..$#item];
    print OUT "0\t",join "\t",@ref,"\n";
}
close FA;
close OUT;

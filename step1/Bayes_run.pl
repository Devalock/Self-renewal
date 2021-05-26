use warnings;
use strict;

my $abs_dir="/data3/pghzeng/self_renewal/Model/";
my $python="./Bayes.py";
my $fea=$ARGV[0];

for(my $re=1;$re<=100;$re++)
{
    my $out_dir=$abs_dir."ML/all2/repeat/$re/";
    my $o_dir=$out_dir."$fea/";
    system "python $python $o_dir";
}
print "$fea\tdone\n";


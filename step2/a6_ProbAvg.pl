use warnings;
use strict;

my $abs_dir="/data3/pghzeng/self_renewal/Model/";
my $out_dir=$abs_dir."ML/PHApply2/test/";
mkdir $out_dir;

open(IN,"/data3/pghzeng/self_renewal/Model/RawData/v3.final.selected_all_TID.signals.rm_loop.txt") or die "$!";
my $n=0;
my %tag=();
while (<IN>)
{
    chomp;
    next if /^TID/;
    $n++;
    my @item=split;
    $tag{$n}=$item[0];
}

close IN;

open(OUT,">$out_dir"."mergeFeature/InProbAVG.txt") or die "$!";
my %hash=();
for(my $i=1;$i<=100;$i++)
{
    open(IN,"$out_dir"."mergeFeature/InProbphase$i.txt") or die "$!";
    my $k=0;
    while (<IN>)
    {
        chomp;
        $k++;
        if (exists $hash{$k})
        {
            $hash{$k}+=$_;
        }else{
            $hash{$k}=$_;
        }
    }
    close IN;
}

#known
my %known=();
open(IN, "/data3/pghzeng/self_renewal/Model/RawData/v3.ESCAPE.TID.RPKM1.txt") or die "$!";
while (<IN>)
{
    chomp;
    $known{$_}++;
}
close IN;

foreach my $key (sort {$hash{$b}<=>$hash{$a}} keys %hash)
{
    my $prob=sprintf "%0.3f",$hash{$key}/100;
    if (exists $known{$tag{$key}})
    {
        
        print OUT $tag{$key},"\t$prob\tKnown\n";
    }else{
        print OUT $tag{$key},"\t$prob\tPredicted\n"
        
    }
    
    
}
close OUT;

use warnings;
use strict;

my $abs_dir="/data3/pghzeng/self_renewal/Model/";
my $o_dir=$abs_dir."ML/all2/repeat/ROC/";
mkdir $o_dir;
#my @method=qw(bayes LGBM Neural SVM XGboost);
my @method=qw(bayes LGBM Neural SVM RF);
open(O, ">$o_dir"."evaluation_difMethods.txt") or die "$!";
open(OU, ">$o_dir"."auc_difMethod.txt") or die "$!";
my %fea=();
my $count=100;
foreach my $fea (@method)
{
    my %hash=();
    my $auc=0;
    open(OUT, ">$o_dir"."$fea.txt") or die "$!";
    for (my $i=1;$i<=$count;$i++)
    {
        my $work_dir=$abs_dir."ML/all2/repeat/$i/mergeFeature/";
        print "$fea\t$work_dir\n";
        open(IN,"$work_dir"."CVroc$fea.txt") or die "$!";
        my $n=0;
        while (<IN>)
        {
            chomp;
            my @item=split/\t/;
            $n++;
            if ($n<102)
            {
                if (exists $hash{$item[0]})
                {
                    my @ref=@{$hash{$item[0]}};
                    for(my $j=0;$j<@ref;$j++)
                    {
                        $ref[$j]+=$item[$j+1];
                    }
                    $hash{$item[0]}=\@ref;
                }else{
                    my @ref=@item[1..$#item];
                    $hash{$item[0]}=\@ref;
                }
            }else{
                s/\s+//g;
               $auc+=$_;
               if (exists $fea{$fea})
               {
                   my @ref=@{$fea{$fea}};
                   push(@ref,$_);
                   $fea{$fea}=\@ref;
               }else{
                   my @ref=();
                   push(@ref,$_);
                   $fea{$fea}=\@ref;
               }
               
            }
        }
        close IN;
    }
    my $avg=sprintf "%0.3f",$auc/$count;
    foreach my $key (sort {$a<=>$b} keys %hash)
    {
        my @ref=@{$hash{$key}};
        for(my $i=0;$i<@ref;$i++)
        {
            $ref[$i]=sprintf "%0.3f",$ref[$i]/$count;
        }
        print OUT $key,"\t",join("\t",@ref),"\n";
        if ($key==0.50)
        {
            print O $fea,"\t",$key,"\t",join("\t",@ref),"\t$avg\n";
        }
        
    }
    print OUT $avg,"\n";
    close OUT;
}
close O;

foreach my $key (keys %fea)
{
    my @ref=@{$fea{$key}};
    print OU $key,"\t",join("\t",@ref),"\n";
}
close OU;

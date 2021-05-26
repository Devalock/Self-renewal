use warnings;
use strict;
use List::Util qw(shuffle);

my $abs_dir="/data3/pghzeng/self_renewal/Model/";
my $data_dir=$abs_dir."RawData/";
my $out_dir=$abs_dir."ML/all2/";
mkdir $out_dir;

my $re=$ARGV[0];
my $new_dir=$out_dir."repeat/";
mkdir $new_dir;
$new_dir=$out_dir."repeat/$re/";
mkdir $new_dir;

my @pos=();
my %raw=();
open(OUT,">$new_dir"."pos.txt") or die "$!";
open(FA, "$data_dir".""."v3.ESCAPE.TID.RPKM1.txt") or die "$!";
while (<FA>)
{
    chomp;
    print OUT $_,"\n";
    push(@pos,$_) unless $_~~ @pos;
    $raw{$_}++;
}
close FA;
close OUT;
my $pos_num=scalar @pos;
print $pos_num,"\tpos_num\n";
my @human=();
open(FA, "$data_dir"."total.txt") or die "$!";
while (<FA>)
{
    chomp;
    push(@human,$_);
}
close FA;

my $c=0;
my %check=();
my @neg=();
open(OUT,">$new_dir"."neg.txt") or die "$!";
while (1)
{
    my $neg=&ranP(\@human);
    next if exists $raw{$neg};
    next if exists $check{$neg};
    push(@neg,$neg);
    print OUT $neg,"\n";
    $c++;
    $check{$neg}++;
    last if $c == $pos_num;
}
close OUT;
my $neg_num=scalar @neg;
print $neg_num,"\tneg_num\n";
#30 independent dataset, 70 train
@pos=shuffle @pos;
@neg=shuffle @neg;
my @trainp=@pos[0..int(0.7* scalar @pos)];
my @trainn=@neg[0..int(0.7* scalar @neg)];
my @indp=@pos[(int(0.7* scalar @pos)+1)..$#pos];
my @indn=@neg[(int(0.7* scalar @neg)+1)..$#neg];
open(OUT, ">$new_dir"."CV.txt") or die "$!";
foreach my $t (@trainp)
{
    print OUT $t,"\t1\n";
}

foreach my $t (@trainn)
{
    print OUT $t,"\t0\n";
}
close OUT;

open(OUT, ">$new_dir"."Intest.txt") or die "$!";
foreach my $t (@indp)
{
    print OUT $t,"\t1\n";
}

foreach my $t (@indn)
{
    print OUT $t,"\t0\n";
}
close OUT;
#close OU;

sub ranP
{
    my $path=$_[0];
    my @p=@{$path};
    my $n=scalar @p;
    my $m=int (rand($n));
    my $ranP=$p[$m];
    return $ranP;
}

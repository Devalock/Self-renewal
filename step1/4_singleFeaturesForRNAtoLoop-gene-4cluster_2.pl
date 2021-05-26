use warnings;
use strict;

my $abs_dir="/data3/pghzeng/self_renewal/Model/";
my $data_dir=$abs_dir."RawData/";
my $re=$ARGV[0];
my $out_dir=$abs_dir."ML/all2/repeat/$re/";

my %class=(
            "C"=>"1","L"=>"1","V"=>"1","I"=>"1","M"=>"1","F"=>"1","W"=>"1",
            "G"=>"2","A"=>"2","S"=>"2","T"=>"2","P"=>"2","H"=>"2","Y"=>"2",
            "R"=>"3","K"=>"3","E"=>"3","D"=>"3","Q"=>"3","N"=>"3"
           );
my $f_dir=$out_dir;
my %hash=();
open(IN,"$data_dir"."v3.final.selected_all_TID.signals.rm_loop.txt") or die "$!";
while (<IN>)
{
    chomp;
    my @item=split;
    my @ref=@item[1..$#item];
    $hash{$item[0]}=\@ref;
}
close IN;

my $o_dir=$f_dir."RNA-seq/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=($ref[57]);
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=($ref[57]);
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;

$o_dir=$f_dir."ATAC/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[1..4];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[1..4];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;


$o_dir=$f_dir."RNAPII/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[5..8];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[5..8];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;


$o_dir=$f_dir."H3K27ac/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[9..12];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[9..12];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;


$o_dir=$f_dir."H3K4me1/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[13..16];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[13..16];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;


$o_dir=$f_dir."H3K4me3/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[17..20];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[17..20];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;


$o_dir=$f_dir."H3K9me3/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[21..24];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[21..24];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;


$o_dir=$f_dir."H3K27me3/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[25..28];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[25..28];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;


$o_dir=$f_dir."CTCF/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[29..32];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[29..32];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;


$o_dir=$f_dir."Smc1/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[33..36];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[33..36];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;



$o_dir=$f_dir."Smc3/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[37..40];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[37..40];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;


$o_dir=$f_dir."YY1/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[41..44];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[41..44];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;

$o_dir=$f_dir."Oct4/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[45..48];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[45..48];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;

$o_dir=$f_dir."Sox2/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[49..52];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[49..52];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;


$o_dir=$f_dir."Nanog/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[53..56];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[53..56];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;


$o_dir=$f_dir."mergeFeature/";
mkdir $o_dir;
open(OUT, ">$o_dir"."CVinput.txt") or die "$!";
open(FA, "$f_dir"."CV.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[1..57];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close FA;
close OUT;
open(OUT, ">$o_dir"."Intestinput.txt") or die "$!";
open(FA, "$f_dir"."Intest.txt") or die "$!";
while (<FA>)
{
    chomp;
    my ($uni,$tag)=split/\s+/,$_;
    if (exists $hash{$uni})
    {
        my @ref=@{$hash{$uni}};
        my @vec=@ref[1..57];
        print OUT $uni,"\t",join("\t",@vec),"\n";
    }
}
close OUT;
close IN;




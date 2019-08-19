open (IN,"<",$ARGV[0]);
my %count;
while (<IN>){
	chomp $_;
	($chr, $str, $end, $class)= split("\t",$_);
	($name, $chrN)= split("_", $chr);
	foreach $class ($class){
	$count{$class}++;
	}
}

print "$name\tcount\n";

foreach my $class (sort keys %count) {
    print "$class\t$count{$class}\n";
}

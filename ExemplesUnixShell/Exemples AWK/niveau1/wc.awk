#!/usr/bin/awk -f

BEGIN \
{
	print "démarrage"
}


{
	chars += length($0) + 1  # add one for the \n
	words += NF
}

END \
{
	print NR, words, chars
	print "fin"
}

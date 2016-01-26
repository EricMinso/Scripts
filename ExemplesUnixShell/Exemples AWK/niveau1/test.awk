#!/usr/bin/awk -f

BEGIN \
{
	print "démarrage"
}


{
	print"- NR : ", NR, " - NF : ", NF, $0
}

END \
{
	
	print "fin"
}

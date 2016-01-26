#!/usr/bin/awk -f

BEGIN \
{
    print "démarrage"
    #FS = "0"
    #OFS = "@"
}


NR == 6, NR == 7 \
{
	for( a = 1 ; a < NF ; a++ )
	{
		print "#",$a,"#"
	}
}

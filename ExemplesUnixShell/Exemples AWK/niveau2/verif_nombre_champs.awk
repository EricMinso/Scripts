#!/usr/bin/awk -f

BEGIN \
{
    nombre_de_champs = 0
    #FS = "0"
    #OFS = "@"
}



{
	if( NF != nombre_de_champs )
	{
		print "Ligne", NR, "le nombre de champs passe de",nombre_de_champs,"à",NF 
		nombre_de_champs = NF
	}
}

#!/usr/bin/awk -f

BEGIN \
{
	#print "ARGC : ", ARGC

	#print "ARGV[0] :", ARGV[0]
	#print "ARGV[1] :", ARGV[1]
	#print "ARGV[2] :", ARGV[2]
	
	if( ARGC != 3 || ARGV[2] < 1 )
	{
		print "\nFormat incorrect.\nSyntaxe : ./lignes_possedant_n_champs.awk [nom_fichier] [nombre_de champs]"
		exit
	}
	
	nombre_de_champs = ARGV[2]
}


NF == nombre_de_champs \
{
	print "ligne",NR,":",$0
}

#!/usr/bin/awk -f

BEGIN \
{
	#print "ARGC : ", ARGC

	#print "ARGV[0] :", ARGV[0]
	#print "ARGV[1] :", ARGV[1]
	#print "ARGV[2] :", ARGV[2]
	
	if( ARGC != 3 || ARGV[2] < 1 )
	{
		print "\nFormat incorrect.\nSyntaxe : ./details_champs_ligne_n.awk [nom_fichier] [numero_de_ligne]"
		exit
	}
	
	numero_de_ligne = ARGV[2]
}


NR == numero_de_ligne \
{
	print "Détails Ligne", NR, "-", NF, "champs"
	
	for( a = 1; a <= NF; a++ )
	{
		print "champ", a,": >", $a, "<"
	}
}

#!/usr/bin/awk -f

# Usage ./renommage_droits <table_de_correspondance> <fichier_entrée>


# Eric Minso
# Société VIA2S
# sept/oct 2008


BEGIN \
{
	FS = ",";
	OFS = ",";
	
	if( ARGC != 3 )
	{
		print "Usage : ./renommage_droits <table_de_correspondance> <fichier_entrée>";
		exit;
	}
	
	table_de_correspondance[0] = 0;
}


{
	if( length( nom_premier_fichier ) == 0 )
	{
		nom_premier_fichier = "" FILENAME;
	}
	
	# Chargement de la table de correspondances
	if( 0 != match( nom_premier_fichier, FILENAME ))
	{
		table_de_correspondance[ $1 ] = $2;
	}
	# Remplacement des occurrences dans le second fichier
	else
	{
		for( i in table_de_correspondance )
		{
			sub( i, table_de_correspondance[ i ], $0 );
		}
		
		print $0;
	}
}



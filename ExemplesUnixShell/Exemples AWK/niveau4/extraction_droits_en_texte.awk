#!/usr/bin/awk -f

# Extrait les droits d'accès depuis un fichier EPR
# et crée un fichier CSV de deux colonnes :
# Numéro de badge, Nom de droit (généré à partir de l'ID Micro et de l'ID droit).


# Eric Minso
# Société VIA2S
# sept/oct 2008

BEGIN \
{
	etat = 0;
	badge = "";
	#tableau[ 0 ][ 0 ][ 0 ] = 0
	OFS = ",";
	flag_erreur = 0;
}



function parse_champs_de_bits( id_micro, str_droits )
{
	# Première apparition de "V"
	indexOfV = index( str_droits, "V" ) - 1;
	
	
	while( indexOfV != -1 )
	{
		# Affiche la correspondance
		print badge, "Micro_" id_micro "_Droit_" indexOfV
		
		# La fonction index ne permet pas de spécifier un indice de départ
		# donc il faut retirer la partie de la chaîne déjà reconnue
		sub( "V", ".", str_droits );
		indexOfV = index( str_droits, "V" ) - 1;
	}
}



# Ligne d'identité 1
$1 ~ /^[0-9][0-9]+[0-9]$/ \
{
	#print "Ligne d'identité 1";
	etat = 1;
	badge = $1;
}


# Ligne d'identité 2
$1 ~ /^[0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/ \
{
	if( etat == 1 )
	{
		etat = 2;
	}
	else
	{
		print "L" NR " : Erreur token <identité 2>";
		flag_erreur ++;
		etat = 0;
	}
}


# Ligne de droit
#$1 ~ /^[0-9][0-9]$/		&& 
#$2 ~ /^[.V]+$/			&&
#$3 ~ /^[0-9][0-9]$/		&&
#$4 ~ /^[.V]+$/ \


# Ligne de droits vides : ignorer
#$2 ~ /^[.]+$/ ||
#$4 ~ /^[.]+$/ \
#{}

# Ligne de droits non vide 1
$1 ~ /^[0-9][0-9]$/		&& 
$2 ~ /V/ \
{
	if( etat == 2 )
	{
		parse_champs_de_bits( $1, $2 );
	}
	else
	{
		print "L" NR " : Erreur token <droits 1>";
		flag_erreur ++;
		etat = 0;
	}
}


# Ligne de droits non vide 2
$3 ~ /^[0-9][0-9]$/		&& 
$4 ~ /V/ \
{
	if( etat == 2 )
	{
		parse_champs_de_bits( $3, $4 );
	}
	else
	{
		print "L" NR " : Erreur token <droits 2>";
		flag_erreur ++;
		etat = 0;
	}
}


END \
{
	if( flag_erreur > 0 )
	{
		print flag_erreur " erreurs survenues.";
	}
}

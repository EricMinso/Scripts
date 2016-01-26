#!/usr/bin/awk -f

# Extrait les droits d'acc�s depuis un fichier EPR
# et cr�e un fichier CSV de deux colonnes :
# Num�ro de badge, Nom de droit (g�n�r� � partir de l'ID Micro et de l'ID droit).


# Eric Minso
# Soci�t� VIA2S
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
	# Premi�re apparition de "V"
	indexOfV = index( str_droits, "V" ) - 1;
	
	
	while( indexOfV != -1 )
	{
		# Affiche la correspondance
		print badge, "Micro_" id_micro "_Droit_" indexOfV
		
		# La fonction index ne permet pas de sp�cifier un indice de d�part
		# donc il faut retirer la partie de la cha�ne d�j� reconnue
		sub( "V", ".", str_droits );
		indexOfV = index( str_droits, "V" ) - 1;
	}
}



# Ligne d'identit� 1
$1 ~ /^[0-9][0-9]+[0-9]$/ \
{
	#print "Ligne d'identit� 1";
	etat = 1;
	badge = $1;
}


# Ligne d'identit� 2
$1 ~ /^[0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/ \
{
	if( etat == 1 )
	{
		etat = 2;
	}
	else
	{
		print "L" NR " : Erreur token <identit� 2>";
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

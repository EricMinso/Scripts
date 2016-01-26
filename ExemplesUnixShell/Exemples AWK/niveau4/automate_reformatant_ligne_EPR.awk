#!/usr/bin/awk -f

# Etape 1

# Génère un fichier où chaque ligne correspond à un enregistrement
# à partir d'un fichier source .EPR où les enregistrements sont sur deux lignes

# Devra être suivi de l'étape 2 - script "automate_creant_fichier_csv_correct.awk"

# Eric Minso
# Société VIA2S
# mai 2008

BEGIN \
{
	etat = 0
	derniere_ligne = ""
}

# Cas d'une ligne incorrecte
$1 !~ /^[0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/ && $1 !~ /^[0-9]+[0-9]$/ \
{
	#if( etat == 0 || etat == 2)
	#{
		etat = 0
		derniere_ligne = ""
	#}
	#else
	#{
	#	print "ligne", NR, "etat = ", etat, "état incorrect (attendu: 0 ou 2)"
	#	exit
	#}
}

# Cas d'une première partie de ligne : mémoriser
$1 ~ /^[0-9][0-9]$/  \
{
	etat = 0
	derniere_ligne = ""
}

# Cas d'une première partie de ligne : mémoriser
$1 ~ /^[0-9]+[0-9]$/ \
{
	if( etat == 0 || etat == 2)
	{
		etat = 1
		derniere_ligne = $0
		gsub("['\r','\n']","",derniere_ligne)
	}
	else
	{
		print "ligne", NR, "etat = ", etat, "état incorrect (attendu: 0 ou 2)"
		exit
	}
}


# Cas d'une seconde partie de ligne : restituer
$1 ~ /^[0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/ \
{
	if( etat == 1 )
	{
		etat = 2
		gsub("['\r','\n']","",$0)
		print derniere_ligne,$0
	}
	else
	{
		print "ligne", NR, "etat = ", etat, "état incorrect (attendu: 1)"
		exit
	}
}



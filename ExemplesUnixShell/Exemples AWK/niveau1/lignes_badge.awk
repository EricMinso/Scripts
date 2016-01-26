#!/usr/bin/awk -f

BEGIN \
{
	etat = 0
	derniere_ligne = ""
}

# Cas d'une ligne incorrecte
$1 !~ /^[0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/ && $1 !~ /^[0-9]+[0-9]$/ \
{
	if( etat == 0 || etat == 2)
	{
		etat = 0
		derniere_ligne = ""
	}
	else
	{
		print "etat = ", etat, "état incorrect (attendu: 0 ou 2)"
		exit
	}
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
		print "etat = ", etat, "état incorrect (attendu: 0 ou 2)"
		exit
	}
}


# Cas d'une seconde partie de ligne : restituer
$1 ~ /^[0-9][0-9]-[0-9][0-9]-[0-9][0-9]$/ \
{
	if( etat == 1 )
	{
		etat = 2
		print derniere_ligne,$0
	}
	else
	{
		print "etat = ", etat, "état incorrect (attendu: 1)"
		exit
	}
}



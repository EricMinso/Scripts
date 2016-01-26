#!/bin/ksh

#if [ $# != 1 ];
#then
#	echo "Global.sh : Manque Parametre 1 : nom du fichier";
#	exit;
#fi

echo "Global.sh : debut"

for fichier_badge in `ls f_badge*`
do

	echo "Parsage de $fichier_badge"

	# Parsage par AWK
	cat $fichier_badge | awk \
	'BEGIN \
	{
		FS = "|"
		print "AWK depuis Global.sh : debut"
		lignes_ignorees = 0
		lignes_erronees = 0
	}
	
	NF < 77 \
	{
		print "ignore " NR " - " NF
		lignes_ignorees += 1
		next
	}
	
	NF > 78 \
	{
		print "erronee " NR " - " NF
		lignes_erronees += 1
		next
	}
	
	NF == 77 || NF == 78 \
	{
		listeDesArguments=""
		
		# Ajout de quotes à chaque argument
		for( i=1; i<=NF; i++ )
		{
			listeDesArguments=listeDesArguments " \"" $i "\""
		}
		
		commande="./ligne.sh " listeDesArguments
		print "AWK depuis Global.sh : appel de " commande " - " listeDesArguments;
		
		# Appel du script "ligne"	
		system( commande );
	}
	
	END \
	{
		print "lignes ignorees : " lignes_ignorees
		print "lignes erronees : " lignes_erronees
	}'

	mkdir ./archive
	mv ./$fichier_badge ./archive/$fichier_badge
done


echo "Global.sh : fin"



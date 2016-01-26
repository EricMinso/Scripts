#!/bin/bash
# Eric MINSO (EM22AEEN) - 20 Mai 2015

# Caractère(s) à supprimer / caractères de remplacement
# (paramètres de la commande tr
CARACTERES_A_SUPPRIMER="'-."
CARACTERES_DE_REMPLACEMENT="_"

# Fonction qui transforme un chemin relatif en chemin absolu
get_absolute_path()
{
	# $1 : relative path
	if [ -d $( dirname "$1" ) ]; then
		echo "$(cd "$(dirname "$1")" && pwd)/$(basename "$1")"
	fi
}


# Début du script principal
echo
echo "Ce script renomme les répertoires SVN de la base ANR "
echo "pour les rendre compatibles avec Python Nose Test"
echo


# Chemin complet
chemin_absolu=$( pwd )
echo "Répertoire courant : $chemin_absolu "

# Etape 1 - vérifier qu'on se trouve dans un dépôt SVN valide
# Regarder si 'svn status' écrit sur stderr (c'est le cas si on n'est pas dans un dépôt SVN valide)
SVN_ERROR_STATUS=`svn status 2>&1 1>/dev/null`

# Erreur SVN : on quitte
if [ -n "$SVN_ERROR_STATUS" ];
then
	echo "Erreur: $SVN_ERROR_STATUS"
	exit 1
fi

# Recherche des répertoires dont le nom contient un '.', à l'exception des .svn
# puis inversion de la liste des résultats pour travailler d'abord sur les répertoires de plus grande profondeur
for resultat in `find $chemin_absolu -type d -print | grep -v -e ".svn" | tac`
do
	echo "# Traitons : $resultat"

	# Nom du répertoire seul
	nom_repertoire=$( basename $resultat )

	# On remplace . par _
	nouveau_nom=`echo $nom_repertoire| tr "$CARACTERES_A_SUPPRIMER" "$CARACTERES_DE_REMPLACEMENT"`

	# On recrée le nouveau chemin absolu
	nouveau_chemin_absolu=`echo $resultat | sed -e "s/$nom_repertoire/$nouveau_nom/"`

	# On renomme
	svn move "$resultat" "$nouveau_chemin_absolu"
	echo "# Renommé  : $nouveau_chemin_absolu"

done

echo "Pour valider les changements, tapez 'svn commit -m \"Conversion des noms de répertoire\"' "
echo "Pour annuler les changements, tapez 'svn revert --depth=infinity $chemin_absolu' "



#!/usr/bin/awk -f

# Etape 2

# A partir d'un fichier généré lors de l'étape 1 par le script "automate_reformatant_ligne_EPR.awk"
# parse le document pour en extraire : le n° de badge, le n° d'employé, le nom et prénom, la date d'émission et d'expiration

# Ce code se base sur le document "description_automate.odp" dans le même répertoire

# Eric Minso
# Société VIA2S
# mai 2008

BEGIN \
{
	etat = 1
	FS = "\t"
	OFS = ""
	indice_lignes_rejetees = 0
}



{
	etat = 1
	ligne_sortie = "" NR ","
	token = ""
	
	
	# On va faire une boucle qui récupère les tokens de la ligne,
	# d'abord selon les tabulations
	for( a = 1; a < NF; a++ )
	{
		flag_next_line = 0
		flag_concatener_sous_tokens = 0

		nb_tokens = split( $a, array, " " )
		
		# puis ensuite selon les espaces
		for( b=1; b<=nb_tokens; b++ )
		{
			token = array[b]
			flag_token_consumed = 0
			
			# Token "Numéro de badge"
			if( etat == 1 && flag_token_consumed == 0 )
			{
				if( match( token, "^[0-9]+$" ))
				{
					ligne_sortie = ligne_sortie token
					flag_token_consumed = 1
					etat = 2
				}
				else
				{
					lignes_rejetees[ indice_lignes_rejetees++ ] = "l" NR " (etat 1) Erreur token " b "/" nb_tokens " <" token "> dans " $0

					flag_next_line = 1
					break
				}
			}
			
			# Token "Numéro d'employé" (peut être vide)
			if( etat == 2 && flag_token_consumed == 0 )
			{
				ligne_sortie = ligne_sortie ","
				etat = 3
				
				if( match( token, "^[0-9]+$" ))
				{
					 ligne_sortie = ligne_sortie token
					 flag_token_consumed = 1
				}
				#else if( match( token, "^.+$" ))
				#{
				#	lignes_rejetees[ indice_lignes_rejetees++ ] = "l" NR " : (etat 2) Erreur token " b "/" nb_tokens " <" token "> dans " $0

				#	flag_next_line = 1
				#	break
				#}
			}
			# Token "Nom de famille" et "Prénom"
			# (peut comprendre plusieurs tokens séparés par des espaces, peut-être optionnel)
			if(( etat == 3 || etat == 4 ) && flag_token_consumed == 0 )
			{
				if( match( token, "^[^0-9]" ) )
				{
					# Premier sous-token
					if( flag_concatener_sous_tokens == 0 )
					{
						ligne_sortie = ligne_sortie "," token
						flag_concatener_sous_tokens = 1
						flag_token_consumed = 1
					}
					# Concaténation des autres sous-tokens
					else
					{
						ligne_sortie = ligne_sortie " " token
						flag_token_consumed = 1
					}
				}
				else
				{
					lignes_rejetees[ indice_lignes_rejetees++ ] = "l" NR " : (etat " etat ") Erreur token " b "/" nb_tokens " <" token "> dans " $0
					flag_next_line = 1
					break
				}

				
				# Fin des sous-tokens
				if( b >= nb_tokens )
				{
					etat ++
					
					# Pour mettre une virgule même si le champ est vide
					if( flag_token_consumed == 0 )
					{
						ligne_sortie = ligne_sortie ","  
					}
				}
			}
			# Token Lettres (ignorés)
			if( etat == 5  && flag_token_consumed == 0 )
			{
				# On ignore les tokens lettres situées entre le token précédent et le token courant
				if( match( token, "^[a-zA-Z]+$" ) )
				{
					flag_token_consumed = 1
				}
				else if( match( token, "^[0-9][0-9]-[0-9][0-9]-[0-9][0-9]$" ) )
				{
					# On ne passe à l'état suivant qu'une fois toutes les lettres consommées
					etat ++
				}
				else
				{
					lignes_rejetees[ indice_lignes_rejetees++ ] = "l" NR " (etat 5) Erreur token " b "/" nb_tokens " <" token "> dans " $0
				}
			}
			
			# Token Date d'émission et token date d'expiration
			if(( etat == 6 || etat == 7 ) && flag_token_consumed == 0 )
			{
				if( match( token, "^[0-9][0-9]-[0-9][0-9]-[0-9][0-9]$" ) )
				{
					ligne_sortie = ligne_sortie "," token
					flag_token_consumed = 1
					etat ++ 
				}
				else
				{
					lignes_rejetees[ indice_lignes_rejetees++ ] = "l" NR " (etat " etat ") Erreur token " b "/" nb_tokens " <" token "> dans " $0

					flag_next_line = 1
					break
				}
			}
			# Les autres tokens sont cordialement ignorés
			
			#if( flag_token_consumed == 0 )
			#	lignes_rejetees[ indice_lignes_rejetees++ ] = "l" NR " : Token non consommé <" token "> dans " $0
		}
		
		if( flag_next_line == 1 )
			break
	}
	
	if( etat == 8 )
	{
		# Ligne correctement parsée
		print ligne_sortie
	}
	else
	{
		# Ligne incorrectement parsée
		lignes_rejetees[ indice_lignes_rejetees++ ] = "l" NR " : <blocage etat " etat "> - " $0 " - ligne incomplètement parsée : " ligne_sortie
	}
	
}


END \
{
	print indice_lignes_rejetees " lignes rejetées : "
	
	# for( a in lignes_rejetees )
	# {
	# 	print lignes_rejetees[ a ]
	# }
	for( a=0; a<indice_lignes_rejetees; a++ )
	{
		print lignes_rejetees[ a ]
	}
}

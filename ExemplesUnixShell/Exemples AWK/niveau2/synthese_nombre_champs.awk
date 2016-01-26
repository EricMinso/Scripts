#!/usr/bin/awk -f

BEGIN \
{
	indice_min = 10000
	indice_max = 0
}



{
	if( NF < indice_min )
		indice_min = NF
	
	if( NF > indice_max )
		indice_max = NF
	
	tableau_d_indices[ NF ] ++

}


END \
{
	print "Nombre de champs min : ", indice_min
	print "Nombre de champs max : ", indice_max
	
	for( a=indice_min; a<=indice_max; a++ )
	{
		if( tableau_d_indices[ a ] > 0 )
			print "Lignes de",a,"champs :", tableau_d_indices[ a ], "occurrences"
	}
}

#!/usr/bin/env python

def compteVrais( *liste ):
	compte = 0

	for i in liste:
		if i:
			compte += 1

	return compte


plageValeurs = ( True, False )

print( "XOR - 2 opérandes" )

for a in plageValeurs:
	for b in plageValeurs:
		print( "%s ^ %s = %s"%( a, b, a^b ) )

print( "\nXOR - 3 opérandes" )

for a in plageValeurs:
	for b in plageValeurs:
		for c in plageValeurs:
			nbVrais = compteVrais( a, b, c )
			print( "%d vrais = %s = (%s ^ %s ^ %s) "%( nbVrais, a^b^c, a, b, c ) )

print( "\nXOR - 4 opérandes" )

for a in plageValeurs:
	for b in plageValeurs:
		for c in plageValeurs:
			for d in plageValeurs:
				nbVrais = compteVrais( a, b, c, d )
				print( "%d vrais = %s = (%s ^ %s ^ %s ^ %s)"%( nbVrais, a^b^c^d, a, b, c, d ) )







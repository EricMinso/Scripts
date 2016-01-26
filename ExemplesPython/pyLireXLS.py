#!/usr/bin/env python

# Bibliothèques officielles 
import argparse
import os
import sys

import openpyxl


"""
Point d'entrée
"""
def main( args ):

    ## Parsage des arguments ##
    parser = argparse.ArgumentParser( description='Fonction MAIN' )
    parser.add_argument( '-f', '--fichier', required=True, help='(*REQUIS*) Le fichier XLS' )
    parser.add_argument( '-p', '--page',    required=True, help='(*REQUIS*) L\'onglet à lire' )
    parser.add_argument( '-c', '--cellule', required=True, help='(*REQUIS*) La cellule à lire' )
    arguments = parser.parse_args()

    # Le fichier n'existe pas
    if not os.path.exists( arguments.fichier ):
        raise OSError( "Le fichier '%s' n'existe pas" %( arguments.fichier ))
        return

    classeurData = openpyxl.load_workbook( filename=arguments.fichier, read_only=True, use_iterators=False, keep_vba=False, data_only=True )
    feuille = classeurData[ arguments.page ]
    cellule = feuille[ arguments.cellule ]
    
    print( cellule.value )
    
        

"""
Point d'entrée
"""
# Execute la fonction main, seulement si le script est appelé directement, et non pas depuis un autre script
if( __name__ == "__main__" ):
    main( sys.argv )

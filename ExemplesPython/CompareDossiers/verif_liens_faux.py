
import os, sys



if len(sys.argv) == 2:

    fichier = open( sys.argv[1], "r" )
    tableau = fichier.readlines()


    for lien in tableau:

        lien_epure = lien.strip().replace( "\r\n", "" )

        if len(lien_epure) > 2 and not os.path.isfile( lien_epure ) and not os.path.isdir( lien_epure ):
            print lien_epure



else:
    print "Usage: verif_liens_faux.py [fichier_contenant_les_liens]"



import os, sys



if len(sys.argv) == 2:

    fichier = open( sys.argv[1], "r" )
    tableau = fichier.readlines()


    for lien in tableau:

        lien_epure = lien.strip().replace( "\r\n", "" )

        if os.path.isfile( lien_epure ):
            print "Fichier:\t\"" + lien_epure + "\""
        elif os.path.isdir( lien_epure ):
            print "Dossier:\t\"" + lien_epure + "\""
        else:
            print "Erreur:\t\"" + lien_epure + "\""



else:
    print "Usage: infos_liens.py [fichier_contenant_les_liens]"


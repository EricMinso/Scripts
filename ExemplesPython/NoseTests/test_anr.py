#!/usr/bin/env python

from configuration import *
import os, os.path
import subprocess

config = None
logger = None
dossierTravail = None


class SilentWrap():
    
    def __init__(self, objet):
        self.objet = objet
    
    def __str__(self):
        return ""
    
    def __repr__(self):
        return ""
    
    def get(self):
        return self.objet


def setup_module(module):
    """ Méthode que Nose Test exécute avant le début des tests """
    global config
    global logger 
    global dossierTravail

    config = ConfigurationDesTests.getInstance()
    logger = ConfigurationDuLog.getLogger( __name__ )
    
    # Récupération du répertoire courant d'après le nom du fichier code source python actuel
    dossierTravail = os.path.dirname( __file__ )
    
    logger.info( "# Démarrage du %s"%module )
    logger.info( "# Dossier Travail = %s"%dossierTravail )


def teardown_module(module):
    """ Méthode que Nose Test exécute après la fin des tests """
    logger.info( "# Fin du %s"%str( module ))
    logger.info( " - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -" )


def test_traitement_repertoire():
    fichier = ""
    try:
        dossierRésultatREF = config.getDossierRésultatREF()
        dossierRésultatTEST = config.getDossierRésultatTEST()

        assert dossierTravail
        assert dossierRésultatREF 
        assert dossierRésultatTEST 

        if not os.path.exists( dossierRésultatREF ):  os.makedirs( dossierRésultatREF )
        if not os.path.exists( dossierRésultatTEST ): os.makedirs( dossierRésultatTEST )

        assert os.path.exists( dossierRésultatREF )
        assert os.path.exists( dossierRésultatTEST )

        for fichier in os.listdir( dossierTravail ):
            if os.path.isfile( dossierTravail + os.sep + fichier ) and fichier.endswith( ".xlsx" ):
                logger.debug( "Traitement : %s"%fichier )
                
                with open( dossierTravail + os.sep + "output.txt" , mode='a') as standardOutputFile:
                    
                    standardOutputFile.__repr__ = lambda x: ""
                    standardOutputFile.__str__ = lambda x: ""
                    
                    yield check_construction_donneeslogo_ref, fichier, SilentWrap(standardOutputFile)
                    yield check_construction_donneeslogo_tst, fichier, SilentWrap(standardOutputFile)
                    yield check_optimisation_ref, SilentWrap(standardOutputFile)
                    yield check_optimisation_tst, SilentWrap(standardOutputFile)
                    yield check_diff_resultats

    except Exception as e:
        logger.error( "Erreur test_traitement_repertoire ! %s: %s"%( type(e), e ))
        logger.error( "Fichier %s"%fichier )
        raise e


def check_construction_donneeslogo_ref( fichier, wrapStandardOutputFile ):
    try:
        logger.debug( "Construction Données Logo Reference pour %s"%str( fichier ))
        
        standardOutputFile = wrapStandardOutputFile.get()
        assert standardOutputFile
        assert fichier
        assert dossierTravail

        ligneCmd = config.getLigneCommandeCréationDonnéesLogoREF(
            nomFichierDataXLS = fichier,
            nomDossierTravail = dossierTravail
        )

        logger.debug( "Ligne de commande : %s"%str( ligneCmd ))
        assert ligneCmd 

        subprocess.call( ligneCmd, stdout=standardOutputFile, stderr=standardOutputFile )

    except Exception as e:
        logger.error( "Erreur check_construction_donneeslogo_ref ! %s: %s"%( type(e), e ))
        raise e


def check_construction_donneeslogo_tst( fichier, wrapStandardOutputFile ):
    try:
        logger.debug( "Construction Données Logo Test pour %s"%str( fichier ))
        
        standardOutputFile = wrapStandardOutputFile.get()
        assert standardOutputFile
        assert fichier
        assert dossierTravail

        ligneCmd = config.getLigneCommandeCréationDonnéesLogoTEST(
            nomFichierDataXLS = fichier,
            nomDossierTravail = dossierTravail
        )

        logger.debug( "Ligne de commande : %s"%str( ligneCmd ))
        assert ligneCmd 

        subprocess.call( ligneCmd, stdout=standardOutputFile, stderr=standardOutputFile )

    except Exception as e:
        logger.error( "Erreur check_construction_donneeslogo_tst ! %s: %s"%( type(e), e ))
        raise e


def check_optimisation_ref( wrapStandardOutputFile ):
    try:
        logger.debug( "Exécution Optimisation Reference =  %s"%str( dossierTravail ))
        
        standardOutputFile = wrapStandardOutputFile.get()
        assert standardOutputFile
        assert dossierTravail

        ligneCmd = config.getLigneCommandeExécutionOptimisationREF( nomDossierTravail = dossierTravail )

        logger.debug( "Ligne de commande : %s"%str( ligneCmd ))
        assert ligneCmd 

        subprocess.call( ligneCmd, stdout=standardOutputFile, stderr=standardOutputFile )

    except Exception as e:
        logger.error( "Erreur check_optimisation_ref ! %s: %s"%( type(e), e ))
        raise e


def check_optimisation_tst( wrapStandardOutputFile ):
    try:
        logger.debug( "Exécution Optimisation Test =  %s"%str( dossierTravail ))
        
        standardOutputFile = wrapStandardOutputFile.get()
        assert standardOutputFile
        assert dossierTravail

        ligneCmd = config.getLigneCommandeExécutionOptimisationTEST( nomDossierTravail = dossierTravail )

        logger.debug( "Ligne de commande : %s"%str( ligneCmd ))
        assert ligneCmd 

        subprocess.call( ligneCmd, stdout=standardOutputFile, stderr=standardOutputFile )
    
    except Exception as e:
        logger.error( "Erreur check_optimisation_tst ! %s: %s"%( type(e), e ))
        raise e


def check_diff_resultats():
    try:
        logger.debug( "Exécution Diff =  %s"%str( dossierTravail ))

        dossierRésultatREF = config.getDossierRésultatREF()
        dossierRésultatTEST = config.getDossierRésultatTEST()

        assert dossierTravail
        assert dossierRésultatREF 
        assert dossierRésultatTEST
        assert os.path.exists( dossierRésultatREF )
        assert os.path.exists( dossierRésultatTEST )

        # Comparaison du nombre de fichiers dans le dossier
        nbElementsREF = len( os.listdir( dossierRésultatREF ))
        nbElementsTEST  = len( os.listdir( dossierRésultatTEST ))
        
        # Nombre de fichiers dans chaque répertoire
        assert nbElementsREF == nbElementsTEST
        
        # Comparaison des fichiers résultats par rapport aux fichiers référence
        for nomElement in os.listdir( dossierRésultatREF ):

            # On sait que DonneesLogo.txt, message.txt, lptk.log sont différents
            if( nomElement == "DonneesLogo.txt" or 
                nomElement == "message.txt" or 
                nomElement == "lptk.log" or
                nomElement == "Coherence.txt" or
                nomElement == "Reporting.txt"
                ):
                continue

            nomFichierSource = dossierRésultatREF + os.sep + nomElement
            nomFichierCible  = dossierRésultatTEST + os.sep + nomElement
            
            # Fichier de référence est un fichier normal
            assert not os.path.isdir( nomFichierSource )
            
            # Fichier cible existe
            assert os.path.exists( nomFichierCible )
        
            # Comparaison ligne à ligne du fichier
            with open( nomFichierSource , mode='r') as fichierSource:
                with open( nomFichierCible , mode='r') as fichierCible:

                    lstLignesSource = fichierSource.readlines()
                    lstLignesCible  = fichierCible.readlines()
                    tailleSource    = len( lstLignesSource )
                    tailleCible     = len( lstLignesCible  )
                    
                    assert tailleSource == tailleCible
                    
                    # Comparaison ligne à ligne
                    for idx, ( ligneSource, ligneCible ) in enumerate( zip( lstLignesSource, lstLignesCible )):
                        assert config.compareStrings( ligneSource, ligneCible )

    except Exception as e:
        logger.error( "Erreur check_diff_resultats ! %s: %s"%( type(e), e ))
        raise e



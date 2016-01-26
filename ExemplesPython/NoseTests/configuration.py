#!/usr/bin/env python

import configparser
import os
import logging
from datetime import date

# Degré de détail du log interne
## NIVEAU_DEBUG = logging.INFO
NIVEAU_DEBUG = logging.DEBUG


class Singleton( object ):
    """ Classe dont il n'existe qu'une seule instance """
 
    # Singleton
    _instance =  None
     
    # Constructeur de l'instance unique
    def __new__( cls ):
        """ Constructeur du singleton """
        if cls._instance is None:
            #print( "Nouvelle instance du Singleton %s "%str( cls ) )
            cls._instance = super().__new__( cls )  # super( Singleton, cls )
        
        return cls._instance
 
    @classmethod
    def getInstance( cls ):
        if cls._instance is None:
            cls._instance = cls()
        
        return cls._instance
 
    def __init__( self ):
        super().__init__()
      
    def __repr__(self, *args, **kwargs):
        return super().__repr__( *args, **kwargs)
  
    def __str__(self, *args, **kwargs):
        return super().__str__( *args, **kwargs)


class ConfigurationDuLog( Singleton ):
    """ Initialise le log """

    def __init__( self ):
        Singleton.__init__( self )

    @staticmethod
    def getLogger( loggerName ):
        logger = logging.getLogger( loggerName )
        logger.propagate = False
    
        for hdlr in logger.handlers:
            logger.removeHandler(hdlr)
        
        formateur = logging.Formatter( '%(asctime)s - %(name)s - %(levelname)s :: %(message)s' )
        nomFichierLog = os.getcwd() + os.sep + "log" + date.today().strftime( "%Y-%m-%d") + ".txt"
        
        fichier = logging.FileHandler( nomFichierLog )
        fichier.setFormatter( formateur )
        
        console = logging.StreamHandler()
        console.setFormatter( formatter )
        
        logger.addHandler( fichier )
        logger.addHandler( console )
        logger.setLevel( NIVEAU_DEBUG )

        # logger.info( "** Ouverture du log ** : %s "%loggerName )
        return logger


class ConfigurationDesTests( Singleton ):

    SECTION_REFERENCE           = 'Reference'
    SECTION_TEST                = 'VersionTest'
    
    CLE_CREATION_DONNEES_LOGO   = "Commande_CreationDonneesLogo"
    CLE_EXECUTION               = "Commande_Execution"
    ##CLE_SOUS_DOSSIER_RESULTAT   = "Sous_Dossier_Resultat"


    # Constructeur de l'instance unique
    def __new__( cls, *args, **kwargs ):
        #print( "ConfigurationDesTests.__new__ : %s "%str( cls ) )
        return super().__new__( cls ) # super( ConfigurationDesTests, cls )

    # Initialisation
    def __init__( self, dossierWorkspace = None, fichierConfiguration = "configuration.ini" ):
        #print( "ConfigurationDesTests.__init__ : %s "%str( self ) )

        # Appel à la superclasse
        super().__init__() # Singleton

        # Récupération du 'workspace' qui a été défini comme variable d'environnement par Jenkins
        self.dossierWorkspace = os.getenv( key='WORKSPACE', default=os.getcwd() ) if dossierWorkspace is None else dossierWorkspace

        # Ajout du séparateur de répertoires
        self.dossierWorkspace += os.sep

        # Lecture du fichier de config
        # dans lequel se trouve les paramètres des tests
        config = configparser.ConfigParser()
        config.read( self.dossierWorkspace + fichierConfiguration )

        configREF  = config[ ConfigurationDesTests.SECTION_REFERENCE ]
        configTEST = config[ ConfigurationDesTests.SECTION_TEST ]

        self.commandeCréationDonnéesLogoREF    = self.dossierWorkspace + configREF[ ConfigurationDesTests.CLE_CREATION_DONNEES_LOGO ].replace( "/", os.sep ).replace( "\\", os.sep )
        self.commandeExécutionREF              = self.dossierWorkspace + configREF[ ConfigurationDesTests.CLE_EXECUTION             ].replace( "/", os.sep ).replace( "\\", os.sep )
        ## self.sousDossierResultatREF            = configREF[ CLE_SOUS_DOSSIER_RESULTAT ].replace( "/", os.sep ).replace( "\\", os.sep )

        self.commandeCréationDonnéesLogoTEST   = self.dossierWorkspace + configTEST[ ConfigurationDesTests.CLE_CREATION_DONNEES_LOGO ].replace( "/", os.sep ).replace( "\\", os.sep )
        self.commandeExécutionTEST             = self.dossierWorkspace + configTEST[ ConfigurationDesTests.CLE_EXECUTION             ].replace( "/", os.sep ).replace( "\\", os.sep )
        ## self.sousDossierResultatTEST           = configTEST[ CLE_SOUS_DOSSIER_RESULTAT ].replace( "/", os.sep ).replace( "\\", os.sep )

#         # Récupération des noms de dossiers définis,
#         # puis (par précaution) modification des séparateurs de dossiers, selon la plateforme UNIX / Windows
#         self.dossierRef_DonneesLogo     =( dossierWorkspace + configREF[ 'Dossier_DonneesLogo' ] ).replace( "/", os.sep ).replace( "\\", os.sep )
#         self.dossierRef_GoeXXX          =( dossierWorkspace + configREF[ 'Dossier_GoeXXX'      ] ).replace( "/", os.sep ).replace( "\\", os.sep )
#         self.dossierTest_DonneesLogo    =( dossierWorkspace + configTEST[ 'Dossier_DonneesLogo' ] ).replace( "/", os.sep ).replace( "\\", os.sep )
#         self.dossierTest_GoeXXX         =( dossierWorkspace + configTEST[ 'Dossier_GoeXXX'      ] ).replace( "/", os.sep ).replace( "\\", os.sep )
#         
#         # Génération des commandes complètes
#         self.commandeRef_DonneesLogo    = self.dossierRef_DonneesLogo + os.sep + configREF[ 'Commande_DonneesLogo' ]
#         self.commandeRef_Goelan         = self.dossierRef_GoeXXX + os.sep + configREF[ 'Commande_Goelan'      ]
#         self.commandeRef_Goelette       = self.dossierRef_GoeXXX + os.sep + configREF[ 'Commande_Goelette'    ]
#         self.commandeRef_Goemon         = self.dossierRef_GoeXXX + os.sep + configREF[ 'Commande_Goemon'      ]
#         self.commandeRef_Goesto_Opti    = self.dossierRef_GoeXXX + os.sep + configREF[ 'Commande_Goesto_Opti' ]
#         self.commandeRef_Goesto_Simu    = self.dossierRef_GoeXXX + os.sep + configREF[ 'Commande_Goesto_Simu' ]
#         
#         self.commandeTest_DonneesLogo   = self.dossierTest_DonneesLogo + os.sep + configTEST[ 'Commande_DonneesLogo' ]
#         self.commandeTest_Goelan        = self.dossierTest_GoeXXX + os.sep + configTEST[ 'Commande_Goelan'      ]
#         self.commandeTest_Goelette      = self.dossierTest_GoeXXX + os.sep + configTEST[ 'Commande_Goelette'    ]
#         self.commandeTest_Goemon        = self.dossierTest_GoeXXX + os.sep + configTEST[ 'Commande_Goemon'      ]
#         self.commandeTest_Goesto_Opti   = self.dossierTest_GoeXXX + os.sep + configTEST[ 'Commande_Goesto_Opti' ]
#         self.commandeTest_Goesto_Simu   = self.dossierTest_GoeXXX + os.sep + configTEST[ 'Commande_Goesto_Simu' ]

    def getDossierRésultatREF( self, nomDossierTravail = None ):
        if nomDossierTravail is None:
            nomDossierTravail = self.dossierWorkspace
            
        return nomDossierTravail + os.sep + ConfigurationDesTests.SECTION_REFERENCE
    
    def getDossierRésultatTEST( self, nomDossierTravail = None ):
        if nomDossierTravail is None:
            nomDossierTravail = self.dossierWorkspace
            
        return nomDossierTravail + os.sep + ConfigurationDesTests.SECTION_TEST

    def getLigneCommandeCréationDonnéesLogoREF(self, nomFichierDataXLS, nomDossierTravail = None, modeLancement = "GOEMON_MONO", modeParsageEntête = "PAR_INDEX_DE_COLONNE " ):
        """
        Renvoie la ligne de commande complète de l'exécutable Python DonneesLogo, options comprises
        sous la forme d'une string (paramètre subprocess.call) 
        """
        if nomDossierTravail is None:
            nomDossierTravail = self.dossierWorkspace

        return( self.commandeCréationDonnéesLogoREF + 
                " --modeParsageEntete " + modeParsageEntête +
                " --modeLancement "     + modeLancement +
                " --repTravail "        + nomDossierTravail + 
                " --repResultats "      + self.getDossierRésultatREF( nomDossierTravail ) +
                " --dataXLS "           + nomFichierDataXLS )
        #return self.commandeCréationDonnéesLogoREF

    def getLigneCommandeCréationDonnéesLogoTEST(self, nomFichierDataXLS, nomDossierTravail = None, modeLancement = "GOEMON_MONO", modeParsageEntête = "PAR_INDEX_DE_COLONNE " ):
        """
        Renvoie la ligne de commande complète de l'exécutable Python DonneesLogo, options comprises
        sous la forme d'une string (paramètre subprocess.call) 
        """
        if nomDossierTravail is None:
            nomDossierTravail = self.dossierWorkspace

        return( self.commandeCréationDonnéesLogoTEST + 
                " --modeParsageEntete " + modeParsageEntête +
                " --modeLancement "     + modeLancement +
                " --repTravail "        + nomDossierTravail +
                " --repResultats "      + self.getDossierRésultatTEST( nomDossierTravail ) +
                " --dataXLS "           + nomFichierDataXLS )
        #return self.commandeCréationDonnéesLogoTEST

    def getLigneCommandeExécutionOptimisationREF( self, nomDossierTravail = None ):
        if nomDossierTravail is None:
            nomDossierTravail = self.dossierWorkspace

        return self.commandeExécutionREF + " " + self.getDossierRésultatREF( nomDossierTravail ) 

    def getLigneCommandeExécutionOptimisationTEST( self, nomDossierTravail = None ):
        if nomDossierTravail is None:
            nomDossierTravail = self.dossierWorkspace
        return self.commandeExécutionTEST + " " + self.getDossierRésultatTEST( nomDossierTravail )


    @staticmethod
    def compareStrings( str1, str2 ):
        (str1, str2) =[ string
            .strip()            
            .casefold()         
            .replace(" ","")
            .replace("à","a") 
            .replace("â","a") 
            .replace("é","e")   
            .replace("è","e") 
            .replace("ê","e") 
            .replace("î","i") 
            .replace("ï","i") 
            .replace("ô","o") 
            .replace("ù","u") 
            .replace("û","u") 
            .replace("ü","u") 
            for string in( str( str1 ), str( str2 )) ]
        
        return( str1 == str2 )


#!/usr/bin/env python
import os

from configuration import ConfigurationDuLog, ConfigurationDesTests

### NOSE TESTS ###
config = None
logger = None 

def setup_module(module):
    """ Méthode que Nose Test exécute avant le début des tests """
    global config
    global logger 
    
    config = ConfigurationDesTests.getInstance()
    logger = ConfigurationDuLog.getLogger( __name__ )
    logger.info( "# Démarrage du %s"%str( module ))


def teardown_module(module):
    """ Méthode que Nose Test exécute après la fin des tests """
    logger.info( "# Fin du %s"%str( module ))
    logger.info( " - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -" )


def test_log():
    global logger
     
    logger1 = ConfigurationDuLog.getLogger( __name__ )
    logger2 = ConfigurationDuLog.getLogger( __name__ )
 
    assert logger is not None
    assert logger  is logger1
    assert logger1 is logger2


def test_instances():
    assert logger is not None
    try:
        logger.info( "Vérification de la lecture correcte du fichier de configuration")
        instance1 = ConfigurationDesTests.getInstance()
        instance2 = ConfigurationDesTests.getInstance()
 
    except Exception as e:
        logger.error( "Erreur ! %s: %s"%( type(e), e ))
        assert False
 
    assert instance1 is not None
    assert instance1 is instance2
    assert len( instance1.getLigneCommandeCréationDonnéesLogoREF( "toto" )) > 0 


# def test_variables_environnement_reference():
#     assert logger is not None
#     try:
#     
#         # Méthode interne utilisée uniquement ici
#         def OuiNon( booléen ):
#             if booléen:
#                 return "Oui"
#             else:
#                 return "Non"
#     
#         logger.info( "Vérification de l'existence des exécutables de référence")
#         config = ConfigurationDesTests.getInstance()
#         assert config is not None
#         
#         exe_donnees_logo    = os.getenv( 'CMD_REF_DONNEES_LOGO',    '' )
#         exe_goelan          = os.getenv( 'CMD_REF_GOELAN',          '' )
#         exe_goelette        = os.getenv( 'CMD_REF_GOELETTE',        '' )
#         exe_goemon          = os.getenv( 'CMD_REF_GOEMON',          '' )
#         exe_goesto_opti     = os.getenv( 'CMD_REF_GOESTO_OPTI',     '' )
#         exe_goesto_simu     = os.getenv( 'CMD_REF_GOESTO_SIMU',     '' )
#             
#         exe_donnees_logo_existe =   os.path.exists( exe_donnees_logo ) 
#         exe_goelan_existe =         os.path.exists( exe_goelan       )
#         exe_goelette_existe =       os.path.exists( exe_goelette     )
#         exe_goemon_existe =         os.path.exists( exe_goemon       )
#         exe_goesto_opti_existe =    os.path.exists( exe_goesto_opti  )
#         exe_goesto_simu_existe =    os.path.exists( exe_goesto_simu  )
#         
#         logger.debug( "Exe Ref Données Logo : %s : %s"%( OuiNon(exe_donnees_logo_existe),   exe_donnees_logo ))
#         logger.debug( "Exe Ref Goelan       : %s : %s"%( OuiNon(exe_goelan_existe),         exe_goelan       ))
#         logger.debug( "Exe Ref Goelette     : %s : %s"%( OuiNon(exe_goelette_existe),       exe_goelette     ))
#         logger.debug( "Exe Ref Goemon       : %s : %s"%( OuiNon(exe_goemon_existe),         exe_goemon       ))
#         logger.debug( "Exe Ref Goesto Opti  : %s : %s"%( OuiNon(exe_goesto_opti_existe),    exe_goesto_opti  ))
#         logger.debug( "Exe Ref Goesto Simu  : %s : %s"%( OuiNon(exe_goesto_simu_existe),    exe_goesto_simu  ))
#     
#     except Exception as e:
#         logger.error( "Erreur ! %s: %s"%( type(e), e ))
#         assert False
#     
#     # test de cohérence
#     assert exe_donnees_logo == config.getCommandeRef_DonneesLogo()
#     assert exe_goelan       == config.getCommandeRef_Goelan()
#     assert exe_goelette     == config.getCommandeRef_Goelette()
#     assert exe_goemon       == config.getCommandeRef_Goemon()
#     assert exe_goesto_opti  == config.getCommandeRef_Goesto_Opti()
#     assert exe_goesto_simu  == config.getCommandeRef_Goesto_Simu()
# 
#     # Test d'existence des fichiers
#     assert exe_donnees_logo_existe
#     assert exe_goelan_existe
#     assert exe_goelette_existe
#     assert exe_goemon_existe
#     assert exe_goesto_opti_existe
#     assert exe_goesto_simu_existe
# 
# 
# def test_variables_environnement_test():
#     assert logger is not None
#     try:
#         # Méthode interne utilisée uniquement ici
#         def OuiNon( booléen ):
#             if booléen:
#                 return "Oui"
#             else:
#                 return "Non"
#     
#         logger.info( "Vérification de l'existence des exécutables de test")
#         config = ConfigurationDesTests.getInstance()
#         assert config is not None
#         
#         exe_donnees_logo    = os.getenv( 'CMD_TEST_DONNEES_LOGO',   '' )
#         exe_goelan          = os.getenv( 'CMD_TEST_GOELAN',         '' )
#         exe_goelette        = os.getenv( 'CMD_TEST_GOELETTE',       '' )
#         exe_goemon          = os.getenv( 'CMD_TEST_GOEMON',         '' )
#         exe_goesto_opti     = os.getenv( 'CMD_TEST_GOESTO_OPTI' ,   '' )
#         exe_goesto_simu     = os.getenv( 'CMD_TEST_GOESTO_SIMU' ,   '' )
#             
#         exe_donnees_logo_existe =   os.path.exists( exe_donnees_logo ) 
#         exe_goelan_existe =         os.path.exists( exe_goelan       )
#         exe_goelette_existe =       os.path.exists( exe_goelette     )
#         exe_goemon_existe =         os.path.exists( exe_goemon       )
#         exe_goesto_opti_existe =    os.path.exists( exe_goesto_opti  )
#         exe_goesto_simu_existe =    os.path.exists( exe_goesto_simu  )
#         
#         logger.debug( "Exe Test Données Logo : %s : %s"%( OuiNon(exe_donnees_logo_existe),   exe_donnees_logo ))
#         logger.debug( "Exe Test Goelan       : %s : %s"%( OuiNon(exe_goelan_existe),         exe_goelan       ))
#         logger.debug( "Exe Test Goelette     : %s : %s"%( OuiNon(exe_goelette_existe),       exe_goelette     ))
#         logger.debug( "Exe Test Goemon       : %s : %s"%( OuiNon(exe_goemon_existe),         exe_goemon       ))
#         logger.debug( "Exe Test Goesto Opti  : %s : %s"%( OuiNon(exe_goesto_opti_existe),    exe_goesto_opti  ))
#         logger.debug( "Exe Test Goesto Simu  : %s : %s"%( OuiNon(exe_goesto_simu_existe),    exe_goesto_simu  ))
# 
#     except Exception as e:
#         logger.error( "Erreur ! %s: %s"%( type(e), e ))
#         assert False
# 
#     # test de cohérence
#     assert exe_donnees_logo == config.getCommandeTest_DonneesLogo()
#     assert exe_goelan       == config.getCommandeTest_Goelan()
#     assert exe_goelette     == config.getCommandeTest_Goelette()
#     assert exe_goemon       == config.getCommandeTest_Goemon()
#     assert exe_goesto_opti  == config.getCommandeTest_Goesto_Opti()
#     assert exe_goesto_simu  == config.getCommandeTest_Goesto_Simu()
# 
#     # Test d'existence des fichiers
#     assert exe_donnees_logo_existe
#     assert exe_goelan_existe
#     assert exe_goelette_existe
#     assert exe_goemon_existe
#     assert exe_goesto_opti_existe
#     assert exe_goesto_simu_existe


### En cas d'appel manuel ###
if( __name__ == "__main__" ):
    print( "Ce fichier ne s'appelle pas directement." )
    print( "Il est utilisé par les tests nose" )


#!/usr/bin/env python

from configuration import ConfigurationDuLog
import os, sys

logger = None
message_découverte = "Test de découverte exécuté : %s"%__file__



def setup_module(module):
    """ Méthode que Nose Test exécute avant le début des tests """
    global logger 
    logger = ConfigurationDuLog.getLogger( __name__ )
    logger.debug( "# Démarrage du %s"%str( module ))


def teardown_module(module):
    """ Méthode que Nose Test exécute après la fin des tests """
    logger.debug( "# Fin du %s"%str( module ))
    logger.debug( " - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -" )


def test_decouverte_print_console():
    # Ecriture sur la console
    print( "PRINT: %s"%message_découverte )
    assert True


def test_decouverte_print_log():
    assert logger is not None
    
    # Ecriture dans le log
    logger.info( "LOG: %s"%message_découverte )


def test_decouverte_print_infos_debug():
    logger.debug( "** INFORMATIONS DEBOGAGE **")
    logger.debug( "__name__ : '%s'"%__name__ )
    logger.debug( "__file__ : '%s'"%__file__ )
    logger.debug( "__package__ : '%s'"%__package__ )
#     logger.debug( "__class__ : '%s'"%__class__ )
#     logger.debug( "__path__ : '%s'"%__path__ )
    logger.debug( "__loader__ : '%s'"%__loader__ )
#    logger.debug( "Loader Name : '%s'"%__loader__.fullname )
    logger.debug( "Sys.Args : '%s'"%( ",".join([ str(elt) for elt in sys.argv ])))


def test_decouverte_print_environnement():
    workspace = os.getenv( 'WORKSPACE', False )
    logger.info( "Variable d'environnement 'WORKSPACE' : %s"%str( workspace ))
    assert workspace


### En cas d'appel manuel ###

if( __name__ == "__main__" ):
    print( "Ce fichier ne s'appelle pas directement." )
    print( "Il est utilisé par les tests nose" )



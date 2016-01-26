#!/usr/bin/env python

from configuration import ConfigurationDuLog

logger = None

def setup_package( package ):
    """ Méthode que Nose Test exécute avant le début des tests """
#     global config
    global logger 
    
    #config = ConfigurationDesTests.getInstance()
    logger = ConfigurationDuLog.getLogger( __name__ )
    logger.info( "<< Démarrage du package %s >>"%str( package ))


def teardown_package( package ):
    """ Méthode que Nose Test exécute après la fin des tests """
#     global config
#     global logger 
    
    #config = ConfigurationDesTests.getInstance()
    logger = ConfigurationDuLog.getLogger( __name__ )
    logger.debug( "<< Fin du package %s >>"%str( package ))


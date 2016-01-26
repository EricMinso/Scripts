#!/usr/bin/env python

### __all__ = [ 'configuration', 'test_configuration', 'test_decouverte' ]

import configuration
from configuration import ConfigurationDuLog 

# from subfolder import test_subfolder
# from subfolder import test_unitaire
# from subfolder import test_anr
# from subfolder import test_configuration
# from subfolder import test_decouverte


print( "Module Root : %s " % __file__ )
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


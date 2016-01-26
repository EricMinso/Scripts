#!/bin/ksh

###############################################################################
#
# NOM		: inter_aix.sh
# DATE		: 25 août 2010
# AUTEUR	: Eric MINSO
# VERSION	: Fichier v0.1
#
# DESCRIPTION :
#	Sauvegarde la base de données
#	Enregistre les infos sympas
#
# PARAMETRES :
#	Aucun
#
# HISTORIQUE :
#
###############################################################################


###############################################################################
# INITIALISATIONS
###############################################################################

. /cas/bin/profile

echo "Repertoire de sortie ? Defaut = /tmp/inter_aix"
read TMP_REP_BASE

if (( ${#TMP_REP_BASE} > 0 ))
then
	REP_BASE=$TMP_REP_BASE
else
	REP_BASE='/tmp/inter_aix'
fi

mkdir $REP_BASE
cd $REP_BASE

NOW=`date +%Y%m%d_%H%M%S`
FIC_SORTIE=${REP_BASE}'/aix_'${NOW}'.txt'
LOG_TAR=${REP_BASE}'/log_'${NOW}'.tar'
BACKUP_BASE=${REP_BASE}'/'${NOW}'_BASE'
BACKUP_BADGE=${REP_BASE}'/'${NOW}'_BADGE'
BACKUP_GRAPH=${REP_BASE}'/'${NOW}'_GRAPH'
BACKUP_HISTO=${REP_BASE}'/'${NOW}'_HISTO'
BACKUP_IMAGE=${REP_BASE}'/'${NOW}'_IMAGE'

if [ $? -ne 0 ]
then
	echo "Echec"
	exit -1
fi

exec 2>&1
{

###############################################################################
# RECUPERATIONS INFOS
###############################################################################

echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| SAUVEGARDE DES INFOS AIX PP'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo 'HostName : '`hostname`
echo 'IP : '`ifconfig en0`
echo 'Repertoire de sortie : '$REP_BASE
echo 'Repertoire courant : '`pwd`
echo 'TPS mode : '`tpsmode`

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| DATE DU SERVEUR'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

date "+%Y-%m-%d %H:%M:%S"

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| OSLEVEL'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

oslevel

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| PLEVEL'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

plevel

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| SKBASE'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

skbase

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| SKVER'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

skver

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| SYSTEM_CONFIG'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

selectrpt "SELECT * FROM system_config"

if [ $? -ne 0 ]
then
	echo "Echec"
	exit -1
fi

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| TPS_DAEMONS'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

selectout "SELECT * FROM tps_daemons"

if [ $? -ne 0 ]
then
	echo "Echec"
	exit -1
fi


echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| INTEGRITE'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

chkchars.sh
vmicro


echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| CRONTAB'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

crontab -l

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| PROCESSUS'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

ps -ef

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| OCCUPATION DISQUE'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

df -k

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| MOUNT'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

mount

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| VOLUME GROUPS'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

lsvg

for VG in `lsvg`
do
	echo ' - '
	lsvg $VG 
	lsvg -l $VG 
done

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| MATERIEL'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

lscfg
lscfg -v
lsdev


echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| RESEAU'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

netstat
netstat -v

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| LOGICIEL'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

lslpp -L

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| TAR DES LOGS'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

tar -cvf $LOG_TAR			\
	/cas/log				\
	/cas/db/log				\
	/custom_pp/log			\
	/etc/hosts				\
	/etc/services			\
	/etc/lmgr/license.dat	\
	/cas/.*					\
	/.aixinstall*			\
	/.quickfix*				\
	/.hotfix*				\
	/.*history				\
	/.profile				\
	/*smit*
	
if [ $? -ne 0 ]
then
	echo "Echec"
	exit -1
fi

gzip $LOG_TAR

echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| BACKUP BASE DE DONNEES'
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
 
cba -c -b -d $BACKUP_BASE -base 
cba -c -b -d $BACKUP_BADGE -badge 
cba -c -b -d $BACKUP_IMAGE -image 
cba -c -b -d $BACKUP_GRAPH -graph
cba -c -b -d $BACKUP_HISTO -hist


echo ''
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'
echo '| FIN le ' `date "+%Y-%m-%d %H:%M:%S"`
echo ' - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -'

} | tee -a $FIC_SORTIE


set WORKSPACE=%~1
set BUILD_DISPLAY_NAME=%~2
set FICHIER_SORTIE_XML=%WORKSPACE%\nosetests.xml
echo Fichier = "%FICHIER_SORTIE_XML%"

cd %WORKSPACE%
python -m nose -vv --with-xunit --xunit-file="%FICHIER_SORTIE_XML%"


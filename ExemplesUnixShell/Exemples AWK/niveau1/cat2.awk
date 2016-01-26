#!/usr/bin/awk -f

BEGIN \
{
    print "démarrage"
    FS = "-"
    OFS = "+"
    ORS = "*\n*"
}


{ print }

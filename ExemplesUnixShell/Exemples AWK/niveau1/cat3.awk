#!/usr/bin/awk -f

# BEGIN \
# {
#     print "demarrage"
#     FS = " "
#     OFS = "+"
#     ORS = "\t"
# }


# $0 { print $1 "#" $2 }


{ tableau[NR] = $0 }

NR == 5 { print tableau[NR-1] }

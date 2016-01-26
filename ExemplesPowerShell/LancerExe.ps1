
Write-Output "Debut : " 
Write-Output Get-Item env:\PATH
[DateTime]::Now

# Vérification du nombre d'arguments
if( $args.count -lt 2 )
{
	Write-Host "Usage : LancerExe.ps1 [chemin] [exe] [arguments exe...]"  -foregroundcolor red
	exit
}

# Formattage des arguments (optimisable)
$chemin		= $args[0]
$exe		= $args[1]
$arg2		= $args[2]
$arg3		= $args[3]
$arguments	= "$arg2 $arg3"

# Compteur de fichiers traités
$compte		= 0

Write-Output "Chemin = $chemin" 
Write-Output "Exe = $exe $arguments" 
Set-Location -literalPath $chemin

# Recherche de tous les Données.txt dans les sous-répertoire du dossier transmis en paramètre
Get-ChildItem $chemin "Donnees.txt" -recurse | ForEach-Object {
	
	# Récupération du répertoire du fichier trouvé
	$repertoire = $_.DirectoryName
	$compte = $compte + 1
	
	Write-Host "Dossier $compte = $repertoire " -foregroundcolor green
	
	# Appel de Goexxx
	$Process = Start-Process $exe "$arguments $repertoire" -wait

	Write-Output "Resultat = $Process"
}

# Fin
Write-Output "Pafff-Fin : $compte dossiers traités" 
[DateTime]::Now

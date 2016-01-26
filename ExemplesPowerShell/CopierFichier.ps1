
Write-Output "Debut : " 
Write-Output Get-Item env:\PATH
[DateTime]::Now

# Vérification du nombre d'arguments
if( $args.count -ne 2 )
{
	Write-Host "Usage : CopierFichier.ps1 [fichier] [chemin]"  -foregroundcolor red
	exit
}

# Formattage des arguments 
$fichier	= $args[0]
$chemin		= $args[1]

# Compteur de fichiers traités
$compte		= 0

Write-Output "Fichier = $fichier" 
Write-Output "Chemin = $chemin" 
#Set-Location -literalPath $chemin

# Recherche de tous les sous-répertoire du dossier transmis en paramètre
Get-ChildItem $chemin -recurse | ForEach-Object {
	
	# Récupération du répertoire du fichier trouvé
	$repertoire = $_.DirectoryName
	$compte = $compte + 1
	
	Write-Host "Dossier $compte = $repertoire " -foregroundcolor green
	
	# Appel de Goexxx
	Copy-Item $fichier $repertoire

}

# Fin
Write-Output "Pafff-Fin : $compte dossiers traités" 
[DateTime]::Now

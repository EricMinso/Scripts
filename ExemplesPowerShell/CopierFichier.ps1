
Write-Output "Debut : " 
Write-Output Get-Item env:\PATH
[DateTime]::Now

# V�rification du nombre d'arguments
if( $args.count -ne 2 )
{
	Write-Host "Usage : CopierFichier.ps1 [fichier] [chemin]"  -foregroundcolor red
	exit
}

# Formattage des arguments 
$fichier	= $args[0]
$chemin		= $args[1]

# Compteur de fichiers trait�s
$compte		= 0

Write-Output "Fichier = $fichier" 
Write-Output "Chemin = $chemin" 
#Set-Location -literalPath $chemin

# Recherche de tous les sous-r�pertoire du dossier transmis en param�tre
Get-ChildItem $chemin -recurse | ForEach-Object {
	
	# R�cup�ration du r�pertoire du fichier trouv�
	$repertoire = $_.DirectoryName
	$compte = $compte + 1
	
	Write-Host "Dossier $compte = $repertoire " -foregroundcolor green
	
	# Appel de Goexxx
	Copy-Item $fichier $repertoire

}

# Fin
Write-Output "Pafff-Fin : $compte dossiers trait�s" 
[DateTime]::Now

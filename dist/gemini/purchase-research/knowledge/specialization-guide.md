# Guide de spécialisation

## Objectif
Transformer les enseignements durables d'une étude d'achat en expertise réutilisable sans figer des informations temporelles.

## Extraction
À la fin d'une étude, classer les apprentissages en :
- universels : restent dans purchase-research ;
- métier durables : candidats au sous-skill ;
- temporels : ne pas intégrer ;
- spécifiques à l'utilisateur : ne pas intégrer sauf structure générique.

## Test de généralisation
Pour chaque règle candidate demander :
« Cette règle aiderait-elle un autre utilisateur recherchant un autre produit de la même catégorie dans deux ans ? »
Si non, ne pas l'intégrer comme règle du skill.

## Nommage
Préférer un nom court en kebab-case :
- vae-research
- laptop-research
- camera-research
- 3d-printer-research
- robot-vacuum-research

## Version
Création : 1.0.0
Ajout méthodologique compatible : +0.1.0
Correction mineure : +0.0.1
Rupture majeure du workflow : +1.0.0

## Livrables
Toujours fournir :
- dossier lisible ;
- ZIP ;
- changelog si mise à jour ;
- résumé des règles capitalisées.

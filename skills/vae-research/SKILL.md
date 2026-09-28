---
name: vae-research
description: Recherche, audite et compare des vélos à assistance électrique (VAE), vélos cargo, longtails, fatbikes et accessoires pour un achat en France ou en Europe. Utiliser pour définir un cahier des charges, trouver des modèles, vérifier prix/promotions, homologation 250 W/25 km/h, PTAC/charge utile/passager, moteur/batterie/freinage, SAV et pièces, accessoires, remorques, transport sur porte-vélos, aides à l'achat, puis produire une shortlist ou un dossier comparatif sourcé.
metadata:
  version: 1.0.0
---

# VAE Research

Skill spécialisé pour la recherche d'achat de VAE. Utiliser avec le workflow générique `purchase-research` lorsqu'il est disponible.

## Principes
- Commencer par l'usage, pas par la forme ou la marque.
- Rechercher les données actuelles : prix, disponibilité, gamme, garantie, aides, SAV, promotions.
- Priorité : fabricant/manuel/certificat → source publique/norme → revendeur officiel → média ayant testé → communauté.
- Séparer `charge utile`, `charge maximale`, `PTAC`, `charge porte-bagages` et `charge passager`.
- Une selle longue ne prouve pas qu'un passager adulte est autorisé.
- En France/UE, vérifier 250 W nominal et assistance jusqu'à 25 km/h ; signaler accélérateur/débridage.
- Ne jamais inventer une compatibilité d'accessoire, remorque ou porte-vélos.
- Comparer le coût du système complet.

## Workflow
1. Cahier des charges : budget, poids utilisateurs, passager, terrain, distances, relief, cargo, transport voiture, SAV, pays/aides.
2. Explorer 5 à 10 candidats parmi VTC/trekking, cargo compact, longtail, fatbike et VTT utilitaire.
3. Auditer les finalistes avec `references/audit-grid.md`.
4. Chercher des essais terrain : autonomie, côte chargé, freinage, stabilité passager, confort, chemins, défauts et pièces.
5. Auditer accessoires : paniers, racks, sacoches, passager + bagagerie, remorque, batterie supplémentaire.
6. Pour le transport automobile : poids sans batterie, longueur, empattement, pneus, limite par rail et charge verticale d'attelage.
7. Vérifier garantie, réseau France, composants standards, batterie et pièces électriques.
8. Pour les aides : rechercher les règles actuelles, résidence, date, catégorie, plafond et justificatifs ; ne jamais supposer qu'un biplace est un cargo.
9. Produire plusieurs scénarios si les usages sont incompatibles.
10. Livrable : tableau + 2 à 5 finalistes ou dossier selon `references/report-template.md`.

## Sources
Lire `references/source-policy.md`.

## Constructeurs
Si une donnée bloquante manque, préparer des questions écrites identiques pour les modèles concurrents.

## Fraîcheur
Toujours dater prix et promotions. Ne pas présenter une information commerciale ancienne comme actuelle.

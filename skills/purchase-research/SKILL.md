---
name: purchase-research
description: Accompagne une réflexion structurée avant l'achat d'un produit. Utiliser dès que l'utilisateur manifeste une intention, une envie, une hésitation ou un projet d'achat et souhaite être conseillé, comparer des produits, savoir quoi choisir, combien dépenser ou vérifier si un produit lui convient. Le skill transforme l'idée initiale en cahier des charges adapté à la catégorie, pose uniquement les questions discriminantes, effectue une recherche web poussée et sourcée (fabricants, documentation, tests indépendants, SAV, prix, accessoires, coût complet), compare plusieurs scénarios d'usage, identifie les inconnues bloquantes et génère sur demande ou en fin d'étude un document de synthèse décisionnel.
metadata:
  version: 1.4.0
---

# Purchase Research

Assistant de réflexion pré-achat. L'objectif n'est pas de trouver rapidement « le meilleur produit », mais de construire une décision robuste à partir des usages réels, contraintes, compromis, coût total et qualité des preuves.

## Principes
- Usage avant produit.
- Poser seulement les questions discriminantes.
- Explorer largement puis auditer profondément 3 à 6 finalistes.
- Privilégier preuves, documentation et tests aux arguments marketing.
- Comparer le système complet et le coût total.
- Utiliser plusieurs scénarios si les usages conduisent à des optimums différents.
- Marquer les données importantes non établies `À CONFIRMER`.
- Réévaluer le classement lorsqu'un nouvel usage apparaît.
- Qualifier les preuves et appliquer les contraintes éliminatoires selon `references/evidence-engine.md`.

## Workflow
1. Identifier l'intention et la catégorie ; lire `references/category-question-bank.md`.
2. Construire un cahier des charges : Obligatoire / Important / Souhaitable / Hors besoin.
3. Lire `references/source-policy.md`, explorer 5 à 12 candidats et éliminer ceux qui violent un critère obligatoire.
4. Lire `references/evidence-engine.md`, puis auditer 3 à 6 finalistes avec `references/audit-framework.md` : officiel, manuel, garantie, pièces, prix actuel et tests indépendants. Pour chaque critère obligatoire, maintenir PASS / FAIL / UNRESOLVED.
5. Vérifier fiabilité, SAV, réparabilité, consommables et pièces critiques.
6. Calculer prix catalogue, prix actuel, accessoires obligatoires, infrastructure, configuration recommandée et coût de possession. Comparer les systèmes qui satisfont le besoin, pas seulement les produits nus.
7. Rechercher des essais terrain adaptés à la catégorie ; ne pas transposer les résultats d'une variante matériellement différente.
8. Comparer par scénarios quand nécessaire ; éviter les scores pseudo-précis.
9. Identifier les inconnues bloquantes et, si nécessaire, préparer les mêmes questions pour les fabricants concurrents.
10. Pour une étude substantielle ou portable, maintenir un état selon `references/state-protocol.md` et les schémas `schemas/`.
11. Générer une synthèse selon `references/report-template.md`.

## Capitalisation en skill spécialisé

Après une étude approfondie, évaluer si la catégorie mérite un skill spécialisé : vocabulaire propre, nombreux critères métier, réglementation/compatibilités spécifiques, sources spécialisées, pièges récurrents ou forte probabilité de réutilisation.

Avant de créer :
1. vérifier les skills disponibles ;
2. réutiliser un skill existant s'il convient ;
3. proposer son amélioration plutôt qu'un doublon si nécessaire ;
4. demander explicitement l'accord utilisateur.

Ne jamais créer ou modifier silencieusement un skill.

Capitaliser uniquement les connaissances durables : questions métier, taxonomie, grille d'audit, normes à vérifier, calculs, compatibilités, sources, protocoles de test, pièges marketing et règles SAV.

Ne pas capitaliser comme vérité durable : prix, promotions, stocks, classements du moment, « meilleur produit », disponibilité vendeur ou aides susceptibles d'évoluer.

Structure recommandée :
```
<category>-research/
  SKILL.md
  references/
    question-bank.md
    audit-grid.md
    source-policy.md
    domain-rules.md
    report-template.md
```

Lire `references/specialization-guide.md` avant de générer ou mettre à jour un sous-skill. Pour une mise à jour, préserver l'existant, ajouter uniquement les connaissances généralisables, incrémenter la version et produire un changelog.

## Comportement
- Montrer les découvertes importantes au fil de la recherche.
- Dire lorsqu'une information change le classement.
- Ne pas défendre une recommandation devenue obsolète.
- Préférer 2 à 4 options finales.
- Distinguer « meilleur pour cet usage » de « meilleur produit absolu ».
- Si un skill spécialisé existe, l'utiliser en complément de ce workflow.

## Version et mises à jour

Lire `references/update-policy.md` lorsqu'une vérification ou une mise à jour du skill est pertinente. Le fichier `manifest.json` du dépôt stable est la source de vérité des versions. Une version plus récente peut être signalée et proposée, mais aucune auto-modification silencieuse n'est autorisée.

## État structuré portable

Pour une recherche longue, une reprise inter-session ou un transfert entre plateformes, lire `references/state-protocol.md`. Les exigences utilisateur sont durables ; les prix, stocks, promotions, réglementation, aides et autres faits temporels doivent être revalidés lors de la reprise. Ne jamais dépendre uniquement de l'historique conversationnel lorsqu'un bundle structuré est disponible.

## Watch Engine

Lorsqu'une étude mature passe en état `WATCH`, lire `references/watch-engine.md`. Ne pas relancer inutilement la découverte du marché : surveiller uniquement les finalistes et événements définis dans `watch.json`. Par défaut, ne notifier que les changements matériels susceptibles de modifier le produit choisi, le moment d'achat, le coût système, une contrainte PASS/FAIL/UNRESOLVED ou la confiance SAV/garantie. Une surveillance future ne doit être planifiée qu'avec l'accord de l'utilisateur et via les capacités de scheduling réellement disponibles sur l'hôte.

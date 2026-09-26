# DG-AUDIT-001 — Archive complète au 25 septembre 2026

## Lire d’abord

Les **157** du plan maître sont des **fiches de constats provisoires**, pas un décompte de fichiers. Cette archive contient **158 fichiers liés à l’audit récupérés dans la Library**, dont **135 rapports Audit_** (109 de phase 2), ainsi que les **60 fichiers du package B01 reconstruits depuis la compilation**. Deux paires de rapports de phase 2 sont des copies binaires identiques et sont signalées dans l’inventaire. Le précédent petit ZIP de transfert est exclu parce que tous ses composants utiles figurent déjà ici. Images de cours d’allemand et autres fichiers sans rapport exclus.

**Autorité :** source normative exacte de B01 ; protocole externe v2 pour la méthode ; hashes et baseline ; checkpoints et rapports de preuve ; plan maître pour reprendre ; mémoire conversationnelle pour l’orientation seulement. `01_Reprise/Plan_Maitre_Audit_Design_Governance-1.md` est le plan actuel. `01_Reprise/Protocole_maitre_audit_v2.md` est le protocole externe actuel. `02_Sources_B01/Design_Governance_V1.0.md` est la compilation B01 ; `02_Sources_B01/package/` en est l’extraction en 60 fichiers, avec les chemins attendus dans le manifeste GitHub. Les versions antérieures dans `05_Historique_non_canonique/` ne sont pas des sources de règles B01.

**État :** phase 9.05 terminée, prochaine 9.06 scénario 19 « Surcharge procédurale ». Six scénarios sur vingt examinés au niveau du contrat, aucun stress complet d’efficacité clos ; 157 fiches toujours provisoires ; aucun patch B01 ni verdict global. La phase 6.02 reste mise de côté à la demande de l’utilisateur : les objets de `04_Pilotes_6_02_differes/` sont des préparations hors B01, sans preuve perceptuelle suffisante et sans clôture de phase.

## Reprendre dans Claude

Ouvrir d’abord le plan, le rapport `Audit_Phase9_05_RESISTANCE_RESULTS_Migration_Aliases_Routes_Promotion.md`, la matrice 9.01, le protocole §3–4/§19, les rapports 5.01–5.04, puis les propriétaires exacts pertinents dans B01. Avant chaque conclusion, vérifier les passages dans les sources et les limites du checkpoint ; ne pas prendre une recherche de passages pour une lecture complète. Pour un essai machine, utiliser une copie isolée de `package/` ou des mutations en mémoire. Ne pas modifier B01. Rédiger un rapport 9.06 avec positif/négatif, preuve et limites, et mettre à jour le plan seulement quand l’état évolue. Conserver rapport et plan actualisé pour un futur transfert.

Dans Claude Projects, charger le plan, le protocole, la compilation B01 et les rapports immédiatement pertinents comme fichiers individuels après extraction du ZIP ; ne pas présumer que le ZIP lui-même sera indexé. Dans un environnement avec accès au dossier et aux commandes, les 60 fichiers `package/` permettent la vérification locale.

## Intégrité et inventaire

Compilation B01 SHA-256 : `016e60028795e6c849e3e84974b103382791e8096ada6be8405a173415f5355d`. Protocole v2 SHA-256 : `990fc86f0e11c9fa20e7c8c3b8ae2bea66dd81defe70eaa6c8d84b2dc20610dd`. Les 60 chemins extraits correspondent aux 60 chemins GitHub du manifeste. La compilation et l’extraction ne certifient ni un dépôt Git original ni une release distante.

`INVENTAIRE.csv` indique pour chacun des 218 fichiers de contenu son chemin dans l’archive, son nom initial, son groupe, sa taille, son empreinte SHA-256 et son identifiant Library lorsqu’il en a un. `SHA256SUMS.txt` permet de vérifier les octets après extraction. Les rapports identiques sont conservés tous les deux afin de ne perdre aucun fichier de la Library.

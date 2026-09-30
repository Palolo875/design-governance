# Carte des moyens par couche — v0 (chantier H)

**Date :** 2026-09-27 · **À revoir avant :** 2027-03 · **Règle :** des **sources**, jamais des styles ; aucune famille, aucun thème par défaut ; le choix découle de la thèse. Droits vérifiés à chaque usage.

| Couche | Plafond sans asset fourni (conditions) | Où trouver de la qualité | Route (`VISUAL_TARGET`) |
|---|---|---|---|
| Typographie | Atteignable si la police est chargeable dans la cible et sa licence vérifiée pour l’usage (web, app, impression) | Polices de la marque ; Google Fonts (licences ouvertes, surtout SIL OFL) ; Fontshare (licence propre au service, gratuite sous conditions, à relire par police) | `CODE-NATIVE` |
| Icônes | Atteignable si la famille couvre les pictogrammes nécessaires ; licence à vérifier | Une seule famille cohérente (par exemple Lucide, Phosphor) | `CODE-NATIVE` |
| Composants | Atteignable dans la stack réelle ; hors web, traduire dans les idiomes de la plateforme | Design system fourni ; sinon bibliothèque éprouvée (par exemple shadcn, Radix) | `CODE-NATIVE` |
| Données, objets de preuve | Atteignable | Contenu du client, sinon données plausibles marquées illustratives | `CODE-NATIVE` |
| Texture et traitement | Atteignable si le rendu et la performance sont vérifiés à la capture | Filtres CSS et SVG, canvas | `CODE-NATIVE`, `HYBRIDE` |
| Photographie | Non sans intrant | Client (même au téléphone, lumière du jour) ; banques sous licence (Wikimedia Commons, Unsplash) | `FOURNI`, `CURATÉ` |
| Illustration, 3D | Non sans intrant | Commande, packs sous licence ; génération dirigée avec références ; 3D (par exemple Spline) | `FOURNI`, `CURATÉ`, `GÉNÉRÉ-DIRIGÉ` |
| Fichiers de design, marque | Non sans intrant | Figma ou kit de marque par connecteur | `FOURNI` |
| Contenu réel | Non sans le client | Client ; sinon contenu d’exemple marqué et liste de ce qu’il faut fournir (D-20, `CNT-01`, R5b-1) | — |

**Avant R8b :** chaque ressource retenue est vérifiée au moment de l’intégrer ou de l’utiliser (licence, usage, disponibilité) ; le nom d’une plateforme ne vaut pas autorisation générale (amendement du 28-09-2026).

**Traitement des assets moyens (chantier I) :** un seul traitement cohérent (recadrage, étalonnage, duotone, grain ou trame), justifié par la thèse ; la trame est un marqueur de la vague 3, à décider, pas à suivre.

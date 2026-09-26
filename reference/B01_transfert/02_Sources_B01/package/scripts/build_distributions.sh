#!/usr/bin/env bash
set -euo pipefail

ROOT=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
DIST="$ROOT/dist"
WORK="$ROOT/.build"
STAGE="$WORK/dist"
BACKUP="$ROOT/.dist.previous"

rm -rf "$WORK" "$BACKUP"
mkdir -p "$STAGE/github" "$STAGE/local"

# GitHub : distribution canonique versionnée.
cp -a "$ROOT/README.md" "$STAGE/github/README.md"
cp -a "$ROOT/RELEASE_NOTES.md" "$STAGE/github/RELEASE_NOTES.md"
cp -a "$ROOT/.gitignore" "$STAGE/github/.gitignore"
cp -a "$ROOT/V1" "$STAGE/github/V1"
cp -a "$ROOT/skills" "$STAGE/github/skills"
cp -a "$ROOT/schemas" "$STAGE/github/schemas"
mkdir -p "$STAGE/github/scripts"
cp -a "$ROOT/scripts/validate_design_governance.py" "$STAGE/github/scripts/validate_design_governance.py"
cp -a "$ROOT/scripts/validate_run_card.py" "$STAGE/github/scripts/validate_run_card.py"
cp -a "$ROOT/scripts/validate_contracts.py" "$STAGE/github/scripts/validate_contracts.py"
cp -a "$ROOT/scripts/build_distributions.sh" "$STAGE/github/scripts/build_distributions.sh"
cp -a "$ROOT/scripts/package_manifest.json" "$STAGE/github/scripts/package_manifest.json"
cp -a "$ROOT/scripts/validate_all.py" "$STAGE/github/scripts/validate_all.py"
cp -a "$ROOT/scripts/validate_reading_map.py" "$STAGE/github/scripts/validate_reading_map.py"
cp -a "$ROOT/scripts/read_route.py" "$STAGE/github/scripts/read_route.py"
mkdir -p "$STAGE/github/.github/workflows"
cp -a "$ROOT/.github/workflows/validate.yml" "$STAGE/github/.github/workflows/validate.yml"

# Local : export compact dérivé, avec les chemins directs d’activation.
cp -a "$ROOT/V1/official" "$STAGE/local/official"
cp -a "$ROOT/skills/design-governance-practice" "$STAGE/local/skill"
cp -a "$ROOT/schemas" "$STAGE/local/schemas"
mkdir -p "$STAGE/local/scripts"
cp -a "$ROOT/scripts/validate_design_governance.py" "$STAGE/local/scripts/validate_design_governance.py"
cp -a "$ROOT/scripts/validate_run_card.py" "$STAGE/local/scripts/validate_run_card.py"
cp -a "$ROOT/scripts/validate_contracts.py" "$STAGE/local/scripts/validate_contracts.py"
cp -a "$ROOT/scripts/package_manifest.json" "$STAGE/local/scripts/package_manifest.json"
cp -a "$ROOT/scripts/validate_all.py" "$STAGE/local/scripts/validate_all.py"
cp -a "$ROOT/scripts/validate_reading_map.py" "$STAGE/local/scripts/validate_reading_map.py"
cp -a "$ROOT/scripts/read_route.py" "$STAGE/local/scripts/read_route.py"
cat > "$STAGE/local/README.md" <<'EOF'
# Design Governance V1.0.0 — export Local

Design Governance V1.0.0 est une expérimentation maintenue qui aide à transformer un brief en proposition de design visuellement dirigée, cultivée, spécifique, construite et polie, puis en travail vérifiable. Il peut servir pour un correctif local, une nouvelle surface, une direction visuelle ou une modification de composant partagé. Son usage recommandé est supervisé ; son efficacité réelle reste à vérifier.

## Commencer en deux minutes

1. Lisez [`official/QUICKSTART.md`](official/QUICKSTART.md).
2. Si les termes `mode`, `risque`, `preuve` ou `run` sont nouveaux, lisez [`official/GLOSSAIRE.md`](official/GLOSSAIRE.md).
3. Si le besoin est déjà identifiable, consultez [`official/READING_MAP.md`](official/READING_MAP.md) pour le premier chemin et la sortie attendue.
4. Écrivez le mode, le risque dominant, la décision à changer, la prochaine preuve et l’owner.
5. Pour une décision visuelle, rendez explicites la présence, le point de vue et le niveau de polish recherchés.
6. Chargez seulement la source utile au mode retenu ; `DIRECTION/START` reste l’unique classification.

## Constitution minimale

Les cinq absolus de `official/DIRECTION.md` protègent la baseline : direction perceptible, ancre inspectable, preuves applicables, déclaration du mode et de la prochaine preuve avant l’exécution, et coordination du réel et du beau. La conformité ne remplace ni la direction ni la preuve.

Pour charger un seul bloc :

```bash
python3 scripts/read_route.py DIRECTION/START
```

Pour renforcer une carte concrète :

```bash
python3 scripts/validate_run_card.py --strict chemin/vers/run_card.json
```

Les cinq sources normatives sont `official/DIRECTION.md`, `official/ACTION.md`, `official/SAVOIR.md`, `official/BIBLIOTHEQUE.md` et `official/CHANGELOG.md`. `README.md`, `QUICKSTART.md` et `GLOSSAIRE.md` orientent la lecture sans créer de règle concurrente.

## Trois cas simples

| Situation | Point de départ |
|---|---|
| Corriger un défaut local, comme un contraste ou un libellé | `LITE` ou `ITER` |
| Créer une première scène qui porte l’identité du produit | `DIRECTION` |
| Modifier un composant ou une convention partagée | `SYSTÈME` |

La projection machine de référence se trouve dans `schemas/run_card.example.json`. Les scripts ne nécessitent aucune dépendance Python tierce et supposent Python 3.10 ou plus récent. Pour contrôler la projection :

```bash
python3 scripts/validate_run_card.py
```

`STATE: CLOSED` signifie que la trace est persistée ; cela ne signifie pas automatiquement que le résultat est accepté ou entièrement vérifié. La validation du package ou de la `RUN_CARD` confirme uniquement les contrôles exécutés ; elle ne prouve ni l’usage, ni l’accessibilité exécutée, ni la performance, ni la qualité visuelle du produit.

Cet export est autonome : il peut être lu, utilisé et contrôlé sans connexion à un dépôt distant.

Les contrôles disponibles sont :

```bash
python3 scripts/validate_design_governance.py
python3 scripts/validate_run_card.py
python3 scripts/validate_reading_map.py
python3 scripts/read_route.py DIRECTION/START
python3 scripts/validate_all.py
```

Dans l’export Local, `validate_all.py` contrôle le package, la projection, les fixtures et la CLI ; le build et la reproductibilité restent contrôlés depuis la distribution GitHub.
EOF

# Vérification de la distribution canonique avant archivage.
python3 "$STAGE/github/scripts/validate_design_governance.py"
python3 "$STAGE/github/scripts/validate_run_card.py"
python3 "$STAGE/github/scripts/validate_contracts.py"
python3 "$STAGE/github/scripts/validate_reading_map.py"

# Valider les chemins relatifs du Local indépendamment, sans exiger la structure GitHub.
python3 - "$STAGE/local" <<'PY'
from pathlib import Path
import re
import sys

root = Path(sys.argv[1])
import json
manifest = json.loads((root / "scripts" / "package_manifest.json").read_text(encoding="utf-8"))
expected = manifest["local"]
for relative in expected:
    if not (root / relative).is_file():
        raise SystemExit(f"Local export missing: {relative}")
for path in root.rglob("*.md"):
    text = path.read_text(encoding="utf-8")
    for target in re.findall(r"\]\(([^)]+)\)", text):
        target = target.split("#", 1)[0]
        if not target or target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (path.parent / target).exists():
            raise SystemExit(f"Broken Local link: {path} -> {target}")
print(f"LOCAL EXPORT PASSED — {len(expected)} fichiers attendus et liens contrôlés")
PY
python3 "$STAGE/local/scripts/validate_design_governance.py"
python3 "$STAGE/local/scripts/validate_run_card.py"
python3 "$STAGE/local/scripts/validate_contracts.py"
python3 "$STAGE/local/scripts/validate_reading_map.py"
python3 "$STAGE/local/scripts/validate_all.py"

# Archives déterministes du contenu, sans répertoire de travail caché.
# Le build nettoie aussi les caches éventuels avant de copier les sources.
find "$STAGE/github" "$STAGE/local" -type d -name '__pycache__' -prune -exec rm -rf {} +
SOURCE_DATE_EPOCH="${SOURCE_DATE_EPOCH:-0}"
find "$STAGE/github" "$STAGE/local" -exec touch -h -d "@$SOURCE_DATE_EPOCH" {} +
(
  cd "$STAGE/github"
  LC_ALL=C find . -type f -print | sort | zip -X -q "$ROOT/Design_Governance_V1_GITHUB.zip" -@
)
(
  cd "$STAGE/local"
  LC_ALL=C find . -type f -print | sort | zip -X -q "$ROOT/Design_Governance_V1_LOCAL.zip" -@
)

# Publier uniquement après validations et archivage réussis.
if [[ -e "$DIST" ]]; then
  mv "$DIST" "$BACKUP"
fi
mv "$STAGE" "$DIST"
rm -rf "$BACKUP" "$WORK"

printf 'Generated:\n  %s\n  %s\n' \
  "$ROOT/Design_Governance_V1_GITHUB.zip" \
  "$ROOT/Design_Governance_V1_LOCAL.zip"


# Projection machine-readable

Cette projection sert au transport entre agents, scripts ou handoffs. Elle ne crée pas de contrat concurrent : `ACTION.md` reste la source d’autorité.

La forme de référence ci-dessous est présentée en YAML pour la lecture. Une version JSON contrôlable et son schéma sont fournis dans `schemas/` :

- `schemas/run_card.schema.json` décrit les champs et les valeurs admises ;
- `schemas/run_card.example.json` est une projection valide ;
- `schemas/fixtures/` contient des cas valides et invalides ;
- `scripts/validate_run_card.py` exécute le contrôle structurel et les invariants sémantiques V1 sans dépendance externe.

```yaml
run_card:
  id: DIRECTION-PREMIUM-001
  owner: design-owner
  date_version: "2026-08-29 / V1"
  mode: DIRECTION
  decision: "Décision dominante à prendre ou vérifier."
  decision_intent: "Décision que le run doit permettre de trancher."
  risk:
    level: normal
    critical_protection: null
  sources:
    - DIRECTION/START
    - ACTION/RUN_CARD
  direction:
    thesis: "Position visuelle située."
    anti_direction:
      - "Pattern générique refusé."
    first_object: "Objet qui matérialise la décision."
  anchors:
    - role: direction
      source: "URL ou référence réellement ouverte"
      date: "2026-08-29"
      scope: "axe ou décision calibré"
      retained:
        - "relation réellement extraite"
      rejected:
        - "surface ou motif copié"
      transformation: "Reformulation en choix propre au produit."
      transformation_status: transformed
      limitation: "Ne prouve ni efficacité ni droit de réemploi."
  artifact:
    locator: "chemin-ou-url-local"
    scope: "Périmètre observé."
  trace_locator: "ticket-ou-chemin-de-run"
  next_proof: "Preuve suivante attendue."
  capability_profile:
    available:
      - "artefact disponible"
    unavailable:
      - "préférence humaine non observée"
    not_required:
      - "participant non requis pour cette passe"
    basis:
      - "capacité déclarée dans le périmètre et les limites du run"
  proof:
    observed:
      - "Observation réellement obtenue dans le scope déclaré."
    not_verified:
      - "Propriété non observée dans le scope."
    provenance:
      artifact_locator: "Artefact réellement inspecté."
      artifact_version: "Version ou identifiant observé."
      method: "Méthode d’inspection ou de test."
      observed_at: "Date ou horodatage de l’observation."
  decision_change:
    value: "Décision effectivement changée, confirmée ou abandonnée."
    evidence: "Artefact ou observation qui l’établit."
  creative_close:
    presence: "Présence effectivement produite dans le scope inspecté."
    signature: "Élément spécifique qui distingue la proposition."
    craft_detail: "Détail ou état révélant le niveau de craft observé."
    dominant_defect: "Défaut créatif restant prioritaire."
    next_polish_action: "Prochaine action de polish ciblée."
  profile_decision:
    decision: "Décision réellement modifiée par le profil."
    dials: "Dials relevés, abaissés ou inchangés."
    counterindication: "Situation où le profil devient nuisible."
    evidence: "Capture, observation ou preuve montrant son effet."
  closure:
    state: CLOSED
    direction_status: HELD
    issue: null
    verdict: ACCEPTED-WITH-RESERVATION
    limitations:
      - "Limite restante."
```

Préserver les distinctions entre `STATE`, `ISSUE`, `VERDICT`, statut de direction, `GATE`, `AXIS` et `DECISION-CHANGE`. Le `closure.verdict` global utilise uniquement les six valeurs d’ACTION. Utiliser `PASS`, `PASS-WITH-RESERVATION`, `NOT-VERIFIED`, `NOT-OBSERVED` et `N/A-JUSTIFIED` pour les axes, les contrôles ou les limites selon leur sens propre ; ils ne deviennent pas des verdicts globaux. `null` ne signifie ni réussite ni preuve absente.

`CLOSED` signifie que la trace et les artefacts sont persistés. Pour un verdict `ACCEPTED` ou `ACCEPTED-WITH-RESERVATION`, `proof.provenance` est obligatoire et doit identifier l’artefact, sa version, la méthode et la date d’observation. Pour une RUN_CARD `DIRECTION` clôturée, `creative_close` est obligatoire et doit contenir `presence`, `signature`, `craft_detail`, `dominant_defect` et `next_polish_action`. Lorsqu’une route `SAVOIR/STYLE` est activée, `profile_decision` peut transporter la décision, les dials, la contre-indication et la preuve de son effet ; s’il est présent, ses quatre champs sont obligatoires. Il peut coexister avec `RETURN`, `EXPLORATORY` ou une issue déclarée ; un axe ou une preuve peut rester `NOT-VERIFIED`. Il ne doit jamais être interprété comme un verdict positif.

Lorsqu’un risque est `critical`, `critical_protection` est un objet structuré qui identifie le contrôle, son owner, son scope, l’action en cas d’échec (`RETURNED`, `BLOCKED` ou `ESCALATED`) et le locator de la preuve attendue. Un texte générique, un placeholder ou une promesse non localisable ne constitue pas une protection critique. Pour un verdict accepté, le locator de provenance doit également correspondre au locator de l’artefact déclaré ; cette cohérence ne prouve toutefois pas que l’artefact existe ou que la méthode a effectivement été exécutée.

Ne jamais introduire `SELF-DECLARED`, `ATLAS-PASS`, `POLISHED`, `SLOP-FREE` ou un score esthétique. Valider les clés avec le script fourni lorsque la projection est utilisée, mais ne jamais traiter cette projection comme une preuve ou une clôture automatique.


import json
def compact_card(d):
    lines = ["{", '  "run_card": {']
    items = list(d["run_card"].items())
    for i, (k, v) in enumerate(items):
        lines.append(f'    {json.dumps(k, ensure_ascii=False)}: {json.dumps(v, ensure_ascii=False)}' + ("," if i < len(items) - 1 else ""))
    lines += ["  }", "}"]
    return "\n".join(lines)
def style_of(text):
    d = json.loads(text)
    tail = text[len(text.rstrip("\n")):]
    if json.dumps(d, ensure_ascii=False, indent=2) + tail == text:
        return ("indent2", tail)
    if isinstance(d, dict) and set(d) == {"run_card"} and compact_card(d) + tail == text:
        return ("compact_card", tail)
    return ("other", tail)
def dump(d, style):
    kind, tail = style
    if kind == "compact_card":
        return compact_card(d) + tail
    return json.dumps(d, ensure_ascii=False, indent=2) + tail

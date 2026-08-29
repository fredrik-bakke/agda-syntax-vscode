#!/usr/bin/env python3

import json
import re
import subprocess
import tempfile
from pathlib import Path


BACKREF = re.compile(r"(?<!\\)((?:\\\\)*)\\(?:[1-9][0-9]*|k<[^>]+>)")


def sanitize(value):
    for key in {"end", "while"}:
        if isinstance(value.get(key), str):
            value[key] = BACKREF.sub(r"\1(?:)", value[key])
    return value


with tempfile.TemporaryDirectory() as directory:
    temporary = Path(directory)
    grammars = []
    for source in sorted(Path("syntaxes").glob("*.tmLanguage.json")):
        grammars.append(
            json.loads(source.read_text(encoding="utf-8"), object_hook=sanitize)
        )
    target = temporary / "grammars.json"
    target.write_text(json.dumps({"patterns": grammars}), encoding="utf-8")
    result = subprocess.run(
        ["npx", "--no-install", "textmate-validate", "-v", "--compact", target]
    )
    if result.returncode:
        raise SystemExit(result.returncode)

#!/usr/bin/env python3

import json
from itertools import chain
from pathlib import Path

from ruamel.yaml import YAML


yaml = YAML(typ="safe")
yaml.version = (1, 2)
yaml.constructor.add_constructor(
    "tag:yaml.org,2002:value", lambda constructor, node: constructor.construct_scalar(node)
)

sources = chain(
    Path("syntaxes").glob("*.tmLanguage.yml"),
    Path("syntaxes").glob("*.tmLanguage.yaml"),
)
for source in sorted(sources):
    grammar = yaml.load(source.read_text(encoding="utf-8"))
    output = json.dumps(grammar, ensure_ascii=False, separators=(",", ":"))
    source.with_suffix(".json").write_text(output + "\n", encoding="utf-8")

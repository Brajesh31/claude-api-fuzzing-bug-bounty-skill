#!/usr/bin/env python3
"""List paths and HTTP methods from a local OpenAPI/Swagger JSON document.

This is a passive document parser. It does not send requests or test a target.
"""
import argparse
import json
from pathlib import Path

METHODS = {"get", "post", "put", "patch", "delete", "options", "head", "trace"}


def load_spec(path: Path):
    text = path.read_text(encoding="utf-8")
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        try:
            import yaml  # Optional dependency for YAML OpenAPI documents.
        except ImportError as exc:
            raise SystemExit("Input is not JSON. Install PyYAML to parse YAML: python -m pip install pyyaml") from exc
        return yaml.safe_load(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("spec", type=Path, help="Local Swagger/OpenAPI JSON or YAML file")
    parser.add_argument("--include-parameters", action="store_true", help="Also show path-level parameter names")
    args = parser.parse_args()
    if not args.spec.is_file():
        parser.error(f"file not found: {args.spec}")
    spec = load_spec(args.spec)
    if not isinstance(spec, dict) or not isinstance(spec.get("paths"), dict):
        parser.error("document does not contain an OpenAPI/Swagger 'paths' object")

    count = 0
    for path, item in sorted(spec["paths"].items()):
        if not isinstance(item, dict):
            continue
        for method, operation in sorted(item.items()):
            if method.lower() not in METHODS or not isinstance(operation, dict):
                continue
            count += 1
            operation_id = operation.get("operationId", "")
            summary = operation.get("summary", "")
            print(f"{method.upper():7} {path}  {operation_id or summary}".rstrip())
            if args.include_parameters:
                params = item.get("parameters", []) + operation.get("parameters", [])
                names = [p.get("name", "?") for p in params if isinstance(p, dict)]
                if names:
                    print("        parameters: " + ", ".join(names))
    print(f"\nFound {count} documented operation(s). This is an inventory only, not a security test.")


if __name__ == "__main__":
    main()

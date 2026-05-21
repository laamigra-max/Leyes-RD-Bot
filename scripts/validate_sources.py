"""
Validate legal source documents for Leyes-RD-Bot.

This script checks whether Markdown legal documents include the minimum
metadata required before being used as legal sources by the bot.
"""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[1]

LEGAL_FOLDERS = [
    "constitucion",
    "consumidor",
    "civil",
    "penal",
    "inmobiliario",
    "administrativo",
    "bancario",
    "tributario",
    "laboral",
    "familia",
    "transito",
    "jurisprudencia",
]

REQUIRED_FIELDS = [
    "titulo",
    "numero",
    "tipo_norma",
    "pais",
    "materia",
    "autoridad_emisora",
    "fuente_oficial",
    "tipo_fuente",
    "url_descarga_pdf",
    "archivo_original_pdf",
    "estado_vigencia",
    "ultima_revision_repo",
]

def extract_front_matter(content: str) -> str | None:
    """
    Extract YAML-style front matter from a Markdown document.
    Expected format:
    ---
    campo: valor
    ---
    """
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    return match.group(1)


def validate_document(path: Path) -> list[str]:
    errors = []

    content = path.read_text(encoding="utf-8")

    front_matter = extract_front_matter(content)

    if front_matter is None:
        errors.append("Missing front matter block.")
        return errors

    for field in REQUIRED_FIELDS:
        pattern = rf"^{field}\s*:"
        if not re.search(pattern, front_matter, re.MULTILINE):
            errors.append(f"Missing required metadata field: {field}")

    if "## Artículo" not in content and "## Articulo" not in content:
        errors.append("No article sections found. Expected '## Artículo' or '## Articulo'.")

    return errors


def main() -> int:
    markdown_files = []

    for folder in LEGAL_FOLDERS:
        folder_path = ROOT / folder
        if folder_path.exists():
            markdown_files.extend(folder_path.glob("*.md"))

    if not markdown_files:
        print("No legal Markdown documents found to validate.")
        return 0

    has_errors = False

    for path in markdown_files:
        errors = validate_document(path)

        if errors:
            has_errors = True
            print(f"\nERROR: {path.relative_to(ROOT)}")
            for error in errors:
                print(f"  - {error}")
        else:
            print(f"OK: {path.relative_to(ROOT)}")

    if has_errors:
        print("\nValidation failed.")
        return 1

    print("\nAll legal documents passed validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

"""
Chunk legal Markdown documents by article for Leyes-RD-Bot.

This script reads a Markdown legal document and extracts article-based chunks.
The output is a JSON file that can later be used for search indexing.
"""

from pathlib import Path
import hashlib
import json
import re
import sys


ROOT = Path(__file__).resolve().parents[1]


ARTICLE_PATTERN = re.compile(
    r"(?P<header>^##\s+Art[ií]culo\s+(?P<number>[A-Za-z0-9\-\.]+).*?$)",
    re.MULTILINE,
)


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def extract_front_matter(content: str) -> str:
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return ""

    return match.group(1)


def parse_simple_front_matter(front_matter: str) -> dict:
    metadata = {}

    for line in front_matter.splitlines():
        if ":" in line and not line.strip().startswith("-"):
            key, value = line.split(":", 1)
            metadata[key.strip()] = value.strip().strip('"').strip("'")

    return metadata


def chunk_by_articles(content: str, source_file: str) -> list[dict]:
    front_matter = extract_front_matter(content)
    metadata = parse_simple_front_matter(front_matter)

    matches = list(ARTICLE_PATTERN.finditer(content))

    chunks = []

    for index, match in enumerate(matches):
        start = match.start()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(content)

        article_text = content[start:end].strip()
        article_number = match.group("number").strip()

        document_id = metadata.get("numero", Path(source_file).stem).replace(" ", "_")

        chunk = {
            "id_chunk": f"{document_id}_art_{article_number}".lower(),
            "titulo_norma": metadata.get("titulo", ""),
            "numero_norma": metadata.get("numero", ""),
            "tipo_norma": metadata.get("tipo_norma", ""),
            "materia": metadata.get("materia", ""),
            "articulo": article_number,
            "texto": article_text,
            "archivo_repo": source_file,
            "fuente_oficial": metadata.get("fuente_oficial", ""),
            "url_oficial": metadata.get("fuente_oficial", ""),
            "estado_vigencia": metadata.get("estado_vigencia", ""),
            "ultima_revision_repo": metadata.get("ultima_revision_repo", ""),
            "hash_texto": sha256_text(article_text),
        }

        chunks.append(chunk)

    return chunks


def main() -> int:
    if len(sys.argv) != 3:
        print("Usage:")
        print("  python scripts/chunk_laws.py <input_markdown> <output_json>")
        print("")
        print("Example:")
        print("  python scripts/chunk_laws.py consumidor/ley_358_05_proteccion_consumidor.md embeddings/ley_358_05_chunks.json")
        return 1

    input_markdown = ROOT / sys.argv[1]
    output_json = ROOT / sys.argv[2]

    if not input_markdown.exists():
        print(f"Input file not found: {input_markdown}")
        return 1

    content = input_markdown.read_text(encoding="utf-8")
    chunks = chunk_by_articles(content, sys.argv[1])

    output_json.parent.mkdir(parents=True, exist_ok=True)
    output_json.write_text(
        json.dumps(chunks, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Created chunks: {len(chunks)}")
    print(f"Output: {output_json}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

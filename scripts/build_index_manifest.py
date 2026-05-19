"""
Build index manifest for Leyes-RD-Bot.

This script scans JSON chunk files in the embeddings folder and updates
embeddings/index_manifest.json with document and chunk metadata.
"""

from pathlib import Path
from datetime import datetime, timezone
import json
import sys


ROOT = Path(__file__).resolve().parents[1]
EMBEDDINGS_DIR = ROOT / "embeddings"
MANIFEST_PATH = EMBEDDINGS_DIR / "index_manifest.json"


def load_chunks(chunk_file: Path) -> list[dict]:
    try:
        data = json.loads(chunk_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"Invalid JSON file: {chunk_file}") from exc

    if not isinstance(data, list):
        raise ValueError(f"Chunk file must contain a JSON list: {chunk_file}")

    return data


def build_document_record(chunk_file: Path, chunks: list[dict]) -> dict:
    first_chunk = chunks[0] if chunks else {}

    return {
        "id_documento": chunk_file.stem.replace("_chunks", ""),
        "titulo": first_chunk.get("titulo_norma", ""),
        "numero": first_chunk.get("numero_norma", ""),
        "tipo_norma": first_chunk.get("tipo_norma", ""),
        "materia": first_chunk.get("materia", ""),
        "archivo_repo": first_chunk.get("archivo_repo", ""),
        "fuente_oficial": first_chunk.get("fuente_oficial", ""),
        "url_oficial": first_chunk.get("url_oficial", ""),
        "estado_vigencia": first_chunk.get("estado_vigencia", ""),
        "fecha_indexacion": datetime.now(timezone.utc).date().isoformat(),
        "total_chunks": len(chunks),
        "estado_indexacion": "indexado" if chunks else "error",
        "chunk_file": str(chunk_file.relative_to(ROOT)),
    }


def main() -> int:
    EMBEDDINGS_DIR.mkdir(parents=True, exist_ok=True)

    chunk_files = sorted(EMBEDDINGS_DIR.glob("*_chunks.json"))

    documents = []

    for chunk_file in chunk_files:
        chunks = load_chunks(chunk_file)
        document_record = build_document_record(chunk_file, chunks)
        documents.append(document_record)

    manifest = {
        "project": "Leyes-RD-Bot",
        "version": "1.0.0",
        "country": "República Dominicana",
        "description": "Manifest del índice legal usado por el bot jurídico dominicano.",
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "status": "ready" if documents else "pending",
        "total_documents": len(documents),
        "documents": documents,
        "notes": [
            "Este archivo registra los documentos legales procesados para búsqueda semántica.",
            "Cada documento indexado debe incluir metadata, fuente oficial, archivo del repositorio, estado de vigencia y total de chunks.",
            "El bot no debe usar documentos que no estén correctamente registrados o validados."
        ]
    }

    MANIFEST_PATH.write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    print(f"Manifest updated: {MANIFEST_PATH.relative_to(ROOT)}")
    print(f"Documents indexed: {len(documents)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())

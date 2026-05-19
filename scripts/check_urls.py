"""
Check official source URLs for Leyes-RD-Bot.

This script scans Markdown legal documents and checks whether URLs declared
in the fuente_oficial metadata are reachable.
"""

from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
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


def extract_front_matter(content: str) -> str | None:
    match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
    if not match:
        return None

    return match.group(1)


def extract_fuente_oficial(front_matter: str) -> str | None:
    match = re.search(r"^fuente_oficial\s*:\s*[\"']?(.*?)[\"']?\s*$", front_matter, re.MULTILINE)
    if not match:
        return None

    value = match.group(1).strip()

    if not value or not value.startswith(("http://", "https://")):
        return None

    return value


def check_url(url: str, timeout: int = 15) -> tuple[bool, str]:
    request = Request(
        url,
        headers={
            "User-Agent": "Leyes-RD-Bot URL Checker/1.0"
        },
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            status_code = response.getcode()
            if 200 <= status_code < 400:
                return True, f"OK HTTP {status_code}"
            return False, f"Unexpected HTTP {status_code}"

    except HTTPError as exc:
        return False, f"HTTP error {exc.code}"

    except URLError as exc:
        return False, f"URL error: {exc.reason}"

    except Exception as exc:
        return False, f"Unexpected error: {exc}"


def main() -> int:
    markdown_files = []

    for folder in LEGAL_FOLDERS:
        folder_path = ROOT / folder
        if folder_path.exists():
            markdown_files.extend(folder_path.glob("*.md"))

    if not markdown_files:
        print("No legal Markdown documents found.")
        return 0

    has_errors = False

    for path in markdown_files:
        content = path.read_text(encoding="utf-8")
        front_matter = extract_front_matter(content)

        if not front_matter:
            continue

        url = extract_fuente_oficial(front_matter)

        if not url:
            print(f"SKIP: {path.relative_to(ROOT)} - No valid fuente_oficial URL found.")
            continue

        ok, message = check_url(url)

        if ok:
            print(f"OK: {path.relative_to(ROOT)} - {url} - {message}")
        else:
            has_errors = True
            print(f"ERROR: {path.relative_to(ROOT)} - {url} - {message}")

    if has_errors:
        print("\nURL check failed.")
        return 1

    print("\nAll checked URLs are reachable.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

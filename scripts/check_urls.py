"""
Check official source URLs for Leyes-RD-Bot.

This script scans Markdown legal documents and checks whether URLs declared
in the fuente_oficial metadata are reachable.

Important:
Some official Dominican government websites may timeout from GitHub Actions.
A timeout should be reported as a warning, not as a hard failure, because the
legal source may still be valid and manually verified.
"""

from pathlib import Path
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import socket
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
    match = re.search(
        r"^fuente_oficial\s*:\s*[\"']?(.*?)[\"']?\s*$",
        front_matter,
        re.MULTILINE,
    )

    if not match:
        return None

    value = match.group(1).strip()

    if not value or not value.startswith(("http://", "https://")):
        return None

    return value


def check_url(url: str, timeout: int = 30) -> tuple[str, str]:
    request = Request(
        url,
        headers={
            "User-Agent": "Mozilla/5.0 Leyes-RD-Bot URL Checker/1.0"
        },
    )

    try:
        with urlopen(request, timeout=timeout) as response:
            status_code = response.getcode()

            if 200 <= status_code < 400:
                return "ok", f"OK HTTP {status_code}"

            return "error", f"Unexpected HTTP {status_code}"

    except HTTPError as exc:
        return "error", f"HTTP error {exc.code}"

    except socket.timeout:
        return "warning", "URL check timed out"

    except TimeoutError:
        return "warning", "URL check timed out"

    except URLError as exc:
        reason = str(exc.reason).lower()

        if "timed out" in reason or "timeout" in reason:
            return "warning", f"URL check timed out: {exc.reason}"

        return "warning", f"URL warning: {exc.reason}"

    except Exception as exc:
        return "warning", f"URL warning: {exc}"


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

        status, message = check_url(url)

        if status == "ok":
            print(f"OK: {path.relative_to(ROOT)} - {url} - {message}")

        elif status == "warning":
            print(f"WARNING: {path.relative_to(ROOT)} - {url} - {message}")

        else:
            has_errors = True
            print(f"ERROR: {path.relative_to(ROOT)} - {url} - {message}")

    if has_errors:
        print("\nURL check failed.")
        return 1

    print("\nURL check completed. Warnings do not fail the workflow.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

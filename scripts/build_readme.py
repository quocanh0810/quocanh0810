from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FRAG_DIR = ROOT / "fragments"
OUT = ROOT / "README.md"

ORDER = [
    "header.md",
    "tech.md",
    "extras.md",
]

def main():
    parts = []
    for fname in ORDER:
        fpath = FRAG_DIR / fname
        if not fpath.exists():
            raise FileNotFoundError(f"error: {fname}")
        parts.append(fpath.read_text(encoding="utf-8").strip())

    content = "\n\n---\n\n".join(parts) + "\n"
    OUT.write_text(content, encoding="utf-8")
    print("Built readme successfully!")

if __name__ == "__main__":
    main()

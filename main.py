"""The Internet in One Word — make.fun entry.

Writes one word to /output/entry.txt.
"""
import os

LINE = "elsewhere".strip()
assert LINE and " " not in LINE and "\n" not in LINE, "entry must be exactly one word"

def main():
    assert len(LINE) <= 40, "entry word is unexpectedly long"
    out = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")
    os.chmod(path, 0o644)
    print(LINE)

if __name__ == "__main__":
    main()

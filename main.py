"""Entry program for the ai-excited-01 bounty.

Copies the bundled entry.png next to this file into the output directory
named by MAKEFUN_OUTPUT_DIR (falling back to /output), then checks the
copy's size so a truncated write is caught immediately. Standard library
only, no network, and fully deterministic: the same input bytes always
produce the same output bytes.
"""

import os
import shutil

SOURCE_NAME = "entry.png"
MAX_BYTES = 1048576


def output_path():
    """Resolve the destination path for the entry image."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(out_dir, SOURCE_NAME)


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)
    if not os.path.isfile(source):
        raise SystemExit(f"missing {SOURCE_NAME} next to main.py; cannot build entry")
    dest = output_path()
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    shutil.copyfile(source, dest)
    copied = os.path.getsize(dest)
    if copied > MAX_BYTES:
        raise SystemExit(f"entry.png is {copied} bytes, over the 1 MiB limit")
    if copied != os.path.getsize(source):
        raise SystemExit("copy size differs from source; output is incomplete")
    print(f"wrote {dest} ({copied} bytes)")


if __name__ == "__main__":
    main()

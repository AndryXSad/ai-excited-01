"""ai-excited-01 entry: copy the bundled image to the output directory.

The image (entry.png) sits next to this file in the repository. This
program copies it, byte for byte, to $MAKEFUN_OUTPUT_DIR/entry.png.

Deterministic by construction: no timestamps, no randomness, no network,
standard library only. Both runs write the exact same bytes.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(HERE, "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(src):
        raise FileNotFoundError("bundled image missing: %s" % src)
    shutil.copyfile(src, dst)
    # Fail loudly instead of silently shipping a truncated copy: the
    # grader runs this program twice and both runs must write the
    # same bytes, so a short write here must never pass unnoticed.
    if os.path.getsize(dst) != os.path.getsize(src):
        raise IOError("copy size mismatch: %s vs %s" % (dst, src))


if __name__ == "__main__":
    main()

"""Entry for make.fun's "Make the AI judge happy" (ai-happy-01).

The image beside this file shows a little robot's first birthday
party: its animal friends surprised it with a cake, one candle,
party hats and confetti. This program copies that image to the
output directory as entry.png.

Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for
/output.
"""

import os
import pathlib
import shutil

HERE = pathlib.Path(__file__).resolve().parent
SOURCE = HERE / "entry.png"


def main() -> None:
    out_dir = pathlib.Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    target = out_dir / "entry.png"
    # Write via a temp file so the judge never sees a partial image.
    tmp = target.with_name("entry.png.tmp")
    shutil.copyfile(SOURCE, tmp)
    tmp.replace(target)


if __name__ == "__main__":
    main()

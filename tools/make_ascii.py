"""Generate dark- and light-mode ASCII portraits from assets/portrait.png.

Writes assets/ascii-art.txt (for dark_mode.svg) and assets/ascii-art-light.txt
(for light_mode.svg). Preserves the 0.54 cell aspect ratio expected by
tools/build_card.py.

Usage:
    python tools/make_ascii.py
"""

from __future__ import annotations

from collections import deque
from pathlib import Path

from PIL import Image, ImageFilter

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "portrait.png"
DARK_OUT = ROOT / "assets" / "ascii-art.txt"
LIGHT_OUT = ROOT / "assets" / "ascii-art-light.txt"

COLS = 74
CELL_ASPECT = 0.54
RAMP = " .:-=+*#%@"


def outer_background_mask(im: Image.Image) -> list[list[bool]]:
    """Return a boolean grid marking the outer white backdrop around the subject."""
    w, h = im.size
    px = im.load()

    mask = Image.new("L", (w, h))
    mpx = mask.load()
    for y in range(h):
        for x in range(w):
            mpx[x, y] = 255 if px[x, y] < 248 else 0

    closed = mask.filter(ImageFilter.MaxFilter(15)).filter(ImageFilter.MinFilter(15))
    cpx = closed.load()

    # Seal subtle cheek/jaw anti-aliased openings so flood-fill stays outside the face.
    for t in range(100):
        for (x0, y0), (x1, y1) in (((113, 215), (125, 280)), ((306, 225), (278, 285))):
            sx = int(x0 + (x1 - x0) * t / 99)
            sy = int(y0 + (y1 - y0) * t / 99)
            for dx in range(-2, 3):
                if 0 <= sx + dx < w and 0 <= sy < h:
                    cpx[sx + dx, sy] = 255

    bg = [[False] * w for _ in range(h)]
    q: deque[tuple[int, int]] = deque()
    for x in range(w):
        if cpx[x, 0] == 0 and px[x, 0] >= 248:
            bg[0][x] = True
            q.append((x, 0))
    for y in range(h):
        for x in (0, w - 1):
            if not bg[y][x] and cpx[x, y] == 0 and px[x, y] >= 248:
                bg[y][x] = True
                q.append((x, y))

    while q:
        cx, cy = q.popleft()
        for nx, ny in ((cx + 1, cy), (cx - 1, cy), (cx, cy + 1), (cx, cy - 1)):
            if 0 <= nx < w and 0 <= ny < h and not bg[ny][nx] and cpx[nx, ny] == 0 and px[nx, ny] >= 248:
                bg[ny][nx] = True
                q.append((nx, ny))
    return bg


def convert(im: Image.Image, bg: list[list[bool]], dark_mode: bool) -> str:
    """Convert grayscale portrait into trimmed ASCII lines for light or dark card."""
    w, h = im.size
    px = im.load()
    rows = round(COLS * CELL_ASPECT * (h / w))
    out: list[str] = []

    for r in range(rows):
        y0, y1 = int(r * h / rows), int((r + 1) * h / rows)
        line: list[str] = []
        for c in range(COLS):
            x0, x1 = int(c * w / COLS), int((c + 1) * w / COLS)
            vals = [px[x, y] for y in range(y0, y1) for x in range(x0, x1)]
            bg_cnt = sum(1 for y in range(y0, y1) for x in range(x0, x1) if bg[y][x])
            tot = len(vals)
            if bg_cnt > tot * 0.55:
                line.append(" ")
                continue
            avg = sum(vals) / tot
            if dark_mode:
                t = max(0.0, (avg - 45.0) / 205.0) ** 0.92
            else:
                t = max(0.0, (250.0 - avg) / 210.0) ** 0.88
            t = min(1.0, t)
            idx = min(len(RAMP) - 1, max(0, int(round(t * (len(RAMP) - 1)))))
            line.append(RAMP[idx])
        out.append("".join(line).rstrip())

    filled = [i for i, l in enumerate(out) if l.strip()]
    body = out[filled[0]: filled[-1] + 1]
    indent = min(len(l) - len(l.lstrip()) for l in body if l.strip())
    return "\n".join(l[indent:] for l in body) + "\n"


def main() -> None:
    im = Image.open(SRC).convert("L")
    bg = outer_background_mask(im)
    DARK_OUT.write_text(convert(im, bg, dark_mode=True), encoding="utf-8")
    LIGHT_OUT.write_text(convert(im, bg, dark_mode=False), encoding="utf-8")
    print(f"wrote {DARK_OUT.name} and {LIGHT_OUT.name} from {SRC.name}")


if __name__ == "__main__":
    main()

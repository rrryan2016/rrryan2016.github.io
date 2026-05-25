#!/usr/bin/env python3
"""Generate the local raster cover image used by the home page."""

from __future__ import annotations

import math
import struct
import zlib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "src" / "assets" / "paper-radar-cover.png"
WIDTH = 1200
HEIGHT = 420


def mix(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3))


def clamp(value: int) -> int:
    return max(0, min(255, value))


def put(canvas: list[list[list[int]]], x: int, y: int, color: tuple[int, int, int], alpha: float = 1.0) -> None:
    if x < 0 or y < 0 or x >= WIDTH or y >= HEIGHT:
        return
    current = canvas[y][x]
    for i in range(3):
        current[i] = clamp(int(current[i] * (1 - alpha) + color[i] * alpha))


def circle(canvas: list[list[list[int]]], cx: int, cy: int, r: int, color: tuple[int, int, int], alpha: float) -> None:
    r2 = r * r
    for y in range(cy - r, cy + r + 1):
        for x in range(cx - r, cx + r + 1):
            d2 = (x - cx) ** 2 + (y - cy) ** 2
            if d2 <= r2:
                edge = min(1.0, max(0.0, (r2 - d2) / max(1, r * 8)))
                put(canvas, x, y, color, alpha * edge)


def line(canvas: list[list[list[int]]], a: tuple[int, int], b: tuple[int, int], color: tuple[int, int, int], alpha: float, width: int = 2) -> None:
    x0, y0 = a
    x1, y1 = b
    steps = max(abs(x1 - x0), abs(y1 - y0), 1)
    for step in range(steps + 1):
        t = step / steps
        x = int(x0 + (x1 - x0) * t)
        y = int(y0 + (y1 - y0) * t)
        circle(canvas, x, y, width, color, alpha)


def rect(canvas: list[list[list[int]]], x0: int, y0: int, x1: int, y1: int, color: tuple[int, int, int], alpha: float) -> None:
    for y in range(max(0, y0), min(HEIGHT, y1)):
        for x in range(max(0, x0), min(WIDTH, x1)):
            put(canvas, x, y, color, alpha)


def make_canvas() -> list[list[list[int]]]:
    canvas: list[list[list[int]]] = []
    top = (16, 52, 68)
    bottom = (238, 241, 232)
    for y in range(HEIGHT):
        row: list[list[int]] = []
        vertical = y / (HEIGHT - 1)
        for x in range(WIDTH):
            horizontal = x / (WIDTH - 1)
            base = mix(top, bottom, vertical * 0.85)
            cool = int(18 * math.sin(horizontal * math.pi * 2.2 + vertical * 2.0))
            row.append([clamp(base[0] + cool), clamp(base[1] + cool // 2), clamp(base[2] + cool // 3)])
        canvas.append(row)
    return canvas


def add_scene(canvas: list[list[list[int]]]) -> None:
    tile_colors = [(54, 108, 102), (93, 143, 119), (198, 168, 91), (64, 89, 117)]
    for row in range(7):
        for col in range(14):
            x = 54 + col * 54 + (row % 2) * 18
            y = 86 + row * 38
            color = tile_colors[(row * 3 + col) % len(tile_colors)]
            alpha = 0.28 + 0.08 * ((row + col) % 3)
            rect(canvas, x, y, x + 42, y + 24, color, alpha)

    orbit = (232, 238, 232)
    for offset, alpha in [(0, 0.26), (34, 0.16), (-38, 0.14)]:
        previous = None
        for degree in range(-30, 214):
            rad = math.radians(degree)
            x = int(860 + math.cos(rad) * (360 + offset))
            y = int(238 + math.sin(rad) * (120 + offset * 0.25))
            if previous is not None:
                line(canvas, previous, (x, y), orbit, alpha, 1)
            previous = (x, y)

    satellite = (244, 239, 224)
    panel = (35, 91, 120)
    body_x, body_y = 836, 108
    rect(canvas, body_x - 16, body_y - 10, body_x + 16, body_y + 10, satellite, 0.94)
    rect(canvas, body_x - 64, body_y - 8, body_x - 22, body_y + 8, panel, 0.92)
    rect(canvas, body_x + 22, body_y - 8, body_x + 64, body_y + 8, panel, 0.92)
    line(canvas, (body_x, body_y + 10), (760, 256), (239, 196, 103), 0.30, 2)
    line(canvas, (body_x, body_y + 10), (914, 256), (239, 196, 103), 0.30, 2)

    nodes = [(985, 255), (1064, 205), (1110, 282), (1032, 325), (930, 318)]
    for a, b in [(0, 1), (1, 2), (2, 3), (3, 4), (4, 0), (0, 3), (1, 4)]:
        line(canvas, nodes[a], nodes[b], (32, 71, 83), 0.38, 2)
    for idx, point in enumerate(nodes):
        color = (239, 196, 103) if idx == 0 else (232, 238, 232)
        circle(canvas, point[0], point[1], 12, color, 0.92)


def write_png(canvas: list[list[list[int]]], path: Path) -> None:
    raw = bytearray()
    for row in canvas:
        raw.append(0)
        for pixel in row:
            raw.extend(pixel)

    def chunk(kind: bytes, data: bytes) -> bytes:
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)

    png = bytearray(b"\x89PNG\r\n\x1a\n")
    png.extend(chunk(b"IHDR", struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 2, 0, 0, 0)))
    png.extend(chunk(b"IDAT", zlib.compress(bytes(raw), 9)))
    png.extend(chunk(b"IEND", b""))
    path.write_bytes(png)


def main() -> None:
    canvas = make_canvas()
    add_scene(canvas)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    write_png(canvas, OUT)
    print(f"Wrote {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

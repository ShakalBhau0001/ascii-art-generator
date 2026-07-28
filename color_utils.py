import colorsys


COLOR_STYLES = [
    "Solid Color",
    "Rainbow",
    "Gradient (2 Colors)",
    "Fire",
    "Ocean",
    "Neon",
    "Pastel",
]


FIRE_STOPS = ["#8B0000", "#FF4500", "#FFA500", "#FFD700"]
OCEAN_STOPS = ["#001F3F", "#0074D9", "#39CCCC", "#7FDBFF"]
NEON_STOPS = ["#FF006E", "#8338EC", "#3A86FF", "#06FFA5"]


def hex_to_rgb(hex_color: str) -> tuple[int, int, int]:
    """Converts '#39FF14' -> (57, 255, 20)."""
    hex_color = hex_color.lstrip("#")
    return tuple(int(hex_color[i : i + 2], 16) for i in (0, 2, 4))


def rgb_to_hex(rgb: tuple[float, float, float]) -> str:
    r, g, b = (max(0, min(255, int(c))) for c in rgb)
    return "#{:02x}{:02x}{:02x}".format(r, g, b)


def interpolate_color(hex1: str, hex2: str, t: float) -> str:
    """Blends two hex colors together. t=0 -> hex1, t=1 -> hex2."""
    t = max(0.0, min(1.0, t))
    r1, g1, b1 = hex_to_rgb(hex1)
    r2, g2, b2 = hex_to_rgb(hex2)
    r = r1 + (r2 - r1) * t
    g = g1 + (g2 - g1) * t
    b = b1 + (b2 - b1) * t
    return rgb_to_hex((r, g, b))


def multi_stop_gradient(position: float, stops: list[str]) -> str:
    """Interpolates across several color stops evenly spaced from 0.0 to 1.0."""
    position = max(0.0, min(1.0, position))
    segments = len(stops) - 1
    if segments <= 0:
        return stops[0]
    scaled = position * segments
    idx = min(int(scaled), segments - 1)
    t = scaled - idx
    return interpolate_color(stops[idx], stops[idx + 1], t)


def rainbow_color(position: float) -> str:
    """Full-saturation rainbow, position 0.0-1.0 across the width of the art."""
    position = max(0.0, min(1.0, position))
    r, g, b = colorsys.hsv_to_rgb(position, 0.85, 0.95)
    return rgb_to_hex((r * 255, g * 255, b * 255))


def pastel_color(position: float) -> str:
    """Soft, low-saturation rainbow — easier on the eyes, good for light themes."""
    position = max(0.0, min(1.0, position))
    r, g, b = colorsys.hsv_to_rgb(position, 0.35, 0.98)
    return rgb_to_hex((r * 255, g * 255, b * 255))


# Single source of truth for "what color is the character at this position"


def resolve_color(
    position: float, style: str, color1: str = "#39FF14", color2: str = "#FF00FF"
) -> str:
    """
    position: 0.0 (left edge) to 1.0 (right edge) of the art
    style: one of COLOR_STYLES
    color1/color2: user-picked hex colors, only used by "Solid Color" and "Gradient"
    """
    if style == "Solid Color":
        return color1
    if style == "Rainbow":
        return rainbow_color(position)
    if style == "Gradient (2 Colors)":
        return interpolate_color(color1, color2, position)
    if style == "Fire":
        return multi_stop_gradient(position, FIRE_STOPS)
    if style == "Ocean":
        return multi_stop_gradient(position, OCEAN_STOPS)
    if style == "Neon":
        return multi_stop_gradient(position, NEON_STOPS)
    if style == "Pastel":
        return pastel_color(position)
    return color1  # safe fallback


def render_html_preview(grid: list[str], get_color_rgb) -> str:
    if not grid:
        return ""

    lines_html = []
    for row_idx, row in enumerate(grid):
        chars_html = []
        for col_idx, ch in enumerate(row):
            if ch == " ":
                chars_html.append("&nbsp;")
                continue
            r, g, b = get_color_rgb(row_idx, col_idx)
            hexcode = rgb_to_hex((r, g, b))
            safe_ch = ch.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
            chars_html.append(f'<span style="color:{hexcode}">{safe_ch}</span>')
        lines_html.append("".join(chars_html))

    body = "<br>".join(lines_html)
    return (
        '<pre style="background:#111111;color:#eee;padding:1em;border-radius:8px;'
        "line-height:1.15;overflow-x:auto;font-family:Consolas,'DejaVu Sans Mono',monospace;\">"
        f"{body}</pre>"
    )

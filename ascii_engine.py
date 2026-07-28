import pyfiglet

SYMBOL_OPTIONS = {
    "@  Bold": "@",
    "#  Sharp": "#",
    "$  Money": "$",
    "|  Minimal": "|",
    "█  Solid Block": "█",
    "▓  Dark Shade": "▓",
    "▒  Medium Shade": "▒",
    "░  Light Shade": "░",
    "%  Percent": "%",
    "&  Ampersand": "&",
    "*  Star": "*",
    "+  Plus": "+",
    "~  Wave": "~",
    "Custom...": None,
}


def generate_ascii_grid(text: str, font: str = "block") -> list[str]:
    """
    Converts input text into a list of ASCII-art rows using pyfiglet.
    "block" is used deliberately: it keeps clear, generous spacing between
    letters. Fancier fonts like "ansi_shadow" are tightly kerned with little
    to no gap between characters — once every filled pixel is swapped for a
    single symbol (see apply_character), neighboring letters visually merge
    into an unreadable blob. "block" avoids that and stays legible.
    Falls back to a safer font if the chosen font can't render the text.
    """
    if not text or not text.strip():
        return []

    try:
        raw = pyfiglet.figlet_format(text, font=font)
    except pyfiglet.FontNotFound:
        raw = pyfiglet.figlet_format(text, font="standard")

    rows = raw.rstrip("\n").split("\n")

    while rows and rows[0].strip() == "":
        rows.pop(0)
    while rows and rows[-1].strip() == "":
        rows.pop()

    return rows


def apply_character(grid: list[str], symbol: str) -> list[str]:
    """
    Replaces every non-space 'pixel' in the grid with the user's chosen symbol.
    Falls back to '*' if no valid single-character symbol is given.
    """
    if not symbol:
        symbol = "*"
    symbol = symbol[0]

    return ["".join(symbol if ch != " " else " " for ch in row) for row in grid]


def grid_is_empty(grid: list[str]) -> bool:
    return not grid or all(row.strip() == "" for row in grid)


def grid_width(grid: list[str]) -> int:
    return max((len(row) for row in grid), default=0)

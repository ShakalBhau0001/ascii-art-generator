import io
import os
from fpdf import FPDF

ASSETS_DIR = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets"
)
FONT_REGULAR = os.path.join(ASSETS_DIR, "DejaVuSansMono.ttf")
FONT_BOLD = os.path.join(ASSETS_DIR, "DejaVuSansMono-Bold.ttf")


def export_pdf(grid: list[str], get_color_rgb) -> io.BytesIO:
    width = max((len(row) for row in grid), default=1) or 1

    if width > 90:
        orientation = "L"
        font_size = 6
    elif width > 60:
        orientation = "L"
        font_size = 8
    else:
        orientation = "P"
        font_size = 11

    pdf = FPDF(unit="pt", format="A4", orientation=orientation)
    pdf.add_page()
    pdf.add_font("DejaVuMono", "", FONT_REGULAR)
    pdf.set_font("DejaVuMono", size=font_size)
    cell_w = font_size * 0.62
    line_height = font_size + 3

    for row_idx, row in enumerate(grid):
        for col_idx, ch in enumerate(row):
            if ch != " ":
                r, g, b = get_color_rgb(row_idx, col_idx)
                pdf.set_text_color(r, g, b)
                pdf.cell(cell_w, line_height, ch, ln=0)
            else:
                pdf.cell(cell_w, line_height, "", ln=0)
        pdf.ln(line_height)

    buffer = io.BytesIO()
    pdf.output(buffer)
    buffer.seek(0)
    return buffer

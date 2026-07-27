import streamlit as st
from ascii_engine import (
    generate_ascii_grid,
    apply_character,
    grid_is_empty,
    grid_width,
    SYMBOL_OPTIONS,
)
from color_utils import resolve_color, hex_to_rgb, COLOR_STYLES, render_html_preview
from exporters.docx_export import export_docx
from exporters.pdf_export import export_pdf

# Page setup

st.set_page_config(page_title="ASCII Art Generator", page_icon="🎨", layout="wide")
st.title("🎨 ASCII Art Generator")
st.caption(
    "Turn text into colorful ASCII art — pick your symbol, your colors, and your format."
)


FORMAT_OPTIONS = [".docx", ".pdf"]


def safe_filename(text: str, fallback: str = "ascii_art") -> str:
    cleaned = "".join(c for c in text if c.isalnum() or c in ("_", "-"))
    return cleaned[:40] or fallback


def color_style_controls(key_prefix: str):
    """
    Renders the 'Color Style' dropdown plus whatever color picker(s) that
    style needs. Returns (style, color1, color2).
    """
    style = st.selectbox("Color Style", COLOR_STYLES, key=f"{key_prefix}_style")

    color1, color2 = "#39FF14", "#00D4FF"
    if style == "Solid Color":
        color1 = st.color_picker("Pick a color", "#39FF14", key=f"{key_prefix}_c1")
    elif style == "Gradient (2 Colors)":
        c1, c2 = st.columns(2)
        with c1:
            color1 = st.color_picker("Start color", "#FF6EC7", key=f"{key_prefix}_c1")
        with c2:
            color2 = st.color_picker("End color", "#00D4FF", key=f"{key_prefix}_c2")
    elif style in ("Fire", "Ocean", "Neon", "Pastel", "Rainbow"):
        st.caption(f"🎨 '{style}' is a ready-made preset — no color picker needed.")
    return style, color1, color2


def download_controls(grid, get_color_rgb, out_format, base_name):
    """Renders the format-specific download button for a finished grid."""
    if out_format == ".docx":
        buffer = export_docx(grid, get_color_rgb)
        st.download_button(
            "⬇ Download .docx",
            buffer,
            file_name=f"{base_name}_ascii.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            use_container_width=True,
        )
    else:
        buffer = export_pdf(grid, get_color_rgb)
        st.download_button(
            "⬇ Download .pdf",
            buffer,
            file_name=f"{base_name}_ascii.pdf",
            mime="application/pdf",
            use_container_width=True,
        )


tab_text, tab_help, tab_about = st.tabs(
    ["✍️ Text to ASCII", "❓ Instructions", "ℹ️ About"]
)


# TAB 1 — Text to ASCII

with tab_text:
    controls_col, preview_col = st.columns([1, 2], gap="large")

    with controls_col:
        st.subheader("Settings")

        text = st.text_input(
            "Enter your text", max_chars=20, placeholder="e.g. HELLO", key="txt_input"
        )
        st.caption(f"{len(text)}/20 characters")

        symbol_choice = st.selectbox(
            "Character Style", list(SYMBOL_OPTIONS.keys()), key="txt_symbol"
        )
        symbol = SYMBOL_OPTIONS[symbol_choice]
        if symbol_choice == "Custom...":
            custom_symbol = st.text_input(
                "Custom character (1 symbol)", max_chars=1, value="*", key="txt_custom"
            )
            symbol = custom_symbol.strip()[:1] or "*"
        else:
            st.caption(
                f"Symbol sample: {symbol * 5}  ·  your actual text preview appears on the right →"
            )

        style, color1, color2 = color_style_controls("txt")
        out_format = st.selectbox(
            "Download as", FORMAT_OPTIONS, index=0, key="txt_format"
        )

    with preview_col:
        st.subheader("Preview")
        if text.strip():
            grid = generate_ascii_grid(text)
            grid = apply_character(grid, symbol)

            if grid_is_empty(grid):
                st.warning(
                    "⚠️ Some characters in your text couldn't be converted to ASCII art. "
                    "Try standard letters, numbers, or punctuation."
                )
            else:
                width = grid_width(grid) or 1
                if width > 90:
                    st.caption(
                        "📏 This art is quite wide — PDF will auto-switch to landscape."
                    )

                def get_color_rgb(
                    row_idx, col_idx, _w=width, _style=style, _c1=color1, _c2=color2
                ):
                    hexcode = resolve_color(col_idx / _w, _style, _c1, _c2)
                    return hex_to_rgb(hexcode)

                html_preview = render_html_preview(grid, get_color_rgb)
                st.markdown(html_preview, unsafe_allow_html=True)

                st.divider()
                base_name = safe_filename(text)
                download_controls(grid, get_color_rgb, out_format, base_name)
        else:
            st.info(
                "👈 Type something in the settings panel to see your ASCII art appear here."
            )


# TAB 2 — Instructions / Help

with tab_help:
    st.subheader("❓ How to use the ASCII Art Generator")
    st.markdown("""
Welcome! This app turns any short word into big, colorful ASCII art in just a few clicks.
Here's how to get started 👇

### 🚀 Quick start (3 steps)
1. **Type your text** — go to the **✍️ Text to ASCII** tab and type a word (up to 20 letters) in the
   **Enter your text** box. Try `HELLO` to see how it works!
2. **Watch it appear** — as soon as you type, your art shows up on the right side of the screen,
    already in color. No extra button needed.
3. **Download it** — pick **.docx** or **.pdf** from the **Download as** dropdown, then click the
    download button. Done!

### 🖌️ Making it your own
- **Character Style** — this changes *what your letters are built out of*. For example, choosing
    `█ Solid Block` draws your text using solid blocks, while `@ Bold` uses `@` symbols instead.
  Pick **Custom...** if you want to use your own single symbol (like `*` or `+`).
- **Color Style** — this changes how your art is colored:
  - 🎯 **Solid Color** — one flat color of your choice
  - 🌈 **Rainbow** — a full spectrum of colors, left to right
  - 🎚️ **Gradient (2 Colors)** — smoothly blends between two colors you pick
  - 🔥 **Fire**, 🌊 **Ocean**, 💜 **Neon**, 🌸 **Pastel** — one-click ready-made color themes

### 📄 Why only .docx and .pdf?
Colors need a file format that can actually store them — plain `.txt` files can only hold letters,
not colors, so it isn't offered here. Downloading as **.docx** or **.pdf** guarantees your art looks
on paper (or in Word) exactly the way it looked on your screen.

### 💡 Handy tips
- Shorter words (under ~12 letters) fit more neatly on a single printed page.
- Typed something wide? No worries — the PDF automatically switches to landscape so nothing gets cut off.
- Not sure what to type? Try your name, a nickname, or a short greeting like `HI` or `WOW`.
""")


# TAB 3 — About

with tab_about:
    st.subheader("ℹ️ About this project")
    st.markdown("""
**ASCII Art Generator** is a small creative tool built with **Streamlit** and Python. It turns
short text into ASCII art — art made entirely out of text characters — and lets you color it
and export it as a document you can share or print.

#### How it works, in short
- **Text art** is built using the `pyfiglet` library, which turns letters into large block shapes;
    the app then swaps every "filled" pixel for whichever character you chose.
- **Color** is calculated per-character using the same logic across the on-screen preview, the DOCX
    export, and the PDF export, so what you see is always exactly what you get in the downloaded file.

#### Tech stack
| Piece | Library |
|---|---|
| Web interface | Streamlit |
| Text-to-art rendering | pyfiglet |
| Word document export | python-docx |
| PDF export | fpdf2 (with an embedded DejaVu Sans Mono font for block characters) |

#### Credits & notes
Built as a personal project for making shareable ASCII banners and art. Not affiliated with any
of the underlying open-source libraries beyond using them — full credit to their respective maintainers.
""")

# 🎨 ASCII Art Generator

### Text → Colorful ASCII Art — Modern Streamlit App with DOCX & PDF Export

**ASCII Art Generator** is a clean, modern, and beginner-friendly web app built entirely in **Python (3.12.x compatible)**.
It turns any short word or phrase into large, colorful ASCII art — no design tools, no manual character drawing, just type and download.

Using a simple two-panel interface, users can:

* ✍️ Convert any text (up to 20 characters) into block-style ASCII art
* 🎨 Apply live colors directly onto the art — solid, rainbow, gradient, or themed presets
* 👀 See an instant, fully colored preview as they type
* 📄 Download the finished art as a **DOCX** or **PDF** file with colors preserved
* 🧩 Pick from multiple character styles (`@`, `#`, `█`, `▓`, or a custom symbol)

All operations run **fully locally** in the browser via Streamlit — no accounts, no tracking, and no external services.

---

## ✨ Key Philosophy

ASCII Art Generator follows three core principles:

### 1️⃣ Simplicity First
Type your text, watch the art appear, hit download — no extra steps.

### 2️⃣ What You See Is What You Get
The same color logic drives the on-screen preview, the DOCX export, and the PDF export, so the downloaded file always matches the preview exactly.

### 3️⃣ Modular Architecture
Text engine, color logic, and file exporters are kept in separate modules for easy maintenance and future expansion.

---

## ✨ Features

* ✍️ Text-to-ASCII conversion using `pyfiglet`
* 🎨 Six color styles: Solid Color, Rainbow, Gradient (2 Colors), Fire, Ocean, Neon, Pastel
* 🖌️ Multiple character styles, plus a custom single-character option
* 👀 Live, fully colored preview — no separate "generate" step
* 📄 Export to **.docx** and **.pdf** (the only two formats that can actually store color)
* 📏 Auto-landscape PDF layout for wide art
* ❓ Built-in Instructions tab for first-time users
* ✅ Input validation and friendly warnings for unsupported characters

---

## ✍️ Text to ASCII

Convert any short word into large block-style ASCII art.

### Character Styles
* `@` Bold
* `#` Sharp
* `$` Money
* `|` Minimal
* `█` Solid Block
* `▓` Dark Shade
* `▒` Medium Shade
* `░` Light Shade
* `%` `&` `*` `+` `~` and more
* Custom single character

### Features
* Live preview as you type
* Automatic width detection with wide-art warnings
* Consistent letter shapes with clean spacing between characters

### Use Cases
> Banner text, social media graphics, terminal art, printable posters, greeting cards

---

## 🎨 Color Styles

Color is calculated per-character and applied directly onto the symbol itself — never shown as a separate swatch.

| Style | Description |
|---|---|
| Solid Color | One flat color you choose |
| Rainbow | Full-spectrum gradient, left to right |
| Gradient (2 Colors) | Smooth blend between two colors you pick |
| Fire | Ready-made warm red → orange → gold theme |
| Ocean | Ready-made deep blue → cyan theme |
| Neon | Ready-made pink → purple → blue → green theme |
| Pastel | Soft, low-saturation rainbow |

### Use Cases
> Themed banners, mood-based art, brand-colored text graphics

---

## 📄 Export Formats

| Format | Color Support | Notes |
|---|---|---|
| `.docx` | ✅ Yes | Opens in Microsoft Word / Google Docs |
| `.pdf` | ✅ Yes | Auto-switches to landscape for wide art |

> ℹ️ Plain `.txt` is intentionally **not offered** — text files have no way to store color, and color is the whole point of this app.

---

## 🖥️ User Interface

The app uses a tabbed, two-panel layout built with Streamlit.

### Screens
* Text to ASCII (Settings + Live Preview)
* Instructions
* About

### Features
* Wide, responsive layout
* Settings on the left, live preview on the right
* Beginner-friendly, no technical setup beyond installation

---

## 📁 Project Structure

```bash
ascii-art-generator/
│
├── assets/
│   ├── DejaVuSansMono.ttf
│   └── DejaVuSansMono-Bold.ttf
│
├── exporters/
│   ├── __init__.py
│   ├── docx_export.py
│   └── pdf_export.py
│
├── ascii_engine.py
├── color_utils.py
├── main.py
├── requirements.txt
├── LICENSE
└── README.md
```

> ✔ Text-generation logic, color logic, and file exporters are strictly separated for maintainability and extensibility.

---

## 🧪 Tech Stack

| Component | Implementation |
|---|---|
| Web Interface | Streamlit |
| Text-to-Art Rendering | pyfiglet |
| Word Document Export | python-docx |
| PDF Export | fpdf2 (embedded DejaVu Sans Mono font) |
| Language | Python 3.12.x |

---

## 🚀 Getting Started

### 1️⃣ Clone Repository
```bash
git clone https://github.com/ShakalBhau0001/ascii-art-generator.git
cd ascii-art-generator
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

**requirements.txt**
```txt
streamlit>=1.35
pyfiglet>=1.0
python-docx>=1.1
fpdf2>=2.7
```

### 3️⃣ Launch Application
```bash
streamlit run main.py
```

> **_The app will open automatically in your default browser._**

---

## ⚠️ Important Notes

* Text input is limited to 20 characters for clean, printable results
* Only `.docx` and `.pdf` downloads preserve color — `.txt` is not offered
* Wide art automatically switches the PDF to landscape orientation
* Unsupported characters may not render — stick to standard letters, numbers, and punctuation
* Internet connection is only required for the initial `pip install`

---

## 🛣️ Roadmap

* Multi-line / multi-word text support
* Additional character ramps and fonts
* Adjustable font size in exports
* Save/share preset color themes
* Standalone desktop packaging

---

## ⚠️ Disclaimer

> This project is intended for **personal, educational, and creative use only**.
> Generated art is created locally from user-provided text — no external content is used or stored.
> The developer is **not responsible** for misuse of this application.

---

## 📸 Preview

### 1. ASCII Tab
![ASCII Art Generator Preview](assets/ASCII-1.png)

### 2. Normal Preview
![ASCII Art Generator Preview](assets/ASCII-2.png)

### 3. DOCX Preview
![ASCII Art Generator Preview](assets/ASCII-3.png)

### 3. PDF Preview
![ASCII Art Generator Preview](assets/ASCII-4.png)

---

## 🪪 Author

> **Developer: Shakal Bhau**

> **GitHub: [ShakalBhau0001](https://github.com/ShakalBhau0001)**

---

> *"Great software hides complexity behind simplicity."*

---

## ⭐ Support

If you like this project, consider giving it a ⭐ on GitHub!

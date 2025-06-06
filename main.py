import os
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from indic_transliteration.sanscript import transliterate, DEVANAGARI, IAST

# Ensure output directory exists
os.makedirs("out", exist_ok=True)

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    extracted_text = []
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        text = page.get_text()
        # If not enough text, try OCR
        if len(text.strip()) < 20:
            pix = page.get_pixmap(dpi=300)
            img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
            text = pytesseract.image_to_string(img, lang="hin")
        extracted_text.append(text)
    return "\n".join(extracted_text)

def transliterate_text(text):
    return transliterate(text, DEVANAGARI, IAST)

if __name__ == "__main__":
    pdf_path = input("Enter path to PDF: ").strip()
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    extracted = extract_text_from_pdf(pdf_path)
    transliterated = transliterate_text(extracted)

    out_extracted = f"out/{base_name}_extracted.txt"
    out_transliterated = f"out/{base_name}_transliterated.txt"

    with open(out_extracted, "w", encoding="utf-8") as f:
        f.write(extracted)
    with open(out_transliterated, "w", encoding="utf-8") as f:
        f.write(transliterated)

    print(f"Extraction complete!\nExtracted: {out_extracted}\nTransliterated: {out_transliterated}") 
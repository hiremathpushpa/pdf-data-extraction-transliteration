import streamlit as st
import fitz  # PyMuPDF
import pytesseract
from PIL import Image
from indic_transliteration.sanscript import transliterate, DEVANAGARI, IAST
import os
import io

def extract_text_from_pdf(pdf_bytes):
    doc = fitz.open(stream=pdf_bytes, filetype="pdf")
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

st.title("PDF Data Extraction & Transliteration (Hindi to IAST)")

uploaded_file = st.file_uploader("Upload a Hindi PDF", type=["pdf"])

if uploaded_file is not None:
    st.write("File uploaded:", uploaded_file.name)
    if st.button("Extract Text and Transliterate"):
        pdf_bytes = uploaded_file.read()
        with st.spinner("Extracting text from PDF..."):
            extracted = extract_text_from_pdf(pdf_bytes)
        st.success("Text extraction complete!")
        st.text_area("Extracted Hindi Text", extracted, height=200)

        with st.spinner("Transliterating to IAST..."):
            transliterated = transliterate_text(extracted)
        st.success("Transliteration complete!")
        st.text_area("Transliterated (IAST) Text", transliterated, height=200)

        # Download buttons
        st.download_button(
            label="Download Extracted Hindi Text",
            data=extracted,
            file_name=f"{os.path.splitext(uploaded_file.name)[0]}_extracted.txt",
            mime="text/plain"
        )
        st.download_button(
            label="Download Transliterated (IAST) Text",
            data=transliterated,
            file_name=f"{os.path.splitext(uploaded_file.name)[0]}_transliterated.txt",
            mime="text/plain"
        ) 
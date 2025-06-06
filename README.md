# PDF Data Extraction & Transliteration

This app extracts text from Hindi PDFs (including scanned/image-based PDFs using Tesseract OCR) and transliterates the extracted text to IAST, all through a simple Streamlit web interface.

## Features
- Upload a Hindi PDF via the web UI
- Extracts text from both text-based and image-based (scanned) PDFs
- Uses Tesseract OCR for Hindi text extraction when needed
- Transliterates extracted Hindi text to IAST (Romanized script)
- View and download both extracted and transliterated text from the browser

## Requirements
- Python 3.8+
- Tesseract OCR installed and added to PATH (with Hindi language data)
- See `requirements.txt` for Python dependencies

## Usage
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Make sure Tesseract is installed and the Hindi language data (`hin.traineddata`) is available.
3. Start the Streamlit app:
   ```sh
   streamlit run app.py
   ```
4. In your browser, upload a Hindi PDF.
5. Click "Extract Text and Transliterate" to process the file.
6. View or download the extracted and transliterated text directly from the web interface.

## Notes
- For best OCR results, ensure your PDFs are high quality.
- You can adjust the script to support other languages by changing the Tesseract `lang` parameter and transliteration logic.
- The command-line script (`main.py`) is no longer needed; all functionality is available via the Streamlit UI. 
# PDF Data Extraction & Transliteration

This app extracts text from Hindi PDFs (including scanned/image-based PDFs using Tesseract OCR) and transliterates the extracted text to IAST.

## Features
- Extracts text from both text-based and image-based (scanned) PDFs
- Uses Tesseract OCR for Hindi text extraction when needed
- Transliterates extracted Hindi text to IAST (Romanized script)
- Saves both extracted and transliterated text to the `out/` folder

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
3. Run the script:
   ```sh
   python main.py
   ```
4. Enter the path to your PDF when prompted.
5. Extracted and transliterated text files will be saved in the `out/` folder.

## Notes
- For best OCR results, ensure your PDFs are high quality.
- You can adjust the script to support other languages by changing the Tesseract `lang` parameter and transliteration logic. 
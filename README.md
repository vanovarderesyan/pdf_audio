# pdf_audio
This program uses Google's Tesseract OCR and pyttsx3 (Text to Speech Library) to convert a pdf into a mp3 file. 

*Currently only works on windows.*



## Installation

1. **Python packages:**

   ```
   pip install -r requirements.txt
   ```

   

2. **Tesseract OCR**

   Download and install the program. Add the directory to PATH, for example:

   > C:\Program Files\poppler-0.68.0\bin

   [Tesseract OCR Downloads](https://tesseract-ocr.github.io/tessdoc/Downloads)

   

3. **Poppler**

   Download the binary files and place them in 'C:\Program Files'. Add the directory to PATH, for example:

   > C:\Program Files\Tesseract-OCR

   [Poppler for Windows](http://blog.alivate.com.au/poppler-windows/)



## Functions

- **pdf_to_text** - *Converts a pdf file (pdf_path) into a txt file.*
- **text_to_audio** - *Converts a txt file (txt_path) into a mp3 audio file.*
- **pdf_to_audio** - *Converts a pdf file (pdf_path) into a mp3 audio file.*



#### pdf_to_text

Converts a pdf file (pdf_path) into a txt file.

pdf_path -> Path to the pdf file to convert

```
python pdf_audio.py pdf_to_text PDF_PATH
```



#### text_to_audio

Converts a txt file (txt_path) into a mp3 audio file.

txt_path -> Path to the txt file to convert

```
python pdf_audio.py text_to_audio TXT_PATH
```



#### pdf_to_audio

Converts a pdf file (pdf_path) into a mp3 audio file.

pdf_path -> Path to the pdf file to convert

```
python pdf_audio.py pdf_to_audio PDF_PATH
```


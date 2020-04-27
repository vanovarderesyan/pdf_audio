import os
import io
import sys
import fire
import shutil
import ntpath
import pyttsx3
import pytesseract
from PIL import Image
from pathlib import Path
from builtins import str
from pdf2image import convert_from_path


def get_filename(path):
    head, tail = ntpath.split(path)
    return tail or ntpath.basename(head)


def get_file_path(path):
    return os.path.splitext(path)[0]


def pdf_to_text(pdf_path):
    """
    Converts a pdf file (pdf_path) into a txt file.
    pdf_path -> Path to the pdf file to convert
    """
    
    if not Path(pdf_path).is_file():
        print("File not found")
        exit() 
    
    output_filename = get_file_path(pdf_path) + ".txt"

    sub_dir = str("images/" + get_filename(pdf_path).replace('.pdf','') + "/")
    if not os.path.exists(sub_dir):
        os.makedirs(sub_dir)

    pages = convert_from_path(pdf_path, thread_count=6, output_folder=sub_dir)
    pg_cntr = 1
            
    for page in pages:
        filename = "pg_"+str(pg_cntr)+'_'+get_filename(pdf_path).replace('.pdf','.jpg')
        page.save(sub_dir+filename)
        page.close()
        del page
        with io.open(output_filename, 'a+') as f:
            f.write(str(pytesseract.image_to_string(sub_dir+filename)+"\n"))
        pg_cntr = pg_cntr + 1
        
    shutil.rmtree(sub_dir)


def text_to_audio(txt_path):
    """
    Converts a txt file (txt_path) into a mp3 audio file.
    txt_path -> Path to the txt file to convert
    """ 
    
    if not Path(txt_path).is_file():
        print("File not found")
        exit()
    
    audio_file_path = get_file_path(txt_path)
    output_path = audio_file_path  + ".mp3"

    engine = pyttsx3.init()

    with open(txt_path, "r") as f:
        engine.save_to_file(f.read(), output_path)
        engine.runAndWait()


def pdf_to_audio(pdf_path):
    """
    Converts a pdf file (pdf_path) into a mp3 audio file.
    pdf_path -> Path to the pdf file to convert
    """
    
    if not Path(pdf_path).is_file():
        print("File not found")
        exit()
    
    clean_path = get_file_path(pdf_path)
    pdf_to_text(clean_path + '.pdf')
    text_to_audio(clean_path + '.txt')
    os.remove(clean_path + '.txt')


if __name__ == "__main__":
    fire.Fire({
        'pdf_to_text': pdf_to_text,
        'text_to_audio': text_to_audio,
        'pdf_to_audio': pdf_to_audio
    })

import os
import shutil
from datetime import datetime

# Funktion, um Bild-Dateierweiterungen zu überprüfen
def is_image_file(filename):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

# Funktion, um Bilder nach Erstellungsdatum zu organisieren
def organize_image_files_by_creation_date(src_folder, dest_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if is_image_file(file):
                src_path = os.path.join(root, file)
                creation_time = os.path.getctime(src_path)
                creation_date = datetime.fromtimestamp(creation_time)
                year = str(creation_date.year)
                dest_subfolder = os.path.join(dest_folder, year)
                os.makedirs(dest_subfolder, exist_ok=True)
                dest_path = os.path.join(dest_subfolder, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {file} to {dest_subfolder}")

# Hauptfunktion
def start(source_folder, destination_folder):
    print("bin angekommen")
    source_folder =source_folder
    destination_folder = destination_folder

    organize_image_files_by_creation_date(source_folder, destination_folder)
    print("Bilddateien wurden nach Erstellungsdatum in neue Ordner verschoben.")

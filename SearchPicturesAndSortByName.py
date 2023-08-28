import os
import shutil

# Funktion, um Bild-Dateierweiterungen zu überprüfen
def is_image_file(filename):
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    return any(filename.lower().endswith(ext) for ext in image_extensions)

# Funktion, um Bilder in neuen Ordnern zu organisieren
def organize_image_files(src_folder, dest_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if is_image_file(file):
                src_path = os.path.join(root, file)
                dest_subfolder = os.path.join(dest_folder, file[0].upper())
                os.makedirs(dest_subfolder, exist_ok=True)
                dest_path = os.path.join(dest_subfolder, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {file} to {dest_subfolder}")

# Hauptfunktion
def main():
    source_folder = input("Bitte gib den Pfad zum Quellordner ein: ")
    destination_folder = input("Bitte gib den Pfad zum Zielordner ein: ")

    organize_image_files(source_folder, destination_folder)
    print("Bilddateien wurden alphabetisch in neue Ordner verschoben.")

if __name__ == "__main__":
    main()

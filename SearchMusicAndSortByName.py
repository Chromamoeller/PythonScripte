import os
import shutil


# Funktion, um Audio-Dateierweiterungen zu überprüfen
def is_audio_file(filename):
    audio_extensions = ['.mp3', '.wav', '.flac', '.aac', '.ogg']
    return any(filename.lower().endswith(ext) for ext in audio_extensions)


# Funktion, um Audio-Dateien in neuen Ordnern zu organisieren
def organize_audio_files(src_folder, dest_folder):
    for root, dirs, files in os.walk(src_folder):
        for file in files:
            if is_audio_file(file):
                src_path = os.path.join(root, file)
                first_letter = file[0].upper() if file[0].isalpha() else 'Other'
                dest_subfolder = os.path.join(dest_folder, first_letter)
                os.makedirs(dest_subfolder, exist_ok=True)
                dest_path = os.path.join(dest_subfolder, file)
                shutil.move(src_path, dest_path)
                print(f"Moved {file} to {dest_subfolder}")


# Hauptfunktion
def main():
    source_folder = input("Bitte gib den Pfad zum Quellordner ein: ")
    destination_folder = input("Bitte gib den Pfad zum Zielordner ein: ")

    organize_audio_files(source_folder, destination_folder)
    print("Audio-Dateien wurden alphabetisch in neue Ordner verschoben.")


if __name__ == "__main__":
    main()

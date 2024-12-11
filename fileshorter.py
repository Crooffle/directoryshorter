import os
import shutil

def organize_files(directory):
    # Cek apakah direktori ada pada sistem
    if not os.path.exists(directory):
        print(f'Direktori {directory} tidak ditemukan')
        return
    
    #Mapping semua file yang ada

    file_types = {
        "Gambar": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
        "Dokumen": [".pdf", ".doc", ".docx", ".txt", ".xls", ".xlsx", ".ppt", ".pptx"],
        "Video": [".mp4", ".mkv", ".avi", ".mov", ".wmv"],
        "Musik": [".mp3", ".wav", ".aac", ".flac"],
        "Arsip": [".zip", ".rar", ".7z", ".tar", ".gz"],
        "Program": [".exe", ".msi"],
        "Code": [".py", ".java", ".cpp", ".js", ".html", ".css", ".php"],
    }

    #Buat folder pada sistem
    for folder in file_types.keys:
        folder_path = os.path.join(directory, folder)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

    #Memindah file ke folder
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        #Skip direktori
        if os.path.isdir(file_path):
            continue

        #Memindah file
        file_moved = False
        for folder, extensions in file_types.items():
            if filename.lower().endswith(tuple(extensions)):
                shutil.move(file_path, os.path.join(directory, folder, filename))
                file_moved = True
                break
        
        #Jika file tidak ada/tidak diketahui oleh sistem
        if not file_moved:
            others_folder = os.path.join(directory, "Others")
            if not os.path.exists(others_folder):
                os.mkdir(others_folder)
            shutil.move(file_path, os.path.join(others_folder, filename))

    print(f'File Di {directory} sudah di rapikan!')

if __name__ == "__main__":
    target_directory = input("Masukka lokasi direktori yang ingin dirapikan: ").strip()
    organize_files(target_directory)
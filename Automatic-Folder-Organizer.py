import os
from tkinter.filedialog import askdirectory

path = askdirectory(title="Select a folder")

all_files = os.listdir(path)


type_files = {
    "images": [".png", ".jpg", ".gif", ".bmp", ".webp", ".tiff", ".raw", ".svg"],
    "texts": [".txt", ".pdf", ".doc", ".docx", ".odt", ".md", ".rtf", ".tex", ".wpd"],
    "musics": [".mp3", ".wav", ".aac", ".flac", ".m4a", ".wma", ".ogg"],
    "videos": [".mp4", ".mov", ".wmv", ".avi", ".avchd", ".mkv", ".webm"],
    "sheets":[ ".xls", ".xlsx", ".csv", ".ods"],
    "scripts":[".js",".py",".html", ".css", ".php",".java",".c", ".cpp", ".cs"],
    "executables":[".exe", ".msi"],
    "compacts":[".rar",".zip",".7z", ".tar", ".gz", ".bz2", ".xz"],
}


for file in all_files:
    name, extension = os.path.splitext(f"{path}/{file}")
    
    for folder in type_files:
        if extension in type_files[folder]:
            if not os.path.exists(f"{path}/{folder}"):
                os.mkdir(f"{path}/{folder}")

            os.rename(f"{path}/{file}", f"{path}/{folder}/{file}")
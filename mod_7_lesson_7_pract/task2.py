import os
import shutil

def sort_files(source_dir):
    if not os.path.exists(source_dir):
        raise FileNotFoundError("Source directory does not exist.")

    extension_map = {
        'images': ['.jpg', '.png', '.gif'],
        'documents': ['.txt', '.pdf', '.doc'],
        'videos': ['.mp4', '.mov', '.avi']
    }

    items = os.listdir(source_dir)

    for name in items:
        full_path = os.path.join(source_dir, name)
        if os.path.isdir(full_path):
            continue
        ext = os.path.splitext(name)[1].lower()
        category = 'other'
        if ext in extension_map['images']:
            category = 'images'
        elif ext in extension_map['documents']:
            category = 'documents'
        elif ext in extension_map['videos']:
            category = 'videos'

        target_dir = os.path.join(source_dir, category)
        if not os.path.exists(target_dir):
            os.mkdir(target_dir)
        shutil.move(full_path, os.path.join(target_dir, name))

source_directory = 'downloads'
try:
    sort_files(source_directory)
    print(f"Файлы в '{source_directory}' были отсортированы.")
except FileNotFoundError as e:
    print(e)

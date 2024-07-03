import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Specify your Downloads directory
DOWNLOADS_DIR = '/Users/sterzout/Downloads'

EXTENSIONS_MAP = {
    'pdf': 'pdf',
    'docx': 'word',
    'html': 'html',
    'txt': 'txt',
    'csv': 'csv',
    'jpg': 'images',
    'webp': 'webstuff',
    'jpeg': 'images',# Organize JPEG images into an 'images' folder
    'png': 'images',   # Organize PNG images into the same 'images' folder
    'zip': 'archives', # Organize ZIP files into an 'archives' folder
    # Add more extensions and folder names as needed
}


class DownloadHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        filepath = event.src_path
        filename = os.path.basename(filepath)
        _, extension = os.path.splitext(filename.lower())
        extension = extension.lstrip('.')  # Remove leading dot if present

        if extension in EXTENSIONS_MAP:
            destination_folder = EXTENSIONS_MAP[extension]
            destination_path = os.path.join(DOWNLOADS_DIR, destination_folder)
            if not os.path.exists(destination_path):
                os.makedirs(destination_path)
            shutil.move(filepath, os.path.join(destination_path, filename))
            print(f'Moved {filename} to {destination_folder} folder.')

def monitor_downloads():
    event_handler = DownloadHandler()
    observer = Observer()
    observer.schedule(event_handler, DOWNLOADS_DIR, recursive=False)
    observer.start()
    print(f"Monitoring {DOWNLOADS_DIR} for new downloads...")

    try:
        while True:
            time.sleep(10)  # Adjust the sleep interval as needed
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    monitor_downloads()

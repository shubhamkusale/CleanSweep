import os
import shutil
import json
import logging
from pathlib import Path

class FileOrganizer:
    def __init__(self, config_path="config.json"):
        self.config = self._load_config(config_path)
        self.logger = logging.getLogger("CleanSweep")

    def _load_config(self, path):
        try:
            with open(path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            self.logger.error(f"Config file not found at {path}")
            return {}

    def get_category(self, file_extension):
        for category, extensions in self.config.items():
            if file_extension.lower() in extensions:
                return category
        return "Others"

    def get_unique_filename(self, destination, filename):
        """
        Generates a unique filename if the file already exists in destination.
        Example: image.png -> image_1.png
        """
        base, ext = os.path.splitext(filename)
        counter = 1
        new_filename = filename
        while os.path.exists(os.path.join(destination, new_filename)):
            new_filename = f"{base}_{counter}{ext}"
            counter += 1
        return new_filename

    def organize_file(self, file_path):
        path = Path(file_path)
        if not path.exists() or path.is_dir():
            return

        # Ignore temporary files or hidden files
        if path.name.startswith('.') or path.name.endswith('.tmp') or path.name.endswith('.crdownload'):
            return

        category = self.get_category(path.suffix)
        destination_dir = path.parent / category
        
        try:
            destination_dir.mkdir(exist_ok=True)
            
            new_filename = self.get_unique_filename(destination_dir, path.name)
            destination_path = destination_dir / new_filename
            
            shutil.move(str(path), str(destination_path))
            self.logger.info(f"Moved: {path.name} -> {category}/{new_filename}")
            
        except Exception as e:
            self.logger.error(f"Error moving {path.name}: {e}")

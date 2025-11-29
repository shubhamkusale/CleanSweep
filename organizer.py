import os
import shutil
import json
import logging
import time
from pathlib import Path

class FileOrganizer:
    def __init__(self, config_path="config.json"):
        self.config = self._load_config(config_path)
        self.logger = logging.getLogger("CleanSweep")
        self.history_file = Path("undo_log.json")
        self.system_paths = {
            "Images": Path(os.path.expanduser("~/Pictures")),
            "Documents": Path(os.path.expanduser("~/Documents")),
            "Audio": Path(os.path.expanduser("~/Music")),
            "Video": Path(os.path.expanduser("~/Videos")),
            "Archives": Path(os.path.expanduser("~/Documents/Archives")),
            "Installers": Path(os.path.expanduser("~/Documents/Installers")),
            "Others": Path(os.path.expanduser("~/Documents/Others"))
        }
        # Ensure directories exist
        for path in self.system_paths.values():
            path.mkdir(parents=True, exist_ok=True)

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

    def log_move(self, src, dest):
        entry = {"src": str(src), "dest": str(dest), "time": time.time()}
        try:
            if self.history_file.exists():
                with open(self.history_file, 'r') as f:
                    history = json.load(f)
            else:
                history = []
            
            history.append(entry)
            
            with open(self.history_file, 'w') as f:
                json.dump(history, f, indent=4)
        except Exception as e:
            self.logger.error(f"Failed to log move: {e}")

    def undo_last_move(self):
        try:
            if not self.history_file.exists():
                print("No history found.")
                return

            with open(self.history_file, 'r') as f:
                history = json.load(f)

            if not history:
                print("Nothing to undo.")
                return

            last_move = history.pop()
            src = Path(last_move["src"])
            dest = Path(last_move["dest"])

            if dest.exists():
                shutil.move(str(dest), str(src))
                print(f"Undid: {dest.name} -> {src}")
                self.logger.info(f"Undid move: {dest} -> {src}")
            else:
                print(f"File not found at {dest}, cannot undo.")

            with open(self.history_file, 'w') as f:
                json.dump(history, f, indent=4)

        except Exception as e:
            print(f"Error during undo: {e}")

    def organize_file(self, file_path):
        path = Path(file_path)
        if not path.exists() or path.is_dir():
            return

        # Ignore temporary files
        if path.name.startswith('.') or path.name.endswith('.tmp') or path.name.endswith('.crdownload'):
            return

        category = self.get_category(path.suffix)
        target_folder = self.system_paths.get(category, self.system_paths["Others"])
        destination_path = target_folder / path.name

        try:
            # Handle Duplicates
            if destination_path.exists():
                copies_dir = path.parent / "Copies"
                copies_dir.mkdir(exist_ok=True)
                destination_path = copies_dir / path.name
                self.logger.info(f"Duplicate found. Moving to: {destination_path}")

            shutil.move(str(path), str(destination_path))
            self.logger.info(f"Moved: {path.name} -> {destination_path}")
            self.log_move(path, destination_path)
            
        except Exception as e:
            self.logger.error(f"Error moving {path.name}: {e}")

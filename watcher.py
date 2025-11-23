import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from organizer import FileOrganizer

class DirectoryWatcher(FileSystemEventHandler):
    def __init__(self, organizer):
        self.organizer = organizer
        self.logger = logging.getLogger("CleanSweep")

    def on_created(self, event):
        if not event.is_directory:
            # Small delay to ensure file write is complete
            time.sleep(1)
            self.organizer.organize_file(event.src_path)

    def on_modified(self, event):
        # We generally only care about creation, but some downloads might 
        # start as .tmp and then be renamed/modified.
        # For simplicity in this version, we'll focus on 'created' and 'moved'
        # but we can add logic here if needed.
        pass

    def on_moved(self, event):
        if not event.is_directory and not event.dest_path.endswith('.tmp'):
             self.organizer.organize_file(event.dest_path)

def start_watching(path_to_watch):
    organizer = FileOrganizer()
    event_handler = DirectoryWatcher(organizer)
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=False)
    observer.start()
    
    logging.info(f"CleanSweep started. Watching: {path_to_watch}")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

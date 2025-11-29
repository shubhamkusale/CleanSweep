import sys
import os
import logging
from watcher import start_watching

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S',
        handlers=[
            logging.FileHandler("cleansweep.log"),
            logging.StreamHandler()
        ]
    )

if __name__ == "__main__":
    setup_logging()
    
    if len(sys.argv) > 1 and sys.argv[1] == "--undo":
        from organizer import FileOrganizer
        organizer = FileOrganizer()
        organizer.undo_last_move()
        sys.exit(0)

    # Default to watching the current directory if no argument provided
    path_to_watch = sys.argv[1] if len(sys.argv) > 1 else "."
    
    # Convert to absolute path
    path_to_watch = os.path.abspath(path_to_watch)
    
    if not os.path.exists(path_to_watch):
        print(f"Error: The directory {path_to_watch} does not exist.")
        sys.exit(1)
        
    print(f"Starting CleanSweep on: {path_to_watch}")
    print("Press Ctrl+C to stop.")
    
    start_watching(path_to_watch)

# CleanSweep 🧹

**CleanSweep** is an intelligent, background file organizer for your desktop. It monitors your cluttered folders (like Downloads) and automatically sorts new files into organized categories in real-time.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

*   **Real-Time Monitoring**: Uses `watchdog` to detect file creation instantly.
*   **System Integration**: Sorts files directly into your system folders (`Documents`, `Pictures`, `Music`, etc.).
*   **Duplicate Safety**: Moves duplicate files to a `Copies` folder instead of overwriting or renaming.
*   **Undo Functionality**: Made a mistake? Run with `--undo` to reverse the last action.
*   **Configurable**: Customize your own sorting rules via `config.json`.
*   **Lightweight**: Runs silently in the background with minimal resource usage.

## 💡 Why I Built This

I noticed that my `Downloads` folder was constantly becoming a graveyard of unorganized files. I wanted a solution that was:
1.  **Automatic**: No manual drag-and-drop.
2.  **Smart**: Puts files where they *actually* belong (System Folders).
3.  **Safe**: Never deletes or overwrites anything.

CleanSweep solves this by acting as a silent housekeeper for your PC.

## 🚀 Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/shubhamkusale/CleanSweep.git
    cd CleanSweep
    ```

2.  Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## 💻 Usage

### 1. Start Cleaning
Run the bot by specifying the folder you want to keep clean:

```bash
python main.py "C:\Users\YourName\Downloads"
```

### 2. Undo a Mistake
If a file was moved by mistake, you can undo the last action:

```bash
python main.py --undo
```

## ⚙️ Configuration

You can modify `config.json` to add new file types or categories:

```json
{
    "Images": [".jpg", ".png", ".gif"],
    "Code": [".py", ".js", ".html"],
    "MyWork": [".docx", ".pptx"]
}
```

## 🛠️ Built With

*   [Python](https://www.python.org/)
*   [Watchdog](https://python-watchdog.readthedocs.io/)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1.  Fork the project
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`)
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4.  Push to the branch (`git push origin feature/AmazingFeature`)
5.  Open a Pull Request

## 🗺️ Roadmap

*   [ ] Add support for custom file patterns via UI
*   [ ] Implement a system tray icon for easy control
*   [x] Add "Undo" functionality for last moved files
*   [x] Smart duplicate handling (Copies folder)
*   [ ] Cross-platform support (macOS/Linux) improvements

## 📄 License

This project is licensed under the MIT License.

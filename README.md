# CleanSweep 🧹

**CleanSweep** is an intelligent, background file organizer for your desktop. It monitors your cluttered folders (like Downloads) and automatically sorts new files into organized categories in real-time.

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-MIT-green)

## ✨ Features

*   **Real-Time Monitoring**: Uses `watchdog` to detect file creation instantly.
*   **Smart Sorting**: Automatically moves files into `Images`, `Documents`, `Audio`, `Video`, `Archives`, and `Installers`.
*   **Safety First**: Never overwrites files. If a duplicate exists, it renames the new file (e.g., `image_1.png`).
*   **Configurable**: Customize your own sorting rules via `config.json`.
*   **Lightweight**: Runs silently in the background with minimal resource usage.

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

Run the bot by specifying the folder you want to keep clean:

```bash
python main.py "C:\Users\YourName\Downloads"
```

To stop the bot, press `Ctrl+C`.

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

## 📄 License

This project is licensed under the MIT License.

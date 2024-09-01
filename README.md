# yt-dlp-gui
Graphical interface for the command line tool [yt-dlp](https://github.com/yt-dlp/yt-dlp), which allows users to download 
videos from various [websites](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md), including YouTube. 
It is designed to be more user-friendly and accessible for those who are not comfortable using the command line.

## Screenshot
![Capture](https://github.com/user-attachments/assets/6265eb04-8552-4330-8cdb-307264a95bc6)

## Getting Started

There are three ways to get started, depending on your preference and system:

* [`Portable`](#portable) ~ *Windows*
* [`Build`](#build) ~ *Windows & Linux*
* [`Manual`](#manual) ~ *Platform independent*

### Portable

Download the latest portable version from the [releases](https://github.com/dsymbol/yt-dlp-gui/releases/latest) section. 
This will download a ZIP file containing the program files and all necessary dependencies.

*All releases are built and released using GitHub Workflow*

### Build

You **must** have [Python](https://www.python.org/downloads/) 3.9+ installed.

To build yt-dlp-gui from its source code:

1. Clone the repository onto your local machine:

```bash
git clone https://github.com/dsymbol/yt-dlp-gui
cd yt-dlp-gui
```

2. Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

3. Use PyInstaller to compile the program:

```bash
cd app
```

#### Linux

```bash
pyinstaller --name=yt-dlp-gui --clean -y app.py
```

#### Windows

```pwsh
pyinstaller --name=yt-dlp-gui --clean -y app.py --icon ./ui/assets/yt-dlp-gui.ico --noconsole
```

4. The executable will be ready at:

```bash
./dist/yt-dlp-gui
```

### Manual

You **must** have [Python](https://www.python.org/downloads/) 3.9+ installed.

1. Clone the repository onto your local machine:

```bash
git clone https://github.com/dsymbol/yt-dlp-gui
cd yt-dlp-gui
```

2. Install the necessary dependencies:

```bash
pip install -r requirements.txt
```

3. Run the program:

```bash
cd app
python app.py
```

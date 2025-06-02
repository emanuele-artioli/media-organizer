# media-organizer

Automatically compress and organize your large media collections—photos, videos, and audio—without losing metadata or noticeable quality.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [How It Works](#how-it-works)
- [Requirements](#requirements)
- [Step 1: Install Miniconda](#step-1-install-miniconda)
- [Step 2: Set Up the Python Environment](#step-2-set-up-the-python-environment)
- [Step 3: Download the Script](#step-3-download-the-script)
- [Step 4: Run the Script](#step-4-run-the-script)
- [Advanced Usage](#advanced-usage)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

**media-organizer** is a Python tool that scans a folder (and all its subfolders) for large media files—images, videos, and audio—and compresses them automatically. It only overwrites files if the compressed version is smaller and preserves all metadata (like EXIF for photos and timestamps for all files). This helps you reclaim disk space without sacrificing quality or losing important information.

---

## Features

- **Automatic compression** of images, videos, and audio files.
- **Preserves metadata** (EXIF, timestamps, etc.).
- **No quality loss**: Uses smart compression settings to keep files looking and sounding great.
- **Skips files** if compression would not save space.
- **Processes entire folders recursively**, sorting by file size (largest first).
- **Cross-platform**: Works on Windows, macOS, and Linux.

---

## How It Works

1. You specify a folder containing your media files.
2. The script finds all supported files above a certain size (default: 5 MB).
3. Each file is compressed using the best available method for its type:
   - **Images**: JPEG/WebP compression via Pillow.
   - **Videos & Audio**: ffmpeg with smart settings.
4. If the compressed file is smaller, it replaces the original (keeping metadata).
5. If not, the original is kept.

---

## Requirements

- Windows, macOS, or Linux
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (recommended for beginners)
- Python 3.7 or higher

---

## Step 1: Install Miniconda

Miniconda is a free tool that makes Python setup easy.

1. Go to the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html).
2. Download the installer for your operating system.
3. Run the installer:
   - **Windows**: Double-click the `.exe` file.
   - **macOS/Linux**: Open Terminal, navigate to the download location, and run `bash Miniconda3-latest-...sh`.
4. After installation, close and reopen your terminal.

---

## Step 2: Set Up the Python Environment

1. **Open your terminal** (or Anaconda Prompt on Windows).
2. **Navigate to the project folder** (where `environment.yml` is located):

   ```
   cd /Users/manu/Desktop/media-organizer
   ```

3. **Create the environment from the YAML file**:

   ```
   conda env create -f environment.yml
   ```

4. **Activate the environment**:

   ```
   conda activate media_organizer
   ```

That's it! All required packages (including ffmpeg, Pillow, and others) will be installed automatically.

---

## Step 3: Download the Script

1. Download or clone this repository.
2. Locate `media_organizer.py`.

---

## Step 4: Run the Script

1. Make sure your environment is activated:

   ```
   conda activate media-env
   ```

2. Run the script, specifying the folder you want to compress:

   ```
   python media_organizer.py
   ```

   By default, it will process `/Users/manu/Desktop/2020` (edit the last line in the script to change this).

---

## Advanced Usage

You can customize:
- **Target folder**: Change the path in the `main()` call at the bottom of `media_organizer.py`.
- **Compression ratio**: Lower values save more space (default is 70, meaning compressed files will be ≤70% of the original size).
- **Minimum file size**: Only files larger than this (in MB) will be processed.

Example:
```python
main("/path/to/your/folder", compression_ratio=60, min_size_mb=2)
```

---

## Troubleshooting

- **ffmpeg not found**: Make sure ffmpeg is installed and available in your system PATH.
- **Permission errors**: Run your terminal as administrator (Windows) or use `sudo` (macOS/Linux) if needed.
- **No files processed**: Check your folder path and minimum file size setting.

---

## License

MIT License. See [LICENSE](LICENSE) for details.

---

*For questions or help, open an issue or contact the maintainer.*


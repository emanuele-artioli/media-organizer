# media-organizer

A simple Python script to help you copy media files from an external hard drive to your Desktop, and create zipped archives of folders for easy backup.

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Requirements](#requirements)
- [Step 1: Install Miniconda](#step-1-install-miniconda)
- [Step 2: Set Up the Python Environment](#step-2-set-up-the-python-environment)
- [Step 3: Download the Script](#step-3-download-the-script)
- [Step 4: Configure the Script](#step-4-configure-the-script)
- [Step 5: Run the Script](#step-5-run-the-script)
- [How the Script Works](#how-the-script-works)
- [Troubleshooting](#troubleshooting)
- [License](#license)

---

## Overview

This project provides a script to automate copying files from an external hard drive to your Desktop, and to create zipped archives of folders for backup or sharing.

---

## Features

- **Copy all files** from a specified folder (e.g., an external hard drive) to your Desktop.
- **Skips files** that already exist and are identical.
- **Overwrites files** if the source and destination differ in size.
- **Creates zipped archives** of any folder, saving the archive to your Desktop.

---

## Requirements

- Windows, macOS, or Linux
- [Miniconda](https://docs.conda.io/en/latest/miniconda.html) (recommended for beginners)
- Python 3.7 or higher

---

## Step 1: Install Miniconda

Miniconda is a free minimal installer for the [conda](https://docs.conda.io/en/latest/) package manager. It makes managing Python environments easy.

1. Go to the [Miniconda download page](https://docs.conda.io/en/latest/miniconda.html).
2. Download the installer for your operating system (Windows, macOS, or Linux).
3. Run the installer and follow the instructions.  
   - On Windows: Double-click the `.exe` file.
   - On macOS/Linux: Open Terminal, navigate to the download location, and run `bash Miniconda3-latest-...sh`.
4. After installation, close and reopen your terminal (or Anaconda Prompt on Windows).

---

## Step 2: Set Up the Python Environment

1. Open your terminal (or Anaconda Prompt on Windows).
2. Create a new environment named `media-env` with Python 3.9:
   ```bash
   conda create -n media-env python=3.9
   ```
3. Activate the environment:
   - On Windows:
     ```bash
     conda activate media-env
     ```
   - On macOS/Linux:
     ```bash
     source activate media-env
     ```

---

## Step 3: Download the Script

Download the `copy_media.py` script from the [GitHub repository](https://github.com/yourusername/media-organizer).

---

## Step 4: Configure the Script

1. Open the `copy_media.py` script in a text editor.
2. Set the `SOURCE_FOLDER` variable to the path of your external hard drive.
3. Set the `DESTINATION_FOLDER` variable to your Desktop path.
4. Save and close the file.

---

## Step 5: Run the Script

1. Open your terminal (or Anaconda Prompt on Windows).
2. Navigate to the folder where you downloaded `copy_media.py`.
3. Run the script:
   ```bash
   python copy_media.py
   ```

---

## How the Script Works

The script uses the `shutil` and `os` modules to copy files and create archives. It compares file sizes to determine if a file should be overwritten. Zipped archives are created using the `zipfile` module.

---

## Troubleshooting

- **Script fails to run**: Ensure Python is correctly installed and the environment is activated.
- **Permission errors**: Run the terminal or Anaconda Prompt as an administrator (Windows) or use `sudo` (macOS/Linux).
- **Files not copying**: Check the `SOURCE_FOLDER` and `DESTINATION_FOLDER` paths in the script.

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.


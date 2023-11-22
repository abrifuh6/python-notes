# Python Installation

## For Windows

## Prerequisites

Make sure you have the following installed on your machine:

- [Python](https://www.python.org/downloads/)

## Installation

1. **Download Python:**
   Visit the [official Python website](https://www.python.org/downloads/) and download the latest version.

2. **Run the Installer:**
   Double-click on the downloaded installer and follow the on-screen instructions. Be sure to check the box that says "Add Python to PATH."

3. **Verify Installation:**
   Open a command prompt and run the following commands to verify that Python and pip (Python package installer) are installed:

   ```bash
   python --version
   pip --version

## For MAC

## Prerequisites

Make sure you have the following installed on your machine:

- [Terminal](https://support.apple.com/guide/terminal/welcome/mac)

## Installation

1. **Open Terminal:**
   - You can find Terminal in the Applications > Utilities folder, or use Spotlight (`Cmd + Space`, then type "Terminal").

2. **Check Existing Python Version (Optional):**
   - Check if Python is already installed by running:

     ```bash
     python --version
     ```

     If a version number is displayed, Python is installed.

3. **Install Python:**
   - If Python is not installed or you want to install the latest version, you can use the following command:

     ```bash
     xcode-select --install
     /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
     brew install python
     ```

     The first command installs the Xcode Command Line Tools, and the subsequent commands install Homebrew and then Python using Homebrew.

4. **Verify Installation:**
   - After the installation is complete, run the following commands to verify that Python is installed:

     ```bash
     python3 --version
     pip3 --version
     ```

# OpenSpecimen Testing

This application performs either destructive or non-destructive tests on an instance of OpenSpecimen and records the output.  By comparing the outputs created before and after an upgrade, it is possible to check that nothing major has changed.

## Installation
1. Download the repository
2. Create a virtual environment and install the contents of the `requirements.txt`
3. Copy `example.env` to `.env` and amend the values to match your system

## Prerequisites
1. Install Firefox using the command: `sudo apt install firefox`
2. Find the latest version of the geckodriver by visiting [Geckodriver Release page](https://github.com/mozilla/geckodriver/releases)
```bash
# Download latest version
wget https://github.com/mozilla/geckodriver/releases/download/v{version number}/geckodriver-v{version number}-linux64.tar.gz

# Extract the file with
tar -xvzf geckodriver*

# Make it executable:
chmod +x geckodriver

# Move file to runable path
sudo mv geckodriver /usr/local/bin/
```

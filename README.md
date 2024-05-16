# OpenSpecimen Testing

This application performs either destructive or non-destructive tests on an instance of OpenSpecimen and records the output.  By comparing the outputs created before and after an upgrade, it is possible to check that nothing major has changed.

## Installation
1. Download the repository
2. Create a virtual environment and install the contents of the `requirements.txt` (see python virtual environments and `pip` for further information)
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
## Running
### Set Up Parameters
To record the output of the correctly, suitable parameters have to be set in the `.env` file.  A description of the parameters and how they affect the output is contained within the `example.env` file.

### Running the tests
You can run either destructive or non-destructive tests using:
```bash
python run_non_destructive_tests.py
```
or
```bash
python run_destructive_tests.py
```
After completing the run for the base version, upgrade OpenSpecimen, update the parameters in the `.env` file and run the same test again.
Then compare the test results using `diff` or other comparison tool.

## Amendmenst for versions
With updates to OpenSpecimen the HTML produced and the data output changes.  This application provides two mechanisms to help cope with these problems, but
unfortunately it requires changes to the code itself.  See `non_desructive_tests/order_tester.py` for examples of the use of `VersionTranslator` and `get_version_item`.

These functions use the `OS_VERSION` and `OS_COMPARE_VERSION` to select different selectors from a dictionary or translate values based on their version.

When developing tests for new versions of this tool for future versions of OpenSpecimen these will have to be used to deal with the changes.
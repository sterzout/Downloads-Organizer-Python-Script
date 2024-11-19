Features
Automated file organization: Moves files to designated folders based on their file extensions.
Customizable folder mapping: Easily modify the EXTENSIONS_MAP dictionary to add or change file types and target folders.
Real-time monitoring: Uses Watchdog to detect and handle file creation events as they happen.
Setup
Prerequisites
Python 3.7 or higher
Required Python package:
watchdog
Install Dependencies
Run the following command to install the required package:
  pip install watchdog
How to Use
Edit the Script: Update the DOWNLOADS_DIR variable in the script to the path of your Downloads folder. 
  For example: DOWNLOADS_DIR = '/Users/your_username/Downloads'
Customize Folder Mappings: Adjust the EXTENSIONS_MAP dictionary to define which file types should be moved to which folders. 
  Example:
  EXTENSIONS_MAP = {
    'pdf': 'pdf',
    'docx': 'word',
    'jpg': 'images',
    'png': 'images',
}
Run the Script: Execute the script using:
  python organizer.py
Monitor Your Downloads: The script will monitor the Downloads directory and move files to the appropriate subfolders as defined in EXTENSIONS_MAP.

Downloads Organizer - README
Overview
The Downloads Organizer is a Python script that automatically organizes files in your Downloads directory into specific subfolders based on their file extensions. By using the Watchdog library, the script monitors the directory for new files and moves them into categorized subfolders.

Features
Automated file organization: Moves files to designated folders based on their file extensions.
Customizable folder mapping: Easily modify the EXTENSIONS_MAP dictionary to add or change file types and target folders.
Real-time monitoring: Uses Watchdog to detect and handle file creation events as they happen.
Setup
Prerequisites
Python 3.7 or higher
Required Python package:
watchdog
Install Dependencies
Run the following command to install the required package:

bash
Copy code
pip install watchdog
How to Use
Edit the Script: Update the DOWNLOADS_DIR variable in the script to the path of your Downloads folder. For example:

python
Copy code
DOWNLOADS_DIR = '/Users/your_username/Downloads'
Customize Folder Mappings: Adjust the EXTENSIONS_MAP dictionary to define which file types should be moved to which folders. Example:

python
Copy code
EXTENSIONS_MAP = {
    'pdf': 'pdf',
    'docx': 'word',
    'jpg': 'images',
    'png': 'images',
}
Run the Script: Execute the script using:

bash
Copy code
python organizer.py
Monitor Your Downloads: The script will monitor the Downloads directory and move files to the appropriate subfolders as defined in EXTENSIONS_MAP.

Folder Structure Example
Given the following EXTENSIONS_MAP:

python
Copy code
EXTENSIONS_MAP = {
    'pdf': 'pdf',
    'jpg': 'images',
    'png': 'images',
    'zip': 'archives',
}
A new example.pdf will be moved to /Downloads/pdf/.
A new picture.jpg will be moved to /Downloads/images/.
A new archive.zip will be moved to /Downloads/archives/.
Stopping the Script
To stop the script, press Ctrl+C in the terminal.

Notes
The script only moves newly created files. Existing files in the Downloads folder are not affected.
Ensure you have write permissions for the Downloads folder and its subfolders.
Folders are automatically created if they do not exist.
Customization
Adding New Extensions: To add a new extension, update the EXTENSIONS_MAP with the extension as the key and the target folder name as the value: EXTENSIONS_MAP['mp4'] = 'videos'
Adjusting Monitoring Frequency: Modify the sleep interval in the while loop: time.sleep(10)  # Check every 10 seconds
License
This script is provided as-is under the MIT License. Modify and use it at your own discretion.

Acknowledgements
Built using the Watchdog Python library.

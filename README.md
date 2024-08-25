# YouTube-Downloader-Modern-GUI

## Overview
This application provides a graphical user interface (GUI) for downloading YouTube videos. Built using Python's tkinter library and customtkinter, it allows users to enter a YouTube video URL, select a file format, choose a download directory, and download the video.

##Features
Insert YouTube URL: Enter the URL of the video you wish to download.
Select File Format: Choose from available file formats (.mp4, .mkv, .mov).
Choose Download Directory: Select the folder where the video will be saved.
Download Video: Download the video in the selected format.
Quit Application: Close the application when done.


##Prerequisites
Make sure you have Python installed on your system. You will also need to install the required Python libraries. Use the following commands to install the necessary packages:

```bash
pip install tkinter
pip install customtkinter
pip install pytubefix
```

## Usage
Run the Application:

```bash
Copy code
python your_script_name.py
```
Insert a YouTube URL: Type or paste the YouTube video URL into the input field.

Select File Format: Choose the desired file format from the dropdown menu.

Choose Download Directory:

Click on the "Select Folder" button to choose the directory where the video will be saved.
Download Video:

Click the "Download" button to start the download.
Quit Application:

Click the "Quit! :(" button to close the application.
Code Explanation
downloader(): Handles the download process. It retrieves the URL and selected file extension, downloads the video using pytubefix, and saves it to the chosen directory.

##### open_folder(): Opens a dialog to select the download directory and enables the download button.

##### exit_app(): Closes the application.

##### on_select(value): Updates the label to show the selected file format.

## Global Variables
directory: Stores the path to the directory where the video will be saved.
<br>
url: Holds the YouTube video URL input by the user.
<br>
selected_value: Stores the selected file format.

## Libraries Used
tkinter: Standard Python library for GUI applications.
customtkinter: A custom tkinter library for modern-looking interfaces.
pytubefix: A library for downloading YouTube videos.

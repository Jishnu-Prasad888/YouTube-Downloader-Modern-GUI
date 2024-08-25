import tkinter as tk
import tkinter
import tkinter.messagebox
import customtkinter
from pytubefix import YouTube
from pytubefix.cli import on_progress
from tkinter import messagebox
from tkinter import filedialog


global directory


# System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def downloader() :
    url = link.get()
    url = url.strip()
    print(url)
    extension = selected_value.get()
    try :
        yt = YouTube(url)
        video_stream = yt.streams.get_highest_resolution()
        video_stream.download(output_path=directory,filename=yt.title+extension)

    except Exception as e :
        messagebox.showerror("Error",e)    


def open_folder():
    global directory
    directory = filedialog.askdirectory()
    downloadButton.configure(state="normal")

def exit_app() :
    app.destroy()

def on_select(value) :
    selected_label.configure(text=f"Selected:{value}")


file_extensions = [".mp4",".mkv",".mov"]

# Our app frame
app = customtkinter.CTk()

global url

app.geometry("720x480")
app.title("YouTube GUI Downloader")

title = customtkinter.CTkLabel(app, text="Insert a YouTube Link")
title.pack(padx=10, pady=10)


url = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=300, height=30,textvariable=url,placeholder_text="URL" )
link.pack(padx=15, pady=20)

selected_value = tk.StringVar(value=file_extensions[0])
dropdown =  customtkinter.CTkOptionMenu(app, values=file_extensions, variable=selected_value, command=on_select)
dropdown.pack()

selected_label = customtkinter.CTkLabel(app, text=f"Selected: {selected_value.get()}")
selected_label.pack(pady=10)
selected_label.pack()

select_folder = customtkinter.CTkButton(app,text="Select Folder",command=open_folder)
select_folder.pack()

downloadButton = customtkinter.CTkButton(app, text="Download", command=downloader,state="disabled")
downloadButton.pack(padx=20, pady=20)

quit_button = customtkinter.CTkButton(app,text="Quit! :(", command=exit_app)
quit_button.pack()

app.mainloop()
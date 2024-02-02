import tkinter
from tkinter import filedialog
import customtkinter
from pytube import YouTube
import threading

# Function to handle download in a separate thread
def download_thread():
    threading.Thread(target=download).start()

# Main download function
def download():
    try:
        ytlink = Enter.get()
        yt_object = YouTube(ytlink, on_progress_callback=update_progress)
        vid = yt_object.streams.get_highest_resolution()
        title.configure(text=yt_object.title, text_color="white")
        finish_Label.configure(text="Download in progress...", text_color="blue")
        
        # Download the video with progress tracking
        vid.download(filename_prefix='temp', output_path=download_location)
        
        finish_Label.configure(text="Download Completed!", text_color="green")
    except Exception as e:
        finish_Label.configure(text="Error while Downloading: " + str(e), text_color="red")

# Function to update progress bar
def update_progress(stream, chunk, bytes_remaining):
    progress = (1 - bytes_remaining / stream.filesize) * 100
    pProgress.configure(text=f"{progress:.2f}%")
    Progress_bar.set(progress)

# Function to select download location
def select_location():
    global download_location
    download_location = filedialog.askdirectory()

# Settings
customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

# App frame 
app = customtkinter.CTk()
app.geometry("703x270")  # Adjusted window width and height

# Label for telling someone to insert a link
title = customtkinter.CTkLabel(app, text="Insert a Youtube Link", font=("Helvetica", 14))  # Adjusted font size
title.pack(padx=10, pady=(20, 5))  # Adjusted vertical padding

# Entry for the user to enter the link 
url_var = tkinter.StringVar()
Enter = customtkinter.CTkEntry(app, width=450, height=30, justify="center", textvariable=url_var)  # Adjusted width and height
Enter.pack(padx=10, pady=5)  # Adjusted vertical padding

# Download Button
Download_Button = customtkinter.CTkButton(app, text="Download", font=("Helvetica", 12), command=download_thread)  # Adjusted font size
Download_Button.pack(pady=5, padx=10)  # Adjusted vertical padding and horizontal padding

# Finish Label 
finish_Label = customtkinter.CTkLabel(app, text="", font=("Helvetica", 10))  # Adjusted font size
finish_Label.pack(padx=10, pady=5)  # Adjusted vertical padding

# Progress Label 
pProgress = customtkinter.CTkLabel(app, text="0%", font=("Helvetica", 10))  # Adjusted font size
pProgress.pack(padx=10, pady=(5, 0))  # Adjusted vertical padding

# Progress Bar
Progress_bar = customtkinter.CTkProgressBar(app, width=450)  # Adjusted width
Progress_bar.set(0)
Progress_bar.pack(padx=10, pady=(0, 5))  # Adjusted vertical padding

# Button to select download location
select_location_button = customtkinter.CTkButton(app, text="Select Download Location", font=("Helvetica", 10), command=select_location)  # Adjusted font size
select_location_button.pack(pady=5, padx=10)  # Adjusted vertical padding and horizontal padding

# Default download location
download_location = "./"

# Run the app 
app.mainloop()

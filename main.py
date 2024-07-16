import tkinter as tk
from tkinter import messagebox, filedialog
import os
from utils import download_video

def download_and_convert():
    url = url_entry.get()
    if not url:
        messagebox.showerror("Error", "Please enter a YouTube URL")
        return
    
    output_path = filedialog.asksaveasfilename(defaultextension=".mp3", filetypes=[("MP3 files", "*.mp3")])
    if not output_path:
        return

    try:
        temp_video_path = "temp_video"
        download_video(url, temp_video_path)
        os.rename(temp_video_path + ".mp3", output_path)
        messagebox.showinfo("Success", f"MP3 saved to {output_path}")
    except Exception as e:
        messagebox.showerror("Error", str(e))
    finally:
        if os.path.exists(temp_video_path + ".mp3"):
            os.remove(temp_video_path + ".mp3")

app = tk.Tk()
app.title("YouTube to MP3 Converter")

frame = tk.Frame(app)
frame.pack(pady=20)

url_label = tk.Label(frame, text="YouTube URL:")
url_label.grid(row=0, column=0, padx=5, pady=5)

url_entry = tk.Entry(frame, width=50)
url_entry.grid(row=0, column=1, padx=5, pady=5)

download_button = tk.Button(frame, text="Download and Convert", command=download_and_convert)
download_button.grid(row=1, columnspan=2, pady=10)

app.mainloop()

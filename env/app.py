import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube
import os

def donload_video():
    url = entry_url.get()
    resolution = resolution_var.get()

    progress_label.pack(pady=(10, 5))
    progress_bar.pack(pady=(10, 5))
    status_label.pack(pady=(10, 5))

    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        stream = yt.streams.filter(res=resolution).first()

        #pobieranie wideo do okreslonego folderu
        os.path.join("downloads", f"{yt.title}.mp4")
        stream.download(output_path="downloads")

        status_label.configure(text="Plik zostal pobrany prawidłowo", text_color="white", fg_color="green")
    except Exception as e:
        status_label.configure(text=f"Error {str(e)}", text_color="white", fg_color="red")

def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    procentage_completed = bytes_downloaded / total_size * 100
    
    progress_label.configure(text = str(int(procentage_completed)) + "%")
    progress_label.update()
    
    progress_bar.set(float(procentage_completed / 100))

#utworzenie okienka nadanie mu kolorow
root = ctk.CTk()
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

#ustawienie tytulu okienka
root.title("YT Downloader")

#ustawienie min i max szerokosci okna
root.geometry("720x480")
root.minsize(780, 480)
root.maxsize(1080, 720)

# stworzenie obszaru dla zawartosci
content_frame = ctk.CTkFrame(root)
content_frame.pack(fill=ctk.BOTH, expand = True, padx=10, pady=10)

# stworzenie pola na wprowadzenie url filmu
url_label = ctk.CTkLabel(content_frame, text="Wprowadz YouTube URL: ")
entry_url = ctk.CTkEntry(content_frame, width=400, height=40)
url_label.pack(pady=(10, 5)) 
entry_url.pack(pady=(10, 5)) 

# utworzenie przycisku pobierania
donload_button = ctk.CTkButton(content_frame, text="Pobierz", command=donload_video)
donload_button.pack(pady=(10, 5)) 

# przycisk do wyboru jakosci wideo
resolution = ["720p", "360p", "240p"]
resolution_var = ctk.StringVar()
resolution_combobox = ttk.Combobox(content_frame, values=resolution, textvariable=resolution_var)
resolution_combobox.pack(pady=(10, 5)) 
resolution_combobox.set("720p")

# stworzenie pola ktore pokazuje postepy pobierania
progress_label = ctk.CTkLabel(content_frame, text="0%")

progress_bar = ctk.CTkProgressBar(content_frame, width=400)
progress_bar.set(0)

# stworzenie pola statusu
status_label = ctk.CTkLabel(content_frame, text="") 

#aby wystartowac aplikacje 
root.mainloop()
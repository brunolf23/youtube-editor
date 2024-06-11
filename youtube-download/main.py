import os
from tkinter import Tk, Label, Entry, Button, filedialog, messagebox
from pytube import YouTube

def download_video():
    url = url_entry.get()
    folder = folder_entry.get()
    
    if not url:
        messagebox.showerror("Erro", "Por favor, insira a URL do vídeo do YouTube.")
        return
    
    if not folder:
        messagebox.showerror("Erro", "Por favor, escolha o diretório para salvar o vídeo.")
        return
    
    try:
        yt = YouTube(url)
        video_stream = yt.streams.filter(res="1080p", file_extension="mp4", progressive=False).first()
        
        if not video_stream:
            messagebox.showerror("Erro", "Vídeo em 1080p não disponível.")
            return
        
        video_path = video_stream.download(output_path=folder, filename=yt.title + "_1080p.mp4")
        
        messagebox.showinfo("Sucesso", "Download completo!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro desconhecido: {e}")

def browse_folder():
    folder_selected = filedialog.askdirectory()
    folder_entry.delete(0, 'end')
    folder_entry.insert(0, folder_selected)

# Configuração da interface gráfica
root = Tk()
root.title("Downloader de Vídeos do YouTube 1080p")

Label(root, text="URL do vídeo do YouTube:").grid(row=0, column=0, padx=10, pady=10)
url_entry = Entry(root, width=50)
url_entry.grid(row=0, column=1, padx=10, pady=10)

Label(root, text="Diretório para salvar o vídeo:").grid(row=1, column=0, padx=10, pady=10)
folder_entry = Entry(root, width=50)
folder_entry.grid(row=1, column=1, padx=10, pady=10)

browse_button = Button(root, text="Procurar", command=browse_folder)
browse_button.grid(row=1, column=2, padx=10, pady=10)

download_button = Button(root, text="Baixar", command=download_video)
download_button.grid(row=2, column=1, padx=10, pady=20)

root.mainloop()
import sys
import os
import threading
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import subprocess

def resource_path(relative_path):
    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    return os.path.join(base_path, relative_path)

class WavToMp3Converter:
    def __init__(self, root):
        self.root = root
        self.root.title("咖喱牌Wav转Mp3")
        self.root.geometry("400x200")
        self.root.iconbitmap(resource_path("icon.ico"))
        self.create_widgets()

    def create_widgets(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(expand=True)

        self.select_button = tk.Button(frame, text="选择WAV文件", command=self.select_file)
        self.select_button.pack(pady=20)

        self.file_label = tk.Label(frame, text="未选择文件", wraplength=350)
        self.file_label.pack(pady=10)

        self.progress = ttk.Progressbar(frame, mode='indeterminate')
        self.progress.pack(pady=10)

    def select_file(self):
        file_path = filedialog.askopenfilename(
            filetypes=[("WAV files", "*.wav")]
        )
        if file_path:
            self.file_label.config(text=file_path)
            self.start_conversion(file_path)

    def start_conversion(self, wav_path):
        self.progress.start()
        threading.Thread(target=self.convert_wav_to_mp3, args=(wav_path,)).start()

    def convert_wav_to_mp3(self, wav_path):
        try:
            mp3_path = wav_path.replace(".wav", ".mp3")
            subprocess.run(
                ["ffmpeg", "-i", wav_path, mp3_path],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                creationflags=subprocess.CREATE_NO_WINDOW
            )
            self.progress.stop()
            messagebox.showinfo("成功", f"转换完成:\n{mp3_path}")
        except Exception as e:
            self.progress.stop()
            messagebox.showerror("错误", f"转换失败: {str(e)}")

if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = WavToMp3Converter(root)
        root.mainloop()
    except Exception as e:
        messagebox.showerror("错误", f"程序初始化失败: {str(e)}")
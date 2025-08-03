# Install required module first: pip install pyttsx3
# pip install pyttsx3 langdetect PyPDF2


import pyttsx3
import tkinter as tk
from tkinter import filedialog, messagebox
import threading
from langdetect import detect
import PyPDF2

engine = pyttsx3.init()
voices = engine.getProperty('voices')

# Default settings
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

# Speak function
def engine_speak(text):
    engine.say(text)
    engine.runAndWait()

def speak_text():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Missing Input", "Please enter some text.")
        return

    # Apply settings
    engine.setProperty('voice', voices[voice_var.get()].id)
    engine.setProperty('rate', int(speed_scale.get()))
    engine.setProperty('volume', float(volume_scale.get()))

 
    # Detect language
    try:
        lang = detect(text)
        lang_label.config(text=f"Detected Language: {lang}")
    except:
        lang_label.config(text="Language: Unknown")

    # Speak in thread
    threading.Thread(target=lambda: engine_speak(text)).start()

def save_audio():
    text = text_input.get("1.0", tk.END).strip()
    if not text:
        messagebox.showwarning("Missing Input", "Please enter some text.")
        return

    filepath = filedialog.asksaveasfilename(defaultextension=".mp3",
                                            filetypes=[("MP3 Files", "*.mp3")])
    if filepath:
        engine.save_to_file(text, filepath)
        engine.runAndWait()
        messagebox.showinfo("Saved", f"Saved as {filepath}")

def load_file():
    filepath = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
    if filepath:
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, content)

def load_pdf():
    filepath = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
    if filepath:
        pdf_text = ""
        try:
            with open(filepath, 'rb') as file:
                reader = PyPDF2.PdfReader(file)
                for page in reader.pages:
                    pdf_text += page.extract_text()
            text_input.delete("1.0", tk.END)
            text_input.insert(tk.END, pdf_text)
        except Exception as e:
            messagebox.showerror("Error", f"Could not read PDF:\n{e}")

# --- GUI Setup ---
root = tk.Tk()
root.title("🗣️ Text-to-Speech Advanced")
root.geometry("500x650")
root.configure(bg="#1e1e1e")  # Dark mode background
root.resizable(False, False)

# Custom font and colors
LABEL_COLOR = "#f5f5f5"
BUTTON_COLOR = "#2a9d8f"
FONT = ("Arial", 11)

tk.Label(root, text="Enter Text:", bg="#1e1e1e", fg=LABEL_COLOR, font=FONT).pack(pady=5)
text_input = tk.Text(root, height=10, font=("Arial", 12), wrap=tk.WORD, bg="#2e2e2e", fg="#f5f5f5", insertbackground='white')
text_input.pack(padx=10, pady=5)

lang_label = tk.Label(root, text="Detected Language: ", bg="#1e1e1e", fg="#cccccc", font=("Arial", 10, "italic"))
lang_label.pack()

voice_frame = tk.Frame(root, bg="#1e1e1e")
voice_frame.pack(pady=5)
voice_var = tk.IntVar(value=0)
tk.Label(voice_frame, text="Voice:", bg="#1e1e1e", fg=LABEL_COLOR, font=FONT).pack(side=tk.LEFT)
tk.Radiobutton(voice_frame, text="Male", variable=voice_var, value=0, bg="#1e1e1e", fg=LABEL_COLOR, selectcolor="#444").pack(side=tk.LEFT)
tk.Radiobutton(voice_frame, text="Female", variable=voice_var, value=1, bg="#1e1e1e", fg=LABEL_COLOR, selectcolor="#444").pack(side=tk.LEFT)

tk.Label(root, text="Speed (Rate):", bg="#1e1e1e", fg=LABEL_COLOR, font=FONT).pack(pady=(10, 0))
speed_scale = tk.Scale(root, from_=100, to=250, orient=tk.HORIZONTAL, bg="#1e1e1e", fg=LABEL_COLOR, highlightthickness=0)
speed_scale.set(150)
speed_scale.pack(pady=5)

tk.Label(root, text="Volume:", bg="#1e1e1e", fg=LABEL_COLOR, font=FONT).pack(pady=(10, 0))
volume_scale = tk.Scale(root, from_=0.0, to=1.0, resolution=0.1, orient=tk.HORIZONTAL, bg="#1e1e1e", fg=LABEL_COLOR, highlightthickness=0)
volume_scale.set(1.0)
volume_scale.pack(pady=5)

btn_frame = tk.Frame(root, bg="#1e1e1e")
btn_frame.pack(pady=20)

def dark_button(text, command):
    return tk.Button(btn_frame, text=text, command=command, bg=BUTTON_COLOR, fg="white", width=12, font=("Arial", 10), relief=tk.FLAT)

dark_button("Speak", speak_text).grid(row=0, column=0, padx=5)
dark_button("Save Audio", save_audio).grid(row=0, column=1, padx=5)
dark_button("Load .txt", load_file).grid(row=1, column=0, padx=5, pady=5)
dark_button("Load PDF", load_pdf).grid(row=1, column=1, padx=5, pady=5)

root.mainloop()

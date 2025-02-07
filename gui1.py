from tkinter import *
from tkinter import ttk, messagebox
from googletrans import Translator, LANGUAGES

def translate_text():
    source_language = source_lang_var.get()
    target_language = dest_lang_var.get()
    text_to_translate = source_text.get("1.0", "end-1c").strip()

    if not text_to_translate:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return

    try:
        translator = Translator()
        translation = translator.translate(text_to_translate, src=source_language, dest=target_language)

        dest_text.config(state=NORMAL)
        dest_text.delete("1.0", "end")
        dest_text.insert("1.0", translation.text)
        dest_text.config(state=DISABLED)
    except Exception as e:
        messagebox.showerror("Translation Error", f"Error: {str(e)}")

# Create the main window
root = Tk()
root.title("English to Hindi Translator")
root.geometry("500x400")
root.configure(bg="#f0f0f0")

# Source text input
Label(root, text="Enter text in English:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
source_text = Text(root, height=5, width=50)
source_text.pack(pady=5)

# Source language selection
Label(root, text="Select Source Language:", font=("Arial", 10), bg="#f0f0f0").pack()
source_lang_var = StringVar(value="english")
source_lang_menu = ttk.Combobox(root, textvariable=source_lang_var, values=list(LANGUAGES.values()), state="readonly")
source_lang_menu.pack()

# Destination language selection
Label(root, text="Select Destination Language:", font=("Arial", 10), bg="#f0f0f0").pack()
dest_lang_var = StringVar(value="hindi")
dest_lang_menu = ttk.Combobox(root, textvariable=dest_lang_var, values=list(LANGUAGES.values()), state="readonly")
dest_lang_menu.pack()

# Translate button
Button(root, text="Translate", font=("Arial", 12), command=translate_text, bg="#007bff", fg="white").pack(pady=10)

# Destination text display
Label(root, text="Translation:", font=("Arial", 12), bg="#f0f0f0").pack()
dest_text = Text(root, height=5, width=50, state=DISABLED)
dest_text.pack(pady=5)

root.mainloop()

import tkinter as tk
from tkinter import ttk
from deep_translator import GoogleTranslator

def translate():
    text = source_widget.get('1.0', tk.END)
    target_lang = selected_lang.get()
    translated_text = GoogleTranslator(source="auto", target=target_lang).translate(text)
    translated_widget.delete('1.0', tk.END)
    translated_widget.insert('1.0', translated_text)

root = tk.Tk()

source_widget = tk.Text(root, width=30, height=10)
source_widget.pack()

label1 = ttk.Label(root, text="Translate to: ").pack()

selected_lang = tk.StringVar(value='km')

combobox = ttk.Combobox(
    root,
    values=['en','km','ja','zh-CN','de','ko'],
    state='readonly',
    textvariable=selected_lang
)

combobox.pack()

btn_translate = ttk.Button(root, text="Translate", command=translate)
btn_translate.pack()

translated_widget = tk.Text(root, width=30, height=10)
translated_widget.pack()

root.mainloop()

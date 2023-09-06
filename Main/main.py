from SearchPicturesAndSortByName import start
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("Python Skripte")
window.minsize(width=900, height=500)
window.config(bg="black")



def open_explorer_to_path1():
    ausgewaehlter_ordner = filedialog.askdirectory()
    link_entry1.insert(0, ausgewaehlter_ordner)
    return ausgewaehlter_ordner

def open_explorer_to_path2():
    ausgewaehlter_ordner = filedialog.askdirectory()
    link_entry2.insert(0, ausgewaehlter_ordner)
    return ausgewaehlter_ordner

def execute_function_from_other_place():
    start(link_entry1.get(), link_entry2.get())

# Label
headline_label = tk.Label(text="Skript zum sortieren und kopieren von Bildern von einem zum anderen Ordner", font=("Arial", 16, "bold"), background="black", foreground="white")
headline_label.place(x=45, y=40)

info_text = tk.Label(text="Bitte beaachten Sie, alle Bilder werden ausgeschnitten und duplicate werden ersetzt.", font=("Arial", 12, "bold"), background="black", foreground="white")
info_text.place(x=45, y=450)

link_lable1 = tk.Label(text="Ordner mit Bildern:", font=("Arial", 12, "bold"), background="black", foreground="white")
link_lable1.place(x=45, y=100)

# Entry
link_entry1 = tk.Entry(width=40, font=("Arial", 12, "bold"), background="gray", foreground="white")
link_entry1.place(x=275, y=100)

# Button
link_button1 = tk.Button(text="...", font=("Arial", 8,), background="black", foreground="white", command=open_explorer_to_path1)
link_button1.place(x=655, y=100)


link_lable2 = tk.Label(text="Ziel- Ordner der Bilder:", font=("Arial", 12, "bold"), background="black", foreground="white")
link_lable2.place(x=45, y=200)

# Entry
link_entry2 = tk.Entry(width=40, font=("Arial", 12, "bold"), background="gray", foreground="white")
link_entry2.place(x=275, y=200)

# Button
link_button2 = tk.Button(text="...", font=("Arial", 8,), background="black", foreground="white", command=open_explorer_to_path2)
link_button2.place(x=655, y=200)

summit_button = tk.Button(text="Start", font=("Arial", 12, "bold"), background="black", foreground="white", command=execute_function_from_other_place)
summit_button.place(x=400, y=300)




window.mainloop()

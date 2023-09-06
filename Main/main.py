from SearchPicturesAndSortByName import start
import tkinter as tk
from tkinter import filedialog

window = tk.Tk()
window.title("Bilder Sortieren")
window.iconbitmap("../img/razz-beere.ico")
window.minsize(width=900, height=500)
window.resizable(False, False)
dark_purple_rgb = (35, 9, 46)
dark_purple_hex = "#{:02x}{:02x}{:02x}".format(*dark_purple_rgb)
window.config(bg=dark_purple_hex)

def change_bg(new_value):
    dark_purple_hex = new_value
    window.config(bg=dark_purple_hex)
    headline_label.config(background=dark_purple_hex)
    info_text.config(background=dark_purple_hex)
    link_lable1.config(background=dark_purple_hex)
    link_lable2.config(background=dark_purple_hex)
    summit_button.config(background=dark_purple_hex)
    canvas.config(bg=dark_purple_hex)


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
headline_label = tk.Label(text="Ausschneiden und nach Erscheinungsjahr sortieren von Bildern", font=("Arial", 16, "bold"), background=dark_purple_hex, foreground="white")
headline_label.place(x=45, y=40)

info_text = tk.Label(text="Bitte beaachten Sie, alle Bilder werden ausgeschnitten und duplicate werden ersetzt.", font=("Arial", 12, "bold"), background=dark_purple_hex, foreground="white")
info_text.place(x=45, y=450)

link_lable1 = tk.Label(text="Ordner mit Bildern:", font=("Arial", 12, "bold"), background=dark_purple_hex, foreground="white")
link_lable1.place(x=45, y=100)

# Entry
link_entry1 = tk.Entry(width=40, font=("Arial", 12, "bold"), background="gray", foreground="white")
link_entry1.place(x=275, y=100)

# Button
link_button1 = tk.Button(text="...", font=("Arial", 8,), background="white", foreground="black", command=open_explorer_to_path1)
link_button1.place(x=655, y=100)


link_lable2 = tk.Label(text="Ziel- Ordner der Bilder:", font=("Arial", 12, "bold"), background=dark_purple_hex, foreground="white")
link_lable2.place(x=45, y=200)

# Entry
link_entry2 = tk.Entry(width=40, font=("Arial", 12, "bold"), background="gray", foreground="white")
link_entry2.place(x=275, y=200)

# Button
link_button2 = tk.Button(text="...", font=("Arial", 8,), background="white", foreground="black", command=open_explorer_to_path2)
link_button2.place(x=655, y=200)

summit_button = tk.Button(text="Start", font=("Arial", 12, "bold"), background=dark_purple_hex, foreground="white", command=execute_function_from_other_place)
summit_button.place(x=400, y=300)

canvas = tk.Canvas(window, width=35, height=150, bg=dark_purple_hex,  highlightthickness=0)
canvas.place(x=850, y=20)
round_button_red = canvas.create_oval(0, 0, 30, 30, fill="#570600")
round_button_blue = canvas.create_oval(0, 35, 30, 65, fill="#0a3b61")
round_button_green = canvas.create_oval(0, 70, 30, 100, fill="#0a611d")

canvas.tag_bind(round_button_red, "<Button-1>", lambda x: change_bg("#570600"))
canvas.tag_bind(round_button_blue, "<Button-1>", lambda x: change_bg("#0a3b61"))
canvas.tag_bind(round_button_green, "<Button-1>", lambda x: change_bg("#0a611d"))

window.mainloop()

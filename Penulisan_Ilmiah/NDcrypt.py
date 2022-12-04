#!/usr/bin/python3
# Path: NDcrypt.py

from tkinter.filedialog import askopenfilename  # Import file dialog
from tkinter.font import Font
from tkinter import *

from Vignere_Reverse import *
from PIL import Image, ImageTk # Import image

# Create a window
window = Tk()
window.state('zoomed')
# window.geometry("800x600")

# Set title of the window
window.title("Aplikasi Encrypt/Decrypt")

# Set the icon of the window
window.iconbitmap("icon_logo.ico")

# Set the font
font = Font(family="Helvetica", weight="bold", size=15)
bigFont = Font(family="Helvetica", weight="bold", size=20)

# Open image with PIL
logo = Image.open("logo_medium.png")
logo = ImageTk.PhotoImage(logo)
logo_label = Label(window, image=logo)
logo_label.pack(pady=80)

# Add label
start_label = Label(window, text="APLIKASI ENKRIPSI DEKRIPSI\nDENGAN METODE KOMBINASI VIGENERE CIPHER DAN REVERSE CIPHER\nMENGGUNAKAN PYTHON BERBASIS DESKTOP", font=bigFont, fg="black")
start_label.pack(pady=0)

# Delete all widgets from the window
def start():
    for widget in window.winfo_children():
        widget.destroy()
    
    # Click the input text box
    def click_1(event):
        input_text_box.delete(1.0, END)
        input_text_box.unbind("<Button-1>")
        
    # Click the key text box
    def click_2(event):
        key_box.delete(1.0, END)
        key_box.unbind("<Button-1>")

    # Clear the text box
    def clear_text_box():
        input_text_box.delete(1.0, END)
        key_box.delete(1.0, END)
        output_text_box.delete(1.0, END)

    # Open a file
    def open_file():
        file_name = askopenfilename(
            initialdir="C:/Users/User/Desktop/",
            title = "Select a file ...",
            filetypes=[
                ("Text files", "*.txt"),
                ("All files", "*.*")])
        if file_name:
            with open(file_name, "r") as file:
                input_text_box.insert(1.0, file.read())
                
        file = open(file_name, "r")
        input_text_box.insert(INSERT, file.read())
        file.close()   # Close the file   

    # Encrypt the text
    def get_encrypt():
        input_text = input_text_box.get(1.0, "end-1c")
        key_text = key_box.get(1.0, "end-1c")
        enc_output_text = reverse(vignere_encrypt(input_text, key_text))
        output_text_box.delete(1.0, END)
        output_text_box.insert("end-1c", enc_output_text)

    # Decrypt the text
    def get_decrypt():
        input_text = input_text_box.get(1.0, "end-1c")
        key_text = key_box.get(1.0, "end-1c")
        dec_output_text = vignere_decrypt(reverse(input_text), key_text)
        output_text_box.delete(1.0, END)
        output_text_box.insert("end-1c", dec_output_text)

    # Create a menu bar
    menu_bar = Menu(window)
    window.config(menu=menu_bar)

    # Add some menu items
    file_menu = Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="Open", command=open_file)
    file_menu.add_command(label="Clear", command=clear_text_box)
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)

    # Create the input text box
    input_text_box = Text(window, width=160, height=22, border=2)
    input_text_box.place(x=0, y=30)
    input_text_box.insert(INSERT, "Enter text here ...", "grey")
    input_text_box_label = Label(window, text="MESSAGE", font=font, fg="black")
    input_text_box_label.place(x=0, y=0)

    # Bind the text box with Mouse Button 1 to clear the text box
    input_text_box.bind("<Button-1>", click_1)

    # Create key text box
    key_box = Text(window, width=30, height=22, border=2)
    key_box.place(x=1290, y=30)
    key_box.insert(INSERT, "Enter key here ...", 'tags')
    key_box_label = Label(window, text="KEY", font=font, fg="black")
    key_box_label.place(x=1290, y=0)

    # Bind the text box with Mouse Button 1 to clear the text box
    key_box.bind("<Button-1>", click_2)

    # Create Encrypt button
    encrypt_button = Button(window, text="Encrypt", font=font, bg="red", fg="white", command=get_encrypt)
    encrypt_button.place(x=650, y=410)

    # Create Decrypt button
    decrypt_button = Button(window, text="Decrypt", font=font, bg="green", fg="white", command=get_decrypt)
    decrypt_button.place(x=750, y=410)

    # Create the output text box
    output_text_box = Text(window, width=191, height=18, border=2)
    output_text_box.place(x=0, y=487)
    output_text_box_label = Label(window, text="OUTPUT", font=font, fg="black")
    output_text_box_label.place(x=0, y=455)

# Start Button
start_btn = Button(window, text="Start", font=font, bg="black", fg="white", height=2, width=10, command=start)
start_btn.pack(pady=100)

window.mainloop()
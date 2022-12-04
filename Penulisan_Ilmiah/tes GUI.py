import tkinter

# Create a window menu
def create_menu(window):
    menu = tkinter.Menu(window)
    window.config(menu=menu)
    
    file_menu = tkinter.Menu(menu)
    menu.add_cascade(label="File", menu=file_menu)
    file_menu.add_command(label="New")
    file_menu.add_command(label="Open...")
    file_menu.add_separator()
    file_menu.add_command(label="Exit", command=window.quit)
    
    edit_menu = tkinter.Menu(menu)
    menu.add_cascade(label="Edit", menu=edit_menu)
    edit_menu.add_command(label="Cut")
    edit_menu.add_command(label="Copy")
    edit_menu.add_command(label="Paste")
    edit_menu.add_separator()
    edit_menu.add_command(label="Undo")
    
    help_menu = tkinter.Menu(menu)
    menu.add_cascade(label="Help", menu=help_menu)
    help_menu.add_command(label="About...")

# Create a window
def create_window():
    window = tkinter.Tk()
    window.title("Window Menu")
    create_menu(window)
    window.mainloop()

create_window()
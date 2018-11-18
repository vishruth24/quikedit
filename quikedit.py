import tkinter
from tkinter import Menu
from tkinter import *
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog,simpledialog,messagebox,font
# creating a tkinter object root
root = tkinter.Tk(className="QuikEdit")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
# creates text area
textPad = ScrolledText(root, width=w, height=h)
textPad.config(background="gray27",foreground="white",insertbackground="white",font=("Arial",20))  # Change parameters for different colors
# create a menu
# New file function
def new_file(event=None):
    if len(textPad.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno("Save the file","Do you wish to save the file?"):
            save_command()
        else:
            textPad.delete('1.0',END)
    root.title("Text Editor")
# Open file function
def open_command(event=None):
        file = filedialog.askopenfile(parent=root,mode='rb',title='Select a file')
        if file != None:
            contents = file.read()
            textPad.delete('1.0',END)
            textPad.insert('1.0',contents)
            file.close()
# Save command
def save_command(event=None):
    file = filedialog.asksaveasfile(mode='w')
    if file != None:
        data = textPad.get('1.0', END+'-1c')
        file.write(data)
        file.close()
# Exit command
def exit_command(event=None):
    if messagebox.askokcancel("Quit", "Do you really want to quit?"):
        root.destroy()
# About
def about_command():
    label = messagebox.showinfo("About", "A text edior built by NIE students")
# Find command to find number of occurances
def find_command(event=None):
    findstring=simpledialog.askstring("Find what?","Enter text")
    textstuff=textPad.get('1.0',END+'-1c')
    occurances=0
    occurances=textstuff.upper().count(findstring.upper())
    if occurances>0:
        messagebox.showinfo("Result",findstring+" has occured "+str(occurances)+" times!")
    else:
        messagebox.showinfo("Result",findstring+" does not occur!")
# Change the font family
def change_font():
    fontroot = Toplevel()
    fontroot.wm_title("Font Style")
    label=Label(fontroot,text="Please select the font and the font size")
    label.pack(pady=10)
    topframe=Frame(fontroot)
    topframe.pack()
    botframe=Frame(fontroot)
    botframe.pack()
    var = StringVar(topframe)
    var.set("Arial") # initial value
    option = OptionMenu(topframe, var,'Arial','Standard Symbols PS', 'DejaVu Math TeX Gyre', 'URW Gothic', 'Nimbus Roman', 'DejaVu Sans Mono', 'Nimbus Mono PS', 'DejaVu Sans', 'Nimbus Sans Narrow', 'DejaVu Serif', 'DejaVu Sans')
    option.pack(side="left")
    var1= StringVar(topframe)
    var1.set("10")
    optionfont=OptionMenu(topframe,var1,'10','20','30')
    optionfont.pack(side="right")
    def ok():
        varf=int(var1.get())
        font = (var.get(), varf)
        textPad.config(font=font)
    button = Button(botframe, text="OK", command=ok)
    button1=Button(botframe,text="Cancel",command=fontroot.destroy)
    button.pack(side="left")
    button1.pack(side="right")
# All basic operations
def cut():
    textPad.event_generate("<<Cut>>")
def copy():
    textPad.event_generate("<<Copy>>")
def paste():
    textPad.event_generate("<<Paste>>")

# Creating menu
# Menu ->File ->Edit ->Help
# File->New->Open->Save->Find->Exit
# Edit->Cut->Copy->Paste->Font
# Help->About
menu = Menu(root)
filemenu = Menu(menu)
editmenu=Menu(menu)
helpmenu = Menu(menu)

root.config(menu=menu)

menu.add_cascade(label="File", menu=filemenu)
menu.add_cascade(label="Edit",menu=editmenu)
menu.add_cascade(label="Help", menu=helpmenu)

filemenu.add_command(label="New", command=new_file,accelerator="Ctrl+N")
filemenu.add_command(label="Open...", command=open_command,accelerator="Ctrl+O")
filemenu.add_command(label="Save", command=save_command,accelerator="Ctrl+S")
filemenu.add_command(label="Find", command=find_command,accelerator="Ctrl+F")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=exit_command,accelerator="Ctrl+Q")
editmenu.add_command(label="Cut",command=cut)
editmenu.add_command(label="Copy",command=copy)
editmenu.add_command(label="Paste",command=paste)
editmenu.add_command(label="Font", command=change_font)
helpmenu.add_command(label="About...", command=about_command)

# Binding keyboard keys to functions
textPad.bind('<Control-S>',save_command)
textPad.bind('<Control-s>',save_command)
textPad.bind('<Control-n>',new_file)
textPad.bind('<Control-N>',new_file)
textPad.bind('<Control-O>',open_command)
textPad.bind('<Control-o>',open_command)
textPad.bind('<Control-f>',find_command)
textPad.bind('<Control-F>',find_command)
textPad.bind('<Control-q>',exit_command)
textPad.bind('<Control-Q>',exit_command)
textPad.pack()
root.mainloop()

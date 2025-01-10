from tkinter import *
from tkinter import messagebox
import json

root = Tk()
root.title("Notes App by Sagar")
root.geometry("500x500")
root.maxsize(500, 500)
root.minsize(500, 500)

img = PhotoImage(file="notes.png")
root.iconphoto(False, img)

#Save Notes
def savenotes():
    title = tle_val.get()
    content = cntnt.get("1.0",END).strip()
    new_note = {title: content}
        
    try:
        with open("notes.json", "r") as f:
            notes_data = json.load(f)
    except:
            notes_data = {}
        
    notes_data.update(new_note)         

    with open("notes.json", "w") as f:
        json.dump(notes_data, f)

        messagebox.showinfo("Success", "Note Saved Successfully!")
        tle_val.set("")
        cntnt.delete("1.0", END)

#Saved Notes
def savednotes():
    try:
        with open("notes.json", "r") as f:
            notes_data = json.load(f)
    except:
        messagebox.showinfo("No Notes", "No saved notes found!")
        return
    
    #Show Notes Window
    s_n_w = Toplevel(root)
    s_n_w.title("Saved Notes")
    s_n_w.geometry("400x400")

    Label(s_n_w, text="Saved Notes", fg="deep sky blue", font="comicsans 20 bold").pack(pady=10)

    for title, content in notes_data.items():
        Label(s_n_w, text=(f"Title: {title}"), font="comicsans 12 bold").pack(anchor="w", padx=20, pady=10)
        Label(s_n_w, text=(f"{content}"), font="Courier").pack(anchor="w", padx=20)

#Main Ui Window
Label(root, text="Notes",fg="deep sky blue", font="Courier 40 bold").pack(pady=20)

f1 = Frame(root)
f1.pack(pady=10)
Label(f1, text="Title:", font="comicsans 12").grid(row=0, column=0, padx=10)
tle_val = StringVar()
tle = Entry(f1, textvariable=tle_val, width=40, bg="ivory2", font="comicsans 12")
tle.grid(row=0, column=1, padx=10)

f2 = Frame(root)
f2.pack(pady=20)
Label(f2, text="Content:", font="comicsans 11").grid(row=0, column=0, sticky="n")
cntnt = Text(f2, bg="ivory2", height=7, width=36, font="Courier 12")
cntnt.grid(row=0, column=1, padx=8)

Button(root, text="Save Note", font="comicsans 15",bg="green", fg="white", command=savenotes).pack(pady=10)
Button(root, text="Show Saved Notes", font="comicsans 15",bg ="blue", fg="white", command=savednotes).pack(pady=10)


root.mainloop()
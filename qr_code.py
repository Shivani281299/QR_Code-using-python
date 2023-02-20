from tkinter import *
import pyqrcode
import png
from tkinter import filedialog
from PIL import Image,ImageTk

root = Tk()
root.title("QR Code Generator")
root.geometry("500x500")
root['background']='#ccb473'
lable1 =Label(root,text="QR Code Generator",font=("Helvetica",20),bg='#ccb473').pack(pady=20)

def create_code():
    input_path = filedialog.asksaveasfilename(title="Save Image",
                                              filetyp=(("PNG File",".png"),("All Files","*.*")))
    if input_path:
        if input_path.endswith(".png"):
            get_code =pyqrcode.create(entry.get())
            get_code.png(input_path,scale=5)

        else:
            input_path =f'{input_path}.png'
            get_code = pyqrcode.create(entry.get())
            get_code.png(input_path, scale=5)
            #add that .png to th end of the file name

        #put QR code on screen
        global get_image
        get_image =ImageTk.PhotoImage(Image.open(input_path))
        #add image to labe

        lable.config(image =get_image)
        entry.delete(0, END)
        entry.insert(0,"Finished!")

def clear_all():
    entry.delete(0,END)
    lable.config(image='')

#create GUI
entry =Entry(root,font=("Helvetica",20))
entry.pack(pady=20)



button =Button(root,text="Create QR Code",command=create_code,font=("Helvetica",20))
button.pack(pady=20)

button2 =Button(root,text="clear",command=clear_all,font=("Helvetica",20))
button2.pack()

lable =Label(root,text="")
lable.pack(pady=20)


root.mainloop()

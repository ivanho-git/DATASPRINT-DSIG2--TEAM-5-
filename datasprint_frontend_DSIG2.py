import tkinter as tk
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk
import matplotlib

window=tk.Tk()

#still now i can only upload images. Then when i integrate it with the backends then we can use this uploaded image for examining

def image_processor1():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        new_window = tk.Toplevel(window)
        new_window.title("Image Viewer")
        new_window.geometry("1000x600")

        # Load image
        img = Image.open(file_path)
        img_tk = ImageTk.PhotoImage(img)

        # Display image
        label = tk.Label(new_window, image=img_tk)
        label.image = img_tk   # keep reference
        label.pack(pady=20)

def image_processor2():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.gif")])
    if file_path:
        new_window = tk.Toplevel(window)
        new_window.title("Image Viewer")
        new_window.geometry("1000x600")

        # Load image
        img = Image.open(file_path)
        img_tk = ImageTk.PhotoImage(img)

        # Display image
        label = tk.Label(new_window, image=img_tk)
        label.image = img_tk   # keep reference
        label.pack(pady=20)

window.geometry("1000x550")

bg_pic=tk.PhotoImage(file="./background.jpg")
label_bg=tk.Label(window,image=bg_pic)
label_bg.pack()

label1 = tk.Label(window, text="WANT TO KNOW YOUR POTATO LEAF CONDITION?", font=('Times new roman',25,'bold'),bg='#d9d9d9',fg='black', bd=5,relief='raised')
label1.place(relx=0.1, rely=0.4)
label2 = tk.Label(window, text="SEND US YOUR PICTURE", font=('Times new roman',25,'bold'),bg='#d9d9d9',fg='black',bd=5,relief='raised')
label2.place(relx=0.35, rely=0.5)

button_ai = tk.Button(window, text="HIGH RESOLUTION", font=("Arial",15),fg="black",bg="#00FFCC",relief='raised', borderwidth='5' ,command=image_processor1)
button_ai.place(relx=0.3,rely=0.6)

button_ml = tk.Button(window, text="LOW RESOLUTION", font=("Arial",15),fg="black",bg="#00FFCC",relief='raised', borderwidth='5' ,command=image_processor2)
button_ml.place(relx=0.6,rely=0.6)


window.mainloop()


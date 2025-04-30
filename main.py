from tkinter import Tk, StringVar, Label

import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("400x400")
root.title("Fileion URL Shorter")
root.configure(bg="#49A")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladdress)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(root, text="Fileion's Shortener", font="poppins").pack(pady=15)
Entry(root, textvariable=url).pack(pady=5)
Button(root, text="Make Shorter", command=urlshortener).pack(pady=15)
Entry(root, textvariable=url_address).pack(pady=5)
Button(root, text="Copy URL", command=copyurl).pack(pady=15)
root.mainloop()
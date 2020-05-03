from tkinter import *
from pycrypto import *
from function import *

window = Tk()
window.title("Cryptography")
window.geometry("500x460")

#frame 1
frame1 = Frame(window)
frame1.pack()
label = Label(frame1,
    width = 26, 
    height = 2, 
    text="Cryptography Application",
    bg="lightgray", 
    font=("Helvetica", 25))
label.pack()

#frame 2
frame2 = Frame(window)
frame2.pack()

btn_des = Button(frame2, 
    width=20, 
    height = 2, 
    text="DES")
btn_des.pack(side=LEFT)
def btn_des_clicked():
    btn_des.configure(bg="gray")
    btn_aes.configure(bg="white")
    btn_rsa.configure(bg="white")
btn_des.configure(command=btn_des_clicked)

btn_aes = Button(frame2, 
    width=20, 
    height = 2, 
    text="AES")
btn_aes.pack(side=LEFT)
def btn_aes_clicked():
    btn_des.configure(bg="white")
    btn_aes.configure(bg="gray")
    btn_rsa.configure(bg="white")
btn_aes.configure(command=btn_aes_clicked)

btn_rsa = Button(frame2, 
    width=20, 
    height = 2, 
    text="RSA")
btn_rsa.pack(side=LEFT)
def btn_rsa_clicked():
    btn_des.configure(bg="white")
    btn_aes.configure(bg="white")
    btn_rsa.configure(bg="gray")
btn_rsa.configure(command=btn_rsa_clicked)

#frame 3
frame3 = Frame(window)
frame3.pack()

btn_file = Button(frame3, 
    width=31, 
    height = 2, 
    text="choose file")
btn_file.pack(side=LEFT)
def btn_file_clicked():
    btn_file.configure(bg="gray")
btn_file.configure(command=btn_file_clicked)

btn_key = Button(frame3, 
    width=30, 
    height = 2, 
    text="choose file key")
btn_key.pack(side=LEFT)
def btn_key_clicked():
    btn_key.configure(bg="gray")
btn_key.configure(command=btn_key_clicked)

#frame 4
frame4 = Frame(window)
frame4.pack()

mess_key = Label(frame4,
    width = 63, 
    height = 15,
    bg="white",
    anchor = NW,
    text="Key is: ")
mess_key.pack()

#frame 5
frame5 = Frame(window)
frame5.pack()

btn_encode = Button(frame5, 
    width=31, 
    height = 2, 
    text="ENCODE")
btn_encode.pack(side=LEFT)
def btn_encode_clicked():
    btn_encode.configure(bg="gray")
btn_encode.configure(command=btn_encode_clicked)

btn_decode = Button(frame5, 
    width=31, 
    height = 2, 
    text="ENCODE")
btn_decode.pack(side=LEFT)
def btn_decode_clicked():
    btn_decode.configure(bg="gray")
btn_decode.configure(command=btn_decode_clicked)

window.mainloop()
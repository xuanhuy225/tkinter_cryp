from tkinter import *
from function import *
from Crypto.Cipher import DES3
from Crypto import Random
from enum import Enum
from tkinter import filedialog

class alg(Enum):
    des=1
    aes=2
    sra=3
type_crypt = alg.des

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
    type_crypt=alg.des
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
    type_crypt=alg.aes
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
    type_crypt=alg.rsa
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
    link_file = filedialog.askopenfilenames(
        initialdir='/',
    	filetypes=[
    		("All files", "*"),
            ("txt", "*.txt"),
            ("PNG", "*.png"),
            ("JPEG", "*.jpg"),
            ("PDF", "*.pdf"),
            ("MP3", "*.mp3"),
            ("MP4", "*.mp4")])
    print(link_file[0])
    f=open(link_file[0],'r')
    file_cont = f.read()
    f.close()
    print(file_cont)
btn_file.configure(command=btn_file_clicked)

btn_key = Button(frame3, 
    width=30, 
    height = 2, 
    text="choose file key")
btn_key.pack(side=LEFT)
def btn_key_clicked():
    btn_key.configure(bg="gray")
    link_key = filedialog.askopenfilenames(
        initialdir='/',
    	filetypes=[
    		("txt", ".txt")])
    f=open(link_key[0],'r')
    key = f.read()
    f.close()   
btn_key.configure(command=btn_key_clicked)

#frame 4
frame4 = Frame(window)
frame4.pack()

mess_stt = Label(frame4,
    width = 63, 
    height = 15,
    bg="white",
    anchor = NW,
    text="Status:\n")
mess_stt.pack()

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

# key = b'Sixteen byte key'
# iv = Random.new().read(DES3.block_size)
# cipher = DES3.new(key, DES3.MODE_OFB, iv)
# plaintext = b'sona si latine loqueris '
# msg = iv + cipher.encrypt(plaintext)
# messagebox.showinfo( "Hello",msg)


window.mainloop()
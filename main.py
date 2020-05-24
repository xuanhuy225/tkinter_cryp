from tkinter import *
from function import *
from Crypto.Cipher import DES3
from enum import Enum
from tkinter import filedialog

key = ""
fileIn = ""
link_key_rsa = ""
origin_file = ""

class alg(Enum):
    des=1
    aes=2
    rsa=3
type_crypt = alg.des

window = Tk()
window.title("Cryptography")
window.geometry("500x500")

#frame 1------------------------------------------
frame1 = Frame(window)
frame1.pack()
label = Label(frame1,
    width = 26, 
    height = 2, 
    text="Cryptography Application",
    bg="lightgray", 
    font=("Helvetica", 25))
label.pack()

#frame 2------------------------------------------
frame2 = Frame(window)
frame2.pack()

btn_des = Button(frame2, 
    width=20, 
    height = 2, 
    text="DES")
btn_des.pack(side=LEFT)
def btn_des_clicked():
    global type_crypt
    type_crypt=alg.des
    btn_des.configure(bg="gray")
    btn_aes.configure(bg="whitesmoke")
    btn_rsa.configure(bg="whitesmoke")
btn_des.configure(command=btn_des_clicked)

btn_aes = Button(frame2, 
    width=20, 
    height = 2, 
    text="AES")
btn_aes.pack(side=LEFT)
def btn_aes_clicked():
    global type_crypt
    type_crypt = alg.aes
    btn_des.configure(bg="whitesmoke")
    btn_aes.configure(bg="gray")
    btn_rsa.configure(bg="whitesmoke")
btn_aes.configure(command=btn_aes_clicked)

btn_rsa = Button(frame2, 
    width=20, 
    height = 2, 
    text="RSA")
btn_rsa.pack(side=LEFT)
def btn_rsa_clicked():
    global type_crypt
    type_crypt=alg.rsa
    btn_des.configure(bg="whitesmoke")
    btn_aes.configure(bg="whitesmoke")
    btn_rsa.configure(bg="gray")
btn_rsa.configure(command=btn_rsa_clicked)

#frame 3------------------------------------------
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
    global fileIn
    fileIn = link_file[0]
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
    global link_key_rsa
    link_key_rsa = link_key[0]
    f=open(link_key[0],'r')
    global key
    key = f.read()
    f.close()
btn_key.configure(command=btn_key_clicked)

#frame 4------------------------------------------
frame4 = Frame(window)
frame4.pack()

mess_stt = Label(frame4,
    width = 63, 
    height = 15,
    bg="white",
    anchor = NW,
    text="Status:\n")
mess_stt.pack()


#frame 5------------------------------------------
frame5 = Frame(window)
frame5.pack()

btn_encode = Button(frame5, 
    width=31, 
    height = 2, 
    text="ENCODE")
btn_encode.pack(side=LEFT)
def btn_encode_clicked():
    btn_encode.configure(bg="gray")
    btn_decode.configure(bg="whitesmoke")
    if type_crypt == alg.des:
        des_encrypt_file(getKey(key), fileIn)
    elif type_crypt == alg.aes:
        aes_encrypt_file(getKey(key), fileIn)
    else:
        rsa_encrypt_file(link_key_rsa, fileIn)
btn_encode.configure(command=btn_encode_clicked)

btn_decode = Button(frame5, 
    width=31, 
    height = 2, 
    text="DECODE")
btn_decode.pack(side=LEFT)
def btn_decode_clicked():
    btn_decode.configure(bg="gray")
    btn_encode.configure(bg="whitesmoke")
    if type_crypt == alg.des:
        des_decrypt_file(getKey(key), fileIn)
    elif type_crypt == alg.aes:
        aes_decrypt_file(getKey(key), fileIn)
    else:
        rsa_decrypt_file(link_key_rsa, fileIn)
    btn_origin_file.configure(state = "active")
    btn_check.configure(state = "active")
btn_decode.configure(command=btn_decode_clicked)

#frame 6------------------------------------------
frame6 = Frame(window)
frame6.pack()

btn_origin_file = Button(frame6, 
    width=31, 
    height = 2, 
    state = "disable",
    text="choose origin file")
btn_origin_file.pack(side=LEFT)
def btn_origin_file_clicked():
    btn_origin_file.configure(bg="gray")
    link_origin_file = filedialog.askopenfilenames(
        initialdir='/',
    	filetypes=[
    		("All files", "*"),
            ("txt", "*.txt"),
            ("PNG", "*.png"),
            ("JPEG", "*.jpg"),
            ("PDF", "*.pdf"),
            ("MP3", "*.mp3"),
            ("MP4", "*.mp4")])
    global origin_file
    origin_file = link_origin_file[0]
btn_origin_file.configure(command=btn_origin_file_clicked)

btn_check = Button(frame6, 
    width=31, 
    height = 2, 
    state = "disable",
    text="Check integrity")
btn_check.pack(side=LEFT)
def btn_check_clicked():
    btn_check.configure(bg="gray")
    checkMD5(origin_file)
btn_check.configure(command=btn_check_clicked)

window.mainloop()
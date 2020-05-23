from tkinter import messagebox
from Crypto.Hash import MD5
from Crypto.Cipher import DES
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto import Random
import os, struct
from Crypto.Cipher import PKCS1_OAEP

des_file = ""

def getKey(key):
    hasher = MD5.new(key.encode('utf-8'))
    return hasher.digest()

def des_encrypt_file(key, in_filename, out_filename=None, chunksize = 64*1024):
    if len(key) == 0:
        messagebox.showinfo( "error","the file key is empty")
        return
    if len(in_filename) == 0:
        messagebox.showinfo( "error","no input file")
        return

    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = Random.new().read(DES.block_size)
    encryptor = DES.new(key[:8], DES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))
    messagebox.showinfo("","encode complete")

def des_decrypt_file(key, in_filename, out_filename=None, chunksize = 64*1024):
    if len(key) == 0:
        messagebox.showinfo( "error","the file key is empty")
        return
    if len(in_filename) == 0:
        messagebox.showinfo( "error","no input file")
        return

    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    global des_file
    des_file = out_filename
        
    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(DES.block_size)
        decryptor = DES.new(key[:8], DES.MODE_CBC, iv)
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize)
    messagebox.showinfo("","decode complete")

def aes_encrypt_file(key, in_filename, out_filename=None, chunksize = 64*1024):
    if len(key) == 0:
        messagebox.showinfo( "error","the file key is empty")
        return
    if len(in_filename) == 0:
        messagebox.showinfo( "error","no input file")
        return

    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)
                outfile.write(encryptor.encrypt(chunk))
    messagebox.showinfo("","encode complete")

def aes_decrypt_file(key, in_filename, out_filename=None, chunksize = 64*1024):
    if len(key) == 0:
        messagebox.showinfo( "error","the file key is empty")
        return
    if len(in_filename) == 0:
        messagebox.showinfo( "error","no input file")
        return

    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    global des_file
    des_file = out_filename

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(AES.block_size)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))
            outfile.truncate(origsize)
    messagebox.showinfo("","decode complete")

def init_key_RSA(link_key):
    key = RSA.generate(2048)
    namePriv = os.path.splitext(link_key)[0] + "_priKey.pem"
    namePubl = os.path.splitext(link_key)[0] + "_pubKey.pem"
    f = open(namePriv,'wb')
    f.write(key.exportKey('PEM'))
    f.close()
    f = open(namePubl,'wb')
    f.write(key.publickey().exportKey('PEM'))
    f.close()

def rsa_encrypt_file(link_key, in_filename, out_filename=None, chunksize = 214):
    if len(link_key) == 0:
        messagebox.showinfo( "error","the file key hasn't chosen")
        return
    if len(in_filename) == 0:
        messagebox.showinfo( "error","no input file")
        return
    init_key_RSA(link_key)
    if not out_filename:
        out_filename = in_filename + '.enc'
    
    f = open(os.path.splitext(link_key)[0] + "_pubKey.pem")
    key = f.read()
    RSAkey = RSA.importKey(key)
    f.close()

    cipher = PKCS1_OAEP.new(RSAkey)
    
    filesize = os.path.getsize(in_filename)

    with open(in_filename, "rb") as inFile:
        with open(out_filename, "wb") as outFile:
            while True:
                chunk = inFile.read(chunksize)
                if len(chunk) == 0:
                    break
                encrypt_chunk = cipher.encrypt(chunk)
                outFile.write(encrypt_chunk)
    messagebox.showinfo("","encode complete")

def rsa_decrypt_file(link_key, in_filename, out_filename=None, chunksize = 256):
    if len(link_key) == 0:
        messagebox.showinfo( "error","the file key is empty")
        return
    if len(in_filename) == 0:
        messagebox.showinfo( "error","no input file")
        return

    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]
    global des_file
    des_file = out_filename

    f = open(os.path.splitext(link_key)[0] + "_priKey.pem")
    RSAkey = RSA.importKey(f.read())
    f.close()
    
    cipher = PKCS1_OAEP.new(RSAkey)

    filesize = os.path.getsize(in_filename)
    with open(in_filename, "rb") as inFile:
        with open(out_filename, "wb") as outFile:
            while True:
                chunk = inFile.read(chunksize)
                if len(chunk) == 0:
                    break
                decrypt_chunk = cipher.decrypt(chunk) #error
                outFile.write(decrypt_chunk)
    messagebox.showinfo("","decode complete")

def checkMD5(origin_file):
    if len(des_file) == 0:
        messagebox.showinfo( "error","no destination file")
        return
    if len(origin_file) == 0:
        messagebox.showinfo( "error","no origin file")
        return
    
    

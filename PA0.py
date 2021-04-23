from tkinter import *
ui = Tk()
ui.geometry("800x570")
ui.configure(background="AntiqueWhite1", highlightbackground="blue") 

toplabel = Label(ui, text="ATBASH CIPHER" , font=("Helvetica", 25), bg ="DeepPink3", fg = "pink")
toplabel.place(x=280, y=20)
toplabel.pack(fill=X)

# Buttoned encryption-decryption
def but_encrypt():
    but_ciphertext.delete(0.0, 'end')
    p = but_plaintext.get(0.0, 'end')
    k = ""
    for i in range(len(p)):
        if p[i]!=" " and p[i]!='\n' and p[i]!="\t":
            if ord(p[i]) in range(97,123):
                k += chr(96 + 26-(ord(p[i])-97))
            elif ord(p[i]) in range(65,91):
                k += chr(64 + 26-(ord(p[i])-65))
            else:
                k += p[i]                
        else:
            k += p[i]
    but_ciphertext.insert(0.0, k)
    
def but_decrypt():
    but_plaintext.delete(0.0, 'end')
    c = but_ciphertext.get(0.0, 'end')
    k=""
    for i in range(len(c)):
        if c[i]!=" " and c[i]!='\n' and c[i]!="\t":
            if ord(c[i]) in range(97,123):
                k += chr(96 + 26-(ord(c[i])-97))
            elif ord(p[i]) in range(65,91):
                k += chr(64 + 26-(ord(c[i])-65))
            else:
                k += c[i]
        else:
            k += c[i]
    but_plaintext.insert(0.0, k)



l1 = Label(ui, text="# Buttoned encryption-decryption" , font=("Helvetica", 15), bg ="AntiqueWhite1", fg = "gray10")
l1.place(x=30, y=80)


but_plabel = Label(ui, text="PLAINTEXT", bg="AntiqueWhite1", fg="gray20", relief="flat")
but_plabel.place(x=30, y=120)

but_plaintext = Text(ui, height = 6, width=43, bg = "snow", fg="black", relief="flat", highlightthickness="2px")
but_plaintext.place(x=30, y=150)

but_encipher = Button(ui, text="Encipher", width=7, height=1, command=but_encrypt, relief="flat", highlightthickness="2px", bg="teal", fg="azure")
but_encipher.place(x=30, y=280)



but_clabel = Label(ui, text="CIPHERTEXT", bg="AntiqueWhite1", fg="gray20", relief="flat")
but_clabel.place(x=410, y=120)

but_ciphertext = Text(ui, height = 6, width=43, bg = "snow", fg="black", relief="flat", highlightthickness="2px")
but_ciphertext.place(x=410, y=150)

but_decipher = Button(ui, text="Decipher", width=7, height=1, command=but_decrypt, relief="flat", highlightthickness="2px", bg="teal", fg="azure")
but_decipher.place(x=700, y=280)


# As-you-type encryption-decryption
def encrypt(*args):
    ciphertext.delete(0.0, 'end')
    p = plaintext.get(0.0, 'end')
    k = ""
    for i in range(len(p)):
        if p[i]!=" " and p[i]!='\n' and p[i]!="\t":
            if ord(p[i]) in range(97,123):
                k += chr(96 + 26-(ord(p[i])-97))
            elif ord(p[i]) in range(65,91):
                k += chr(64 + 26-(ord(p[i])-65))
            else:
                k += p[i]
        else:
            k += p[i]
    ciphertext.insert(0.0, k)

    
def decrypt(*args):
    plaintext.delete(0.0, 'end')
    c = ciphertext.get(0.0, 'end')
    k=""
    for i in range(len(c)):
        if c[i]!=" " and c[i]!='\n'and c[i]!="\t":
            if ord(c[i]) in range(97,123):
                k += chr(96 + 26-(ord(c[i])-97))
            elif ord(p[i]) in range(65,91):
                k += chr(64 + 26-(ord(c[i])-65))
            else:
                k += c[i]
        else:
            k += c[i]
    plaintext.insert(0.0, k)


l2 = Label(ui, text="# As-you-type encryption-decryption" , font=("Helvetica", 15), bg ="AntiqueWhite1", fg = "gray10")
l2.place(x=30, y=350)


plabel = Label(ui, text="PLAINTEXT", bg="AntiqueWhite1", fg="gray20", relief="flat")
plabel.place(x=30, y=390)

plaintext = Text(ui, height = 6, width=43, bg = "snow", fg="black", relief="flat", highlightthickness="2px")
plaintext.place(x=30, y=420)
plaintext.bind('<Any-KeyRelease>', encrypt)


clabel = Label(ui, text="CIPHERTEXT", bg="AntiqueWhite1", fg="gray20", relief="flat")
clabel.place(x=410, y=390)

ciphertext = Text(ui, height = 6, width=43, bg = "snow", fg="black", relief="flat", highlightthickness="2px")
ciphertext.place(x=410, y=420)
ciphertext.bind('<Any-KeyRelease>', decrypt)


ui.mainloop()
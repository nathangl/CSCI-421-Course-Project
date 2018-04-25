#client.py
#client to client chat program encrypted with ciphers from class
#Group 4: Nathaniel Law, Anca-Maria Murgoci, Damilola Olakunle, Callum Walsh

import os, sys, time, threading, random, string
from Tkinter import *
from socket import *
from cipherlib import *

host = "127.0.0.1"

#check for arguments
if(len(sys.argv) < 3) :
    print "Enter: python client.py listenport sendport"
    sys.exit()

listenPort = int(sys.argv[1])
sendPort = int(sys.argv[2])

buf = 1024

addrSend = (host,sendPort)
addrListen = (host,listenPort)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addrListen)

#vars for received data
messageReceived = False
messageData = 'default'

#set by chosen button, defaults to Caesar
encryptionMethod = 'Caesar'

class ClientListener(threading.Thread):
    def __init__(self, root):
        threading.Thread.__init__(self)
        self.GUI()

    def GUI(self):
        root.title("Encrypted Chat")
        root.geometry("350x500")

        #ENCRYPTION METHOD
        def encrypt(text):
            global encryptionMethod
            key = keyBox.get()
            if encryptionMethod == "Caesar":
                return getEncryptedCaesarMessage(text, int(key))
            elif encryptionMethod == "Mono":
                #not currently working
                return text
            elif encryptionMethod == "Vignere":
                return getEncryptedVignereMessage(text, key)
            elif encryptionMethod == "Playfair":
                return getEncryptedPlayfairMessage(text, key)

        #DECRYPTION METHOD
        def decrypt(text):
            global encryptionMethod
            key = keyBox.get()
            if encryptionMethod == "Caesar":
                return getDecryptedCaesarMessage(text, int(key))
            elif encryptionMethod == "Mono":
                #not currently working
                return text
            elif encryptionMethod == "Vignere":
                return getDecryptedVignereMessage(text, key)
            elif encryptionMethod == "Playfair":
                return getDecryptedPlayfairMessage(text, key)

        #sends message from inputbox to other client
        def sendMessage():
            temp = inputBox.get()
            output.insert(INSERT, "Client 1: " + temp + "\n")
            inputBox.delete(0, END)
            temp = encrypt(temp)
            UDPSock.sendto(temp, addrSend)

        #defines encrypt method from chosen button
        def setEncrypt(method):
            global encryptionMethod
            encryptionMethod = method

        #checks for if a message was received, prints message if found
        def listen():
            global messageReceived
            global messageData
            if messageReceived == True:
                global encryptionMethod
                text = decrypt(messageData)
                output.insert(INSERT, str("Client 2: " + text + "\n"))
                messageReceived = False
            root.after(500, listen)

        #Chat input box
        inputBox = Entry(root, bg="light blue")
        inputBox.grid(row=5, column=1, columnspan = 3)

        #Key input box
        keyBox = Entry(root, bg="grey")
        keyBox.grid(row=0, column=1, columnspan = 3)

        #Key Label
        keyText = Label(root, text = "Enter Key: ", width = 8, height = 5)
        keyText.grid(row=0, column=0)

        #Send Button
        Button(root, width=17, text ="send", command = sendMessage).grid(row=6, column=1, columnspan = 3)

        #Method Label
        methodText = Label(root, text = "Choose: ", width = 8, height = 5)
        methodText.grid(row=1, column=0)

        #Caesar Button
        Button(root, width=5, text ="Caesar", command= lambda: setEncrypt("Caesar")).grid(row=1, column=1, columnspan = 1)

        #Mono Button
        Button(root, width=5, text ="Mono", command= lambda: setEncrypt("Mono")).grid(row=1, column=2, columnspan = 1)

        #Vignere Button
        Button(root, width=5, text ="Vignere", command= lambda: setEncrypt("Vignere")).grid(row=1, column=3, columnspan = 1)

        #Playfair Button
        Button(root, width=5, text ="Playfair", command= lambda: setEncrypt("Playfair")).grid(row=1, column=4, columnspan = 1)

        #Output / Chat History
        output = Text(root, width = 30, height = 20, background="white", fg = 'blue')
        output.grid(row=2, column=1, columnspan = 3)

        listen()

    def run(self):
        while True:
            (data, addrListen) = UDPSock.recvfrom(buf)
            global messageReceived
            messageReceived = True
            global messageData
            messageData = data

root = Tk()
clientListenerThread = ClientListener(root)
clientListenerThread.daemon = True
clientListenerThread.start()
root.mainloop()

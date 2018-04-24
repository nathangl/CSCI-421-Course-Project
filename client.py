import os, sys, time, threading
from Tkinter import *
from socket import *
from CaesarcipherEncrypt import *
from CaesarcipherDecrypt import *
from keylibrary import *
from keylib import *

host = "127.0.0.1"
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

messageReceived = False
messageData = 'default'
encryptionMethod = 'default'

class ClientListener(threading.Thread):
    def __init__(self, root):
        threading.Thread.__init__(self)
        self.GUI()

    def GUI(self):
        root.title("Encrypted Chat")
        root.geometry("350x500")

        def encrypt(text):
            global encryptionMethod
            print encryptionMethod
            if encryptionMethod == "Caesar":
                key = 5
                return getEncryptedCaesarMessage(text, key)
            elif encryptionMethod == "Mono":
                key = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
                key.lower()
                #inverse = inverse_monoalpha_cipher(text)
                return encrypt_with_monoalpha(text, key)
            elif encryptionMethod == "Vignere":
                key = 'bob'
            elif encryptionMethod == "Playfair":
                key = 'GoHounds'
                key = playKey(key)
                matrix = playMatrix(key)
                pairs = playPairs(text)
                encrypt = playEncrypt(matrix, pairs)

                finalText = ''
                for pair in encrypt:
                    finalText += pair + ' '

                return finalText

        #DECRYPTION METHOD
        def decrypt(text):
            global encryptionMethod
            print encryptionMethod
            if encryptionMethod == "Caesar":
                key = 5
                return getDecryptedCaesarMessage(text, key)
            elif encryptionMethod == "Mono":
                key = 'BCDEFGHIJKLMNOPQRSTUVWXYZA'
                key.lower()
                inverse = inverse_monoalpha_cipher(text)
                return encrypt_with_monoalpha(inverse, key)
            elif encryptionMethod == "Vignere":
                key = 'bob'
            elif encryptionMethod == "Playfair":
                key = 'GoHounds'
                key = playKey(key)
                matrix = playMatrix(key)
                pairs = playPairs(text)
                encrypt = playDecrypt(matrix, pairs)

                finalText = ''
                for pair in encrypt:
                    finalText += pair + ' '

                return finalText

        def sendMessage():
            temp = inputBox.get()
            output.insert(INSERT, "Client 1: " + temp + "\n")
            #output['text'] = output['text'] + "Client 1: " + temp + "\n"
            inputBox.delete(0, END)
            temp = encrypt(temp)
            UDPSock.sendto(temp, addrSend)

        def setEncrypt(method):
            global encryptionMethod
            encryptionMethod = method

        def listen():
            global messageReceived
            global messageData
            if messageReceived == True:
                text = decrypt(messageData)
                output.insert(INSERT, str("Client 2: " + text + "\n"))
                #output['text'] = output['text'] + "Client 2: " + messageData + "\n"
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
        output = Text(root, width = 20, height = 20, background="white", fg = 'blue')
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

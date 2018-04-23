import os, sys, time, threading
from Tkinter import *
from socket import *
from CaesarcipherEncrypt import *
from CaesarcipherDecrypt import *

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

class ClientListener(threading.Thread):
    def __init__(self, root):
        threading.Thread.__init__(self)
        self.GUI()

    def GUI(self):
        root.title("Input Output")
        root.geometry("200x200")

        def sendMessage():
            temp = inputBox.get()
            output['text'] = output['text'] + "Client 1: " + temp + "\n"
            inputBox.delete(0, END)
            temp = getEncryptedMessage(temp, 5)
            UDPSock.sendto(temp, addrSend)

        def listen():
            global messageReceived
            global messageData
            if messageReceived == True:
                messageData = getDecryptedMessage(messageData, 5)
                output['text'] = output['text'] + "Client 2: " + messageData + "\n"
                messageReceived = False
            root.after(500, listen)

        inputBox = Entry(root, bg="lightblue")
        inputBox.grid(row=0, column=0, columnspan = 3)

        Button(root, width=20, text ="send", command = sendMessage).grid(row=1, column=0, columnspan = 3)

        scrollbar = Scrollbar(root)
        scrollbar.pack(side = RIGHT, fill = Y)

        output = Label(root, text = "", width = 20, height = 20, background="white", fg = 'blue', yscrollcommand = scrollbar.set)
        output.grid(row=2, column=0, columnspan = 3)
        output.pack(SIDE = LEFT, fill = BOTH)
        scrollbar.config(command = output.yview)

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

import os, sys, time, threading
from Tkinter import *
from socket import *

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
        '''
        def run(self):
            (data, addrListen) = UDPSock.recvfrom(buf)
            output['text'] = output['text'] + "Client 2: " + temp + "\n"
        '''

        def sendMessage():
            temp = inputBox.get()
            output['text'] = output['text'] + "Client 1: " + temp + "\n"
            inputBox.delete(0, END)
            UDPSock.sendto(temp, addrSend)

            '''
            def forword(sendPort, listenPort):
                string = ' '
                while string:
                    string = UDPSock.rcvfrom(buf)
                    if string:
                        listenPort.sendto(string)
                    else:
                        sendPort.shutdown(socket.SHUT_RD)
                        listenPort.shutdown(socket.SHUT_WR)
            '''

        def listen():
            global messageReceived
            global messageData
            if messageReceived == True:
                output['text'] = output['text'] + "Client 2: " + messageData + "\n"
                messageReceived = False
            root.after(500, listen)

        inputBox = Entry(root, bg="lightblue")
        inputBox.grid(row=0, column=0, columnspan = 3)

        Button(root, width=20, text ="send", command = sendMessage).grid(row=1, column=0, columnspan = 3)

        output = Label(root, text = "", width = 20, height = 2, background="light blue")
        output.grid(row=2, column=0, columnspan = 3)

        listen()

        #master.after(0, listen)

    def run(self):
        while True:
            (data, addrListen) = UDPSock.recvfrom(buf)
            global messageReceived
            messageReceived = True
            global messageData
            messageData = data
            #output['text'] = output['text'] + "Client 2: " + data + "\n"
            #master.after_idle(500, listen)


class Gui(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        master = Tk()
        master.title("Input Output")
        master.geometry("200x200")
        '''
        def run(self):
            (data, addrListen) = UDPSock.recvfrom(buf)
            output['text'] = output['text'] + "Client 2: " + temp + "\n"
        '''

        def sendMessage():
            temp = inputBox.get()
            output['text'] = output['text'] + "Client 1: " + temp + "\n"
            inputBox.delete(0, END)
            UDPSock.sendto(temp, addrSend)
            print 'sent'

            '''
            def forword(sendPort, listenPort):
                string = ' '
                while string:
                    string = UDPSock.rcvfrom(buf)
                    if string:
                        listenPort.sendto(string)
                    else:
                        sendPort.shutdown(socket.SHUT_RD)
                        listenPort.shutdown(socket.SHUT_WR)
            '''

        inputBox = Entry(master, bg="lightblue")
        inputBox.grid(row=0, column=0, columnspan = 3)

        Button(master, width=20, text ="send", command = sendMessage).grid(row=1, column=0, columnspan = 3)

        output = Label(master, text = "", width = 20, height = 2, background="light blue")
        output.grid(row=2, column=0, columnspan = 3)

        #master.after(0, listen)

        master.mainloop()

root = Tk()
'''
GuiThread = Gui(root)
GuiThread.start()
'''
clientListenerThread = ClientListener(root)
clientListenerThread.daemon = True
clientListenerThread.start()
root.mainloop()





'''
host = "127.0.0.1"
if(len(sys.argv) < 3) :
    print "Enter: python client.py listenport sendport"
    sys.exit()

listenPort = int(sys.argv[1])
sendPort = int(sys.argv[2])

buf = 1024

addr = (host,sendPort)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    #data = input("Enter message or type 'exit'")
    data = raw_input("Enter message or type 'exit'")
    #data = data.encode('utf-8')
    UDPSock.sendto(data, addr)
    (data, addr) = UDPSock.recvfrom(buf)
    print("Received message: " + data)
    if data == "exit":
        break

UDPSock.close()
os._exit(0)
'''

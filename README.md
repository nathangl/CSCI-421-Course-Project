# CSCI-421-Course-Project
Python Encrypted Chat Program

This program allows encrypted chat between two clients on a local address using UDP. The user may select which cipher to use, as well as their respective keys.

Requires Tkinterface and Python 2.7.5

To run: 'python client.py listenport sendport' for both clients

client 1 listen port == client 2 send port
client 1 send port == client 2 listen port

Caesar takes an integer key.
Vignere takes a string key.
Monoalphabetic takes a string of one alphabet with no duplicate letters.
Playfair takes a string key.

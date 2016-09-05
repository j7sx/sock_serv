#!/usr/bin/python2

import socket

HOST, PORT = "localhost", 4449

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))

while 1:
    data = raw_input(">>>: ")
    sock.sendall(bytes(data + "\n"))
    print "Sent:     {}".format(bytes(data))

    # Receive data from the server and shut down
    received = sock.recv(1024)
    print "Received: {}".format(received)
    if not data:
        sock.close()

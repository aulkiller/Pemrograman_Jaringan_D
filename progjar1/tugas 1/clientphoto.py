import sys
import socket
import base64
import os

# Listening Port
portz = [5000, 5002]

for i in portz:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('192.168.161.128', i)
    print(f"connecting to {server_address}")
    sock.connect(server_address)

    try:
        # Send Data
        img = 'ups.png'
        imgfile = open(img, 'rb')
        imgbytes = imgfile.read()
        imgbase64 = base64.b64encode(imgbytes)
        sock.sendall(imgbase64)
        imgfile.close()
        print(f"sending {img} with size", len(imgbytes) // 1024, "kb")

        # Look for the response
        amount_received = 0
        proses = open('base64_' + str(i) + '.png', 'wb')
        amount_expected = len(imgbase64)
        while amount_received < (amount_expected + 12):
            data = sock.recv(16)
            proses.write(data)
            amount_received += len(data)

        proses.close()

        coded = open('base64_' + str(i) + '.png', 'rb')
        dedoded = base64.b64decode(coded.read())
        response = open("response_" + str(i) + ".png", 'wb')
        response.write(dedoded)
        response.close()
        coded.close()

    finally:
        print("closing")
        os.remove('base64_' + str(i) + '.png')
        sock.close()

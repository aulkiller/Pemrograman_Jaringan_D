import sys
import socket
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
        # Send data
        img = "ups.png"
        imgfile = open(img, 'rb')
        imgbase = imgfile.read()
        print(f"sending {img} with size", len(imgbase) // 1024, "kb")
        sock.sendall(imgbase)
        # Look for the response
        amount_received = 0
        amount_expected = len(imgbase)
        img_response = "image_response_port" + str(i) + ".png"
        with open(img_response, 'wb') as response:
            while amount_received < (amount_expected + 12):
                data = sock.recv(16)
                amount_received += len(data)
                if not data:
                    break
                response.write(data)
    finally:
        print("closing")
        print("respons balik berupa foto", img_response, "dapat dibuka")
        sock.close()

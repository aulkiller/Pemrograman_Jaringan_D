import sys
import socket

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
        messagesize = 2097152
        message = ''
        for x in range(messagesize // 16):
            message += 'INI ADALAH DATA!'
        print(f"sending INI ADALAH DATA! sebanyak ", messagesize // 16, "kali")
        sock.sendall(message.encode())
        # Look for the response
        amount_received = 0
        amount_expected = len(message)
        print(len(message))
        msgcount = 0;
        while amount_received < (amount_expected + 12):
            data = sock.recv(16)
            amount_received += len(data)
            msgcount += 1
            print(f"{data}")
    finally:
        print("closing")
        print("Jumlah", {data}, "yang diterima ada", msgcount, "kali")
        sock.close()

#!python
"""
convert int to/from bytes array:
>>> num = 42
>>> big = num.to_bytes(4)
>>> little = num.to_bytes(4, byteorder="little")  # default byteorder is "big"
>>> [x for x in big]
[0, 0, 0, 62]
>>> [x for x in little]
[62, 0, 0, 0]
"""
import json
import socket
import struct
import sys
import time

HOST, PORT, PORT_JSON = "localhost", 41004, 41003
PORT = PORT_JSON

def main():
    print("emit cluster event")

    event = {
        "Name": "quit",
        "Type": "command",
        "Category": "",
        "Parameters":{}
    }
    event_string = json.dumps(event)
    event_string = '{"Name":"quit","Type":"command","Category":"","Parameters":{}}'

    msg = bytes(event_string, "utf-8")
    print("bytes '{}'".format(msg))
    msg = struct.pack("I", len(msg)) + msg
    print("struct '{}'".format(msg))

    # Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.send(msg)

        # Receive data from the server and shut down
        # received = sock.recv(1024)

        print("done")
    except ConnectionRefusedError:
        print("refused")
    finally:
        sock.close()


if __name__ == "__main__":
    while True:
        main()
        time.sleep(1)

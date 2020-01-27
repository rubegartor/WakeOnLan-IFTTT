import struct
import socket


def generatePacket(mac):
    data = b'FFFFFFFFFFFF' + (mac * 16).encode()
    send_data = b''

    # Split up the hex values in pack
    for i in range(0, len(data), 2):
        send_data += struct.pack(b'B', int(data[i: i + 2], 16))
    return send_data


def sendWOL(mac, ip='255.255.255.255', port=9):
    mac = mac.replace(':', '')
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
    sock.connect((ip, port))
    sock.send(generatePacket(mac))
    sock.close()

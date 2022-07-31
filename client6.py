import socket
import can
from time import sleep
import sys

HOST = sys.argv[1]
PORT = 7000
server_addr = (HOST, PORT)

s = socket.socket(socket.AF_INET6, socket.SOCK_DGRAM)
bus = can.Bus(channel='vcan0', interface='socketcan')

while True:
    message = bus.recv()
    d=message.data
    data=[]
    while len(d) != 0:
        data.append(d.pop())
    msg = f'{message.arbitration_id}:{message.dlc}:{data[::-1]}'
    print('sendto ' + str(server_addr) + ': ' + msg)
    
    s.sendto(msg.encode(), server_addr)
    # sleep(1)

    # indata, addr = s.recvfrom(1024)
    # print('recvfrom ' + str(addr) + ': ' + indata.decode())

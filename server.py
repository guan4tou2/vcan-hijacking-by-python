import socket
import can

HOST = '0.0.0.0'
PORT = 7000

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((HOST, PORT))
bus = can.Bus(channel='vcan0', interface='socketcan')

print('server start at: %s:%s' % (HOST, PORT))
print('wait for connection...')
while True:
    indata, addr = s.recvfrom(1024)
    data = indata.decode().split(":")
    

    msg = can.Message(arbitration_id=(
        int(data[0])), data=eval(data[2]), is_extended_id=False)

    print('recvfrom ' + str(addr) + ': ' + indata.decode())

    bus.send(msg)

    # outdata = 'echo ' + indata.decode()
    # s.sendto(outdata.encode(), addr)

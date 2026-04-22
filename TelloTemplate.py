# Started from Tello Template
# This Python app is in the Public domain
# Some parts from Tello3.py

import threading, socket, sys, time, subprocess


# GLOBAL VARIABLES DECLARED HERE....
host = ''
port = 9000
locaddr = (host,port)
tello_address = ('192.168.10.1', 8889) # Get the Tello drone's address



# Creates a UDP socketd
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(locaddr)


def recv():
    count = 0
    while True:
        try:
            data, server = sock.recvfrom(1518)
            print(data.decode(encoding="utf-8"))
        except Exception:
            print ('\n****Keep Eye on Drone****\n')
            break


def sendmsg(msg, sleep = 6):
    print("Sending: " + msg)
    msg = msg.encode(encoding="utf-8")
    sock.sendto(msg, tello_address)
    time.sleep(sleep)

# recvThread create
recvThread = threading.Thread(target=recv)
recvThread.start()


# CREATE FUNCTIONS HERE....


print("\nCyle & William")
print("Program Name:Hoop Competition ")
print("Date: 4.20.2026 ")
print("\n****CHECK YOUR TELLO WIFI ADDRESS****")
print("\n****CHECK SURROUNDING AREA BEFORE FLIGHT****")
ready = input('\nAre you ready to take flight: ')


try:
    if ready.lower() == 'yes':
        print("\nStarting Drone!\n")

        sendmsg('command', 0)
        sendmsg('battery?')
        sendmsg('takeoff',8)

        # Commit Message: First Hoop - Stable
        # Don't forget to take video of this portion of the competition.
        # Make sure I put video into our Repository
        # Commit Message: First Hoop Video in Repository
        sendmsg('go 195 30 20 100',8)

    




        # Commit Message: Second Hoop - Stable
        # Don't forget to take video of this portion of the competition.
        # Make sure I put video into our Repository
        # Commit Message: Second Hoop Video in Repository  
        sendmsg('go 220 15 35 100',8)

        






        # Commit Message: Third Hoop - Stable
        # Don't forget to take video of this portion of the competition.
        # Make sure I put video into our Repository
        # Commit Message: Third Hoop Video in Repository 






        # Commit Message: Fourth Hoop - Stable
        # Don't forget to take video of this portion of the competition.
        # Make sure I put video into our Repository
        # Commit Message: Fourth Hoop Video in Repository






        # Commit Message: All Hoops - Stable
        # Don't forget to take video of this portion of the competition.
        # Make sure I put video into our Repository
        # Commit Message: All Hoops Video in Repository

        sendmsg('land')
        sendmsg('battery?')
        print('\nGreat Flight!!!')

    else:
        print('\nMake sure you check WIFI, surroundings, co-pilot is ready, re-run program\n')
except KeyboardInterrupt:
    sendmsg('emergency')

breakr = True
sock.close()

import socket
import select
import sys
import geocoder
import requests
import json
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) != 3:
    print("Correct usage: script, IP address, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address, Port))
 
while True:
    sockets_list = [sys.stdin, server]
    read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
   # print(read_sockets)
 
    for socks in read_sockets:
 
        if socks == server:
            message = socks.recv(2048)
            print(message.decode())
        else:
            message = str(sys.stdin.readline())
            if message=="Report Accident\n" or message=="REPORT ACCIDENT\n" or message=="report accident\n" or message=="Report Accident\n":
                send_url = 'http://freegeoip.net/json'
                r = requests.get(send_url)
                j = json.loads(r.text)
                lat = j['latitude']
                lon = j['longitude']
                gloc = geocoder.google([lat, lon], method='reverse')
                accident_message="Accident reported at <" +"lat = " + str(lat) +">, <lon = " +str(lon)+">\n" +gloc.city+", "+gloc.state+", "+gloc.country+" \n"
                server.send(accident_message.encode())
                sys.stdout.write("<You>")
                sys.stdout.write(accident_message)
                sys.stdout.flush()
            else:
                server.send(message.encode())
                sys.stdout.write("<You>")
                sys.stdout.write(message)
                sys.stdout.flush()
 
server.close()

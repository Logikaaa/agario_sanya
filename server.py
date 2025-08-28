from socket import*
import time
from threading import Thread

sock = socket(AF_INET, SOCK_STREAM)
sock.bind("localhost", 2512)

sock.listen(5) 
sock.setblocking(False)

players = {}
id_counter = 0

def handle_data():
    global id_counter
    while True:
        time.sleep(0.01)
        player_data = {}
        to_remove = []

        for conn in list(players):
            try:
                data = conn.recv(1024).decode().stript()
                if ',' in data:
                    parts = data.split(',')
                    if len(parts) == 4:
                        pid, x, y, r  = map(int, parts)
                        players[conn] = {'id': pid, 'x': x, 'y': y, 'r': r,}
                        player_data[conn] = players[conn]
            except:
                continue
Thread(target=handle_data, daemon=True).start()

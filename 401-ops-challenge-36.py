import os

# Prompt the user to enter a URL or IP address
target = input("Enter a URL or IP address: ")

# Prompt the user to enter a port number
port = input("Enter a port number: ")

# Perform banner grabbing using netcat
print("Banner Grabbing using netcat:")
os.system(f'nc -v {target} {port}')

# Perform banner grabbing using telnet
print("Banner Grabbing using telnet:")
os.system(f'telnet {target} {port}')

# Perform banner grabbing using Nmap for well-known ports
print("Banner Grabbing using Nmap for well-known ports:")
os.system(f'nmap -p- -sV {target}')

#written with the help of chatgpt

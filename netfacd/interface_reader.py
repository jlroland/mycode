#!/usr/bin/env python3

import netifaces

print(netifaces.interfaces())

'''for i in netifaces.interfaces():
    print('\n****** details of interface - ' + i + ' ******')
    try:
        print('MAC: ', end='') # This print statement will always print MAC without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) # Prints the MAC address
        print('IP: ', end='')  # This print statement will always print IP without an end of line
        print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) # Prints the IP address
    except:          # This is a new line
        print('Could not collect adapter information') # Print an error message
'''
def find_ip(device):
    if device in netifaces.interfaces():
        print(f"IP Address: {(netifaces.ifaddresses(device)[netifaces.AF_INET])[0]['addr']}")
    else:
        print(f"Could not find information for {device}")

def find_mac(device):
    if device in netifaces.interfaces():
        print(f"MAC Address: {(netifaces.ifaddresses(device)[netifaces.AF_LINK])[0]['addr']}")
    else:
        print(f"Could not find information for {device}")

req_if = input("Enter interface to retrieve information:  ")
info_type = input("Would you like ip or mac?  ")

if info_type.lower() == 'ip':
    find_ip(req_if)
elif info_type.lower() == 'mac':
    find_mac(req_if)
else:
    print("Not a valid option")


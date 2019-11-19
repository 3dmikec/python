'''
Display some ASN info for an IP address or translates a host name to IPv4 address format
'''

from ipwhois import IPWhois
import socket

def host_check(addr):
    print('Found address: ' + socket.gethostbyname(addr))
    
def who_is(addr):
    ip = IPWhois(addr)
    results = ip.lookup_rdap()
    print('ASN Information: \n')
    for k,v in results.items():
        if k.startswith('asn'):
            print(f'{k}: {v}')

while True:

    addr = input("Enter a host name or IP address: ")
    
    try:
        print(f'Trying IP address lookup for {addr}...')
        who_is(addr)
        break
    except ValueError:
        print('Input does not appear to be an IPv4 or IPv6 address')
        pass
    try:
        print(f'Trying DNS lookup for {addr}...')
        host_check(addr)
        break
    except socket.gaierror:
        print('Failed to get address. Please try another input')
        continue
'''

Write a function that takes an IP address and returns the domain name using PTR DNS records.

'''

import socket

def get_domain(ip_address):
    return socket.gethostbyaddr(ip_address)[0]
	



if __name__ == "__main__":
    print(get_domain("8.8.4.4"))
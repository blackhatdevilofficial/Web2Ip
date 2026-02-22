#!/usr/bin/python3
"""
Website IP Address Finder and Port Scanner
"""

import socket
import requests
import argparse

def get_ip_address(domain):
    try:
        ip = socket.gethostbyname(domain)
        print(f"IP address for {domain}: {ip}")
    except socket.gaierror as e:
        print(f"Error resolving domain: {e}")

def scan_port(ip, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Timeout in seconds
        result = sock.connect_ex((ip, port))
        
        if result == 0:
            print(f"Port {port} is open")
        else:
            print(f"Port {port} is closed")
            
    except Exception as e:
        print(f"Error scanning port: {e}")
    
def main():
    parser = argparse.ArgumentParser(description="Website IP Address Finder and Port Scanner")
    parser.add_argument("domain", help="Target domain name (e.g., example.com)")
    parser.add_argument("--ip-only", action="store_true", help="Only get IP address")
    parser.add_argument("--port", type=int, choices=range(1, 65536), 
                       help="Specific port to scan (default: 80 for HTTP)")

    args = parser.parse_args()

    # Get the target domain
    try:
        if not args.ip_only:
            ip_address = socket.gethostbyname(args.domain)
            print(f"Domain {args.domain} resolved to IP address: {ip_address}")
            
        # Scan specific port if requested
        if args.port:
            scan_port(ip_address, args.port)
    
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

import re

ips = []     # creates an empty list called ips

with open('auth.log', 'r') as f:
    for line in f:
        # Search for IP addresses in each line
        found_ips = re.findall(r'\d+\.\d+\.\d+\.\d+', line)
        ips.extend(found_ips)  # Add found IPs to the list

# Print all collected IP addresses
for ip in ips:
    print(ip)
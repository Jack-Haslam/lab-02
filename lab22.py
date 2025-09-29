# lab2-2_starter.py

LOGFILE = "sample_auth_small.log"  # change filename if needed
"""
def simple_parser(line):#This function locates the port no.
    
    looks for the substring ' port ' and returns the following port number.
    Returns None if no matching substring found.
    
    if " port " in line:
        parts = line.split() # splits the line into tokens, seperates by spaces by default
        try:
            anchor = parts.index("port")    # Find the position of the token "port", our anchor
            port = parts[anchor+1]          # the port value will be next token, anchor+1
            return port.strip()             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None

    return None
    """

def simple_ips(line):#This function locates the ips from "sample_auth_small.log" 
                         
    if " from " in line:
        ips = line.split()                 # splits the line into tokens, seperates by spaces by default
        try:
            anchor = ips.index("from")     # Find the position of the token "from", our anchor
            ips = ips[anchor+1]            # the port value will be next token, anchor+1
            return ips.strip()             # strip any trailing punctuation

        except (ValueError, IndexError):
            return None
    return None

## This is the main block that will run first. 
## It will call any functions from above that we might need.
if __name__ == "__main__":

    uniqueIps = {}
    noOfLines = 0
    all_ips=[]
    sorted_uniquie_ips = []
    with open(LOGFILE, "r") as f:

        for line in f:
        
            all_ips.append(simple_ips(line.strip()))
            noOfLines = noOfLines+1

    print ("Lines read: "+str(noOfLines))
    uniqueIps = set(all_ips)                        #adds ips to set
    for i in uniqueIps:
        if i:                                       #uses an if to say if ip, then sort. Removes null entries.
            sorted_uniquie_ips.append(i)            #removes ips from a set to a list to remove duplicates.

    sorted_uniquie_ips=sorted(sorted_uniquie_ips)   #assignes removed, sorted ips to a varaible
    print("Unique IP's: "+str(len(set(all_ips))))   #prints the length of the set of ips. Sets auto remove duplicates.
    print ("First 10 IP's: "+str(sorted_uniquie_ips[:10]))#[:10] only prints the first 10 ips in list.

    from collections import defaultdict

    counts = defaultdict(int)           # Create a dictionary to keep track of IPs

    with open("sample_auth_small.log") as f:
        for line in f:
            if "Failed password" in line or "Invalid user" in line:
                # extract ip
                ip = ip_parse(line)
                if ip:
                    counts[ip] += 1
    print(counts)
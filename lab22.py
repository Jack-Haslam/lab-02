# lab2-2_starter.py

LOGFILE = "sample_auth_small.log"  # change filename if needed
""""
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

    uniqueIps = ()
    noOfLines = 0

    with open(LOGFILE, "r") as f:

        for line in f:
        
            print (simple_ips(line.strip()))
            noOfUniqueIps = uniqueIps(simple_ips)
            noOfLines = noOfLines+1

    print ("Lines read: "+str(noOfLines))
    print(noOfUniqueIps)
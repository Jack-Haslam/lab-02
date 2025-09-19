import re

pattern = r"\d+\.\d+\.\d+\.\d+"
text = "Failed login from 192.168.0.1 at 10:30"
text = "Successful login from 192.168.0.2 at 10:35"#prints last occ of ip

print(re.findall(pattern, text))
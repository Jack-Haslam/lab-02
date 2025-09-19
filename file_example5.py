import re

pattern = r"[\d]+"#search for numbers
text = "Order 123 was placed on 2023-05-01."

print(re.findall(pattern, text))

pattern = r"[A-Za-z]+"#search for letters
text = "Order 123 was placed on 2023-05-01."

print(re.findall(pattern, text))
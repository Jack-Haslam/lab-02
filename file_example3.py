#with open('output.txt', 'w') as f:
#    f.write("This is a new file.\n") /n = newline
#    f.write("It has two lines.\n")

with open('sample.txt', 'r') as src, open('copy.txt', 'w') as dest:
    for line in src:
        dest.write(line)

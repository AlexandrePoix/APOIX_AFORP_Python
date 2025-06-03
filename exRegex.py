import re


ip = input()
x = re.search("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip)

if (x):
    print("yes")
else: print("no")
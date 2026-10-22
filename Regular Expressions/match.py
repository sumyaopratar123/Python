import re

s = "Dypcet Kolhapur"

match = re.match('Dypcet', s)

if match:
    print("Pattern matched")
else:
    print("Pattern not matched")
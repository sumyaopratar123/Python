import re

string = "cat dog cat"

result = re.subn('cat', 'rat', string)

print(result)
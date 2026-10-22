import re

string = "price$100.00"

result = re.escape(string)

print(result)
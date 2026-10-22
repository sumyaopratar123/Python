import re

string = """Hello my Number is 123456789 and
my friend's number is 987654321"""

regex = r'\d+'

match = re.findall(regex, string)

print(match)
import re

string = "I like Java. Java is easy."

result = re.sub('Java', 'Python', string)

print(result)
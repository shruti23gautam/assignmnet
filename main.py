import re
s= input()
pattern = "\d+"
ans = re.findall(pattern,s)
print(ans)
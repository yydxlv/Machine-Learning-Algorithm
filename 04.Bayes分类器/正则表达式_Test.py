__author__ = 'xilin'
import re
mysent="This is the best book on Python or M.L. I have ever laid eyes upon ."
print(mysent.split())
regex=re.compile('\\W*')
listofTokens=regex.split(mysent)
print(listofTokens)
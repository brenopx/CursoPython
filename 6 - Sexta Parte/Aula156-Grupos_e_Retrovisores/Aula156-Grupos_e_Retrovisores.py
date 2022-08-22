# Meta caracteres: ^ $ ()
# [@#abca-zA-Z0-9]
# [a-z]+
# (abc|def)
# (Luiz|Otávio)
# (...)
# ()  \1
# ()()  \1 \2
# (())()  \1 \2 \3

import re
from pprint import pprint


texto = '''
<p> Frase 1</p> <p> Qualquer 2</p> <p> Qualquer frase 3</p> <div> 1 </div>
'''

# print(re.findall(r'<([pdiv]{1,3})>.+?<\/\1>', texto))
# print(re.findall(r'(<([divp]{1,3})>.+?<\/\2>)', texto))

# tags = re.findall(r'(<([divp]{1,3})>(.+?)<\/\2>)', texto)
tags = re.findall(r'(<([divp]{1,3})>(?:.+?)<\/\2>)', texto)
pprint(tags)

# for tag in tags:
#     # print(tag)
#     um, dois, tres = tag
#     print(tres)

cpf = 'a 147.852.963-12 a'
# print(re.findall(r'[0-9]{3}\.[0-9]{3}\.[0-9]{3}-[0-9]{2}', cpf))
# print(re.findall(r'((?:[0-9]{3}\.){2}[0-9]{3}-[0-9]{2})', cpf))

# tags = re.findall(r'<(?P<tag>[divp]{1,3})>(.+?)<\/(?P=tag)>', texto)
# tags = re.findall(r'(<([divp]{1,3})>(.+?)<\/\2>)', texto)
# pprint(tags)

print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 \3 \4', texto))
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 "\3" \4', texto))
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1 MAIS \3 COISAS \4', texto))
print(re.sub(r'(<(.+?)>)(.+?)(<\/\2>)', r'\1  \4', texto))

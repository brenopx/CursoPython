# Meta caracteres: ^ $ ()
# * 0 ou n
# + 1 ou n
# ? 0 ou 1
import re

texto = '''
<p>Frase 1</p> <p> Qualquer 2</p> <p> Qualquer frase 3</p> <div></div>
'''
print(re.findall(r'<[pdiv]{1,3}>.*<\/[pdiv]{1,3}>', texto))  # Greddy
print(re.findall(r'<[pdiv]{1,3}>.*?<\/[pdiv]{1,3}>', texto))  # Non-Greddy
print(re.findall(r'<[pdiv]{1,3}>.+?<\/[pdiv]{1,3}>', texto))

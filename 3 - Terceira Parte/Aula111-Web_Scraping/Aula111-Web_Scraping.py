"""
Aula 111 - Web Scraping com Python
"""
from bs4 import BeautifulSoup
import requests

url = 'https://pt.stackoverflow.com/questions/tagged/python'
response = requests.get(url)
# print(response.text)
html = BeautifulSoup(response.text, 'html.parser')
# print(html)

for pergunta in html.select('.question-summary'):
    titulo = pergunta.select_one('.question-hyperlink')
    data = pergunta.select_one('.relativetime')
    votos = pergunta.select_one('.vote-count-post')

    print(data.text, titulo.text, votos.text, sep='\t')

#imports 

import requests
from bs4 import BeautifulSoup

pagina = requests.get('https://www.google.com/finance/quote/EUR-BRL?sa=X&ved=2ahUKEwjfrYTgtaSFAxWcpZUCHaBgC6IQmY0JegQIBhAv')
sopa = BeautifulSoup(pagina.text, 'html.parser')

container = sopa.findAll('div', {'class': "YMlKec fxKbKc"})



euro = container[0].text.strip()

print(euro)


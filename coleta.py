#imports 

import requests
from bs4 import BeautifulSoup

#coletando dados do euro

pagina = requests.get('https://www.google.com/finance/quote/EUR-BRL?sa=X&ved=2ahUKEwjfrYTgtaSFAxWcpZUCHaBgC6IQmY0JegQIBhAv')
sopa = BeautifulSoup(pagina.text, 'html.parser')
container = sopa.findAll('div', {'class': "YMlKec fxKbKc"})

valor_euro = container[0].text.strip()
#texto_euro = print('{:.2f}'.format(float(valor_euro)))


#coletando dados do dolar

pagina2 = requests.get('https://www.google.com/finance/quote/USD-BRL?sa=X&ved=2ahUKEwibndLr-qSFAxWiqJUCHSEjCT8QmY0JegQIBxAv')
sopa2 = BeautifulSoup(pagina2.text, 'html.parser')
container2 = sopa2.findAll('div', {'class': "YMlKec fxKbKc"})   

valor_dolar = container2[0].text.strip()
#texto_dolar = print('{:.2f}'.format(float(valor_dolar)))

texto = ("💲 Cotação Dolar e Euro: \n"+ \
        "💵 O valor do Dolar é: US${:.2f}".format(float(valor_dolar)) + "\n" + \
        "💶 O valor do Euro é: €{:.2f}".format(float(valor_euro)) + "\n\n")

print(texto)
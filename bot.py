#imports 

import requests
from bs4 import BeautifulSoup
import tweepy
import time
from datetime import datetime


#coletando dados do euro

pagina = requests.get('https://www.google.com/finance/quote/EUR-BRL?sa=X&ved=2ahUKEwjfrYTgtaSFAxWcpZUCHaBgC6IQmY0JegQIBhAv')
sopa = BeautifulSoup(pagina.text, 'html.parser')
container = sopa.findAll('div', {'class': "YMlKec fxKbKc"})

valor_euro = container[0].text.strip()

#coletando dados do dolar

pagina2 = requests.get('https://www.google.com/finance/quote/USD-BRL?sa=X&ved=2ahUKEwibndLr-qSFAxWiqJUCHSEjCT8QmY0JegQIBxAv')
sopa2 = BeautifulSoup(pagina2.text, 'html.parser')
container2 = sopa2.findAll('div', {'class': "YMlKec fxKbKc"}) 

valor_dolar = container2[0].text.strip()


texto = ("💲 Cotação Dolar e Euro: \n"+ \
        "💵 O valor do Dólar é: US${:.2f}".format(float(valor_dolar)) + "\n" + \
        "💶 O valor do Euro é: €{:.2f}".format(float(valor_euro)) + "\n\n")


#Criando o bot

consumer_key = 'sua_consumer_key'
consumer_secret = 'seu_consumer_secret'
access_token = 'seu_acess_token'
access_token_secret = 'seu_token_secret'

# Autenticação no Twitter
auth = tweepy.OAuth1UserHandler(consumer_key, consumer_secret, access_token, access_token_secret)
api = tweepy.API(auth)

#automatizando o bot

def enviar_tweet():
    texto_tweet = texto
    api.update_status(texto_tweet)
    print("Tweet enviado com sucesso!")

# Loop para enviar tweet a cada hora
while True:
    enviar_tweet()
    # Intervalo de 1 hora
    time.sleep(3600)
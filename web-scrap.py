import requests 
from bs4 import BeautifulSoup
from twilio.rest import Client

# Colocar url do site em que o protudo desejado esta
url = 'https://www.levi.com.br/calca-jeans-levis-568-stay-loose-cargo-lavagem-clara-000lp0001/p'

# Sistema operacional, aplicação, fornecedor e/ou versão do agente que está fazendo a requisição
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'}

# Configurações padrao das bibliotecas BealtifulSoup e requests
site = requests.get(url, headers=headers)
soup = BeautifulSoup(site.content, 'html.parser')

# Variaveis para nome de produto e preço
title = soup.find('h1', {'class':'vtex-store-components-3-x-productNameContainer mv0 t-heading-4'}).get_text()
price = soup.find('span', {'class': 'vtex-product-price-1-x-currencyContainer'}).get_text()

# Transformando a variavel de preço de string para float
num_price = price[3:9]
num_price = num_price.replace(',', '.')
num_price = float(num_price)


# Função para enviar o SMS (necessario uma conta no Twilio para ter o token, SID e o numero que vai te mandar o SMS)
def enviar_sms(numero, mensagem):
    account_sid = 'SID' # Alterar conforme o seu SID
    auth_token = 'TOKEN' # Alterar conforme o seu Token
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=mensagem,
        from_='numero_de_telefone_fornecido_pelo_Twilio', # +19999999999
        to=numero
    )

    print(f"SMS enviado: SID {message.sid}")
    
# Variaveis para inserir seu numero e a mensagem desejada  
numero = 'seu_numero_de_telefone' # Ex: +1155999999999
mensagem = 'Seu item está em promoção!!'

if num_price <= 500: # Editar conforme preço desejado   
    enviar_sms(numero, mensagem)
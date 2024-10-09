# Monitor de Preço de Produto com Notificação via SMS

Este script Python monitora o preço de um produto específico em um site de e-commerce e envia uma notificação via SMS utilizando o serviço **Twilio** caso o preço do produto esteja abaixo de um determinado valor. O exemplo atual verifica o preço de uma calça jeans no site da Levi's.

## Requisitos

Antes de utilizar o script, você precisa instalar as seguintes dependências:

- Python 3.x
- Bibliotecas externas:
  - `requests`
  - `beautifulsoup4`
  - `twilio`

### Instalação das Dependências

Para instalar as dependências, execute o seguinte comando no terminal:

```bash
pip install requests

pip install bs4

pip install twilio
```
### Configuração 

1. URL do Produto
Você deve modificar o valor da variável `url` com o link do produto que deseja monitorar. No exemplo atual, o link é o de uma calça jeans Levi's:

```bash
url = 'https://www.levi.com.br/calca-jeans-levis-568-stay-loose-cargo-lavagem-clara-000lp0001/p'
```

#### 2. Twilio Account SID, Auth Token e Número de Envio
Você precisará de uma conta no Twilio para enviar SMS. Após criar a conta, obtenha o Account SID, Auth Token e número de telefone Twilio.

Substitua os valores na função `enviar_sms` pelos dados da sua conta:

```bash
account_sid = 'seu_account_sid_aqui'
auth_token = 'seu_auth_token_aqui'
```


O número Twilio deve ser inserido na variável `from_`:

```bash
from_='+seu_numero_twilio'
```

#### 3. Número para Enviar a Notificação
Na variável `numero`, insira o número de telefone que deverá receber o SMS:

```bash
numero = '+5511999999999'  # Exemplo
```

#### 4. Mensagem Personalizada
Modifique a mensagem da variável `mensagem` conforme desejar. No exemplo atual, a mensagem avisa que o item está em promoção:

```bash
mensagem = 'Seu item está em promoção!!'
```

#### 5. Definir o Limite de Preço
No exemplo atual, a notificação via SMS será enviada se o preço do produto for igual ou inferior a R$500. Se quiser alterar esse limite, modifique o valor da condição:

```bash
if num_price <= 500:
```

## Como usar

Após configurar as variáveis, execute o script.
O código irá buscar o nome e o preço do produto na página especificada.
Se o preço for igual ou menor que o limite definido, o script enviará uma mensagem de SMS para o número especificado.

### Exemplo de Saída
Se o preço do produto estiver abaixo do limite, você verá algo assim no terminal:
```bash
SMS enviado: SID SMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

## Considerações Finais

O Twilio possui uma conta gratuita com limitações, como o uso de um número pré-configurado para enviar SMS.
A função de scraping depende da estrutura HTML do site. Certifique-se de que os seletores (`class` ou `id`) usados no BeautifulSoup estejam corretos. Se a estrutura da página mudar, será necessário atualizar esses seletores.
from bs4 import BeautifulSoup
import requests

# doc da lib - https://www.crummy.com/software/BeautifulSoup/bs4/doc/

# substituir a url com a que for usar
html = requests.get('http://urlaqui ...')

# isso analisa a pagina, "lxml" é só o parse para ler o html (pode ser alterado)
soup = BeautifulSoup(html.text, "lxml")

# isso pega os links e armazena na variavel links
links = soup.find_all('a')

for link in links:
    # printa os links
    print(link)
    

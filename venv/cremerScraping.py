import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

def scraping_precos (url):

    page = requests.get(url).content
    soup = BeautifulSoup(page, 'html.parser')

    c=1
    nome_e_preco = dict()
    
    produtos = soup.find_all('span', class_='base')

    for produto in produtos:
        nome_e_preco['prod'] = (produto.get_text())

    precos = soup.find_all('span', class_="price")

    for preco in precos:
        if len(precos) == 1:
            nome_e_preco['valor'] = (preco.get_text())
        if len(precos) > 1 and c == 2:
            nome_e_preco['valor'] = (preco.get_text())
        c += 1
    
    return nome_e_preco

lista_de_urls_dos_produtos=[
    'https://www.dentalcremer.com.br/compressa-de-gaze-ultracotton-9-fios-n-o-esteril-ultracotton-100545.html', 
    'https://www.dentalcremer.com.br/sugador-descartavel-transparente-allprime-127720.html', 
    'https://www.dentalcremer.com.br/tira-de-lixa-de-poliester-microdont-513202.html', 
    'https://www.dentalcremer.com.br/anestesico-lidostesim-3-1-50-000-dla.html',
    ]
lista_de_urls_dos_produtos.sort()

dados_para_excel_cremer = []
for url in lista_de_urls_dos_produtos:
    dados_para_excel_cremer.append(scraping_precos(url))

print(dados_para_excel_cremer)


precos_excel = Workbook()
planilha1 = precos_excel.worksheets[0]
planilha1.title='Dental Cremer'

print(precos_excel.sheetnames)
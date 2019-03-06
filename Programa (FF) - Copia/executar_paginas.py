from selenium import webdriver
from bs4 import BeautifulSoup as bs
from pegar_registros import *

class Page:

    # Função construtora do programa, que ira armazenar variaveis self, que irão orientar o selenium na interação com o site.
    def __init__(self, driver):
        self.driver = driver
        self.url = 'http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCEP.cfm'
        self.search_bar = 'f1col'
        self.btn_search = 'btn2'
        self.table = 'tmptabela'

    # Inicia a navegação até o URL requisitado
    def navegar(self):
        self.driver.get(self.url)
        Page.estado(self)
        
    #Menu de opções, onde o usuario ira decidir a UF a ser pesquisada.
    def estado(self):
        escolha=0
        while escolha !=1:
            print(20 * '-=')
            print('Escolha uma opção: \n[0] Para pesquisar por uma UF\n[1] Para encerrar o programa')
            escolha = int(input('Escolha [0] ou [1]: '))
            if escolha == 0:
                uf = input(str('Insira a sigla da UF (Unidade da Federação), por exemplo: SC,SP,RS... : ')).upper()
                Page.pesquisar(self, uf)
                return uf
            elif escolha == 1:
                print(20 * '-=')
                print('FINALIZANDO PROGRAMA!')
                gc.quit()
            else:
                print('OPÇÃO INVÁLIDA! DIGITE UM NÚMERO VALIDO POR FAVOR [0] ou [1]')

    # Função responsável por selecionar pela UF requisitada e clicar e buscar.
    def pesquisar(self, word='None'):
        self.driver.find_element_by_class_name(
            self.search_bar).send_keys(word)
        self.driver.find_element_by_class_name(
            self.btn_search).click()
        Page.pegar_tabelas(self, t=1)
    
    # Função responsável por clicar na opção "Nova Consulta"
    @staticmethod
    def inicia_nova_consulta(driver):
        print('Registros achados coletados, retornando para fazer uma nova consulta...')
        driver.find_element_by_link_text("[ Nova Consulta ]").click()
        g.navegar()

     # Função responsável por pegar a tabela em HTML onde os registros estão.   
    @staticmethod
    def pegar_tabelas(self, t=1):
        tabelas = (self.driver.find_elements_by_class_name(
            self.table))
        tabela = tabelas[t]
        pagina_HTML()
    
    #Função responsável por tentar clicar na opção "Próxima" quando possivél, quando não for possivél, iniciará uma nova consulta.
    @staticmethod
    def mudar_pagina(driver):
        try:
            driver.find_element_by_link_text("[ Próxima ]").click()
        except:
            Page.inicia_nova_consulta(gc)

# Função recebe a tabela onde estão os registros, fica responsável por pegar todo documento o HTML da pagina, e "dissecar" ele até as chegar nas tags <td>, onde é chamado a função limpa_registros.
def pagina_HTML(qual_tabela=1):
    html = gc.page_source
    correio_pagina = bs(html, 'html.parser')
    tabela = correio_pagina.find_all('table')
    tbody = tabela[qual_tabela].find('tbody')
    td = tbody.find_all('td')
    limpa_registros(td)
    return td

# Função recebe as tags <td> cruas ,fica responsável por retirar apenas o texto das tags <td>, armazenando-as em uma lista que é mandada para a função gerando_arquivo_json(),e depois continua procurando por registros até acabar com a função continua_procurando().
def limpa_registros(td):
    cep_inicial = 1
    cidade_inicial = 0
    lista_registros = []
    for cada_registro in range(0, len(td), 2):
        lista_registros.append(td[cidade_inicial].text)
        lista_registros.append(td[cep_inicial].text)
        cidade_inicial += 2
        cep_inicial += 2
    gerando_arquivo_json(lista_registros)
    continua_procurando(lista_registros)
    return lista_registros

# Função responsável por ficar "infinitamente" trocando a página e armazenando os registros que encontrar.
def continua_procurando():
    while True:
        Page.mudar_pagina(gc)
        pagina_HTML(0)
        break


gc = webdriver.Chrome(executable_path='./chromedriver')
g = Page(gc)
g.navegar()

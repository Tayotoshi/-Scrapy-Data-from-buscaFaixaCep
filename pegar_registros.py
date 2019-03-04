
#Cria um arquivo.txt e armazena a lista de registros (lista_registros)
def cria_e_salva_arquivo (lista_registros):
    x=0
    arq = open('registros.json', 'a',encoding='utf-8')
    texto = lista_registros
    while x < len(lista_registros):
        arq.write(texto[x])
        x += 1
    arq.close()

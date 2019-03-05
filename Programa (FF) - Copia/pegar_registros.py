import jsonlines

#Armazena os registros em um arquivo JSONL
def gerando_arquivo_json(lista_registros):
    cep_inicial = 1
    cidade_inicial = 0
    for registros in range(0, len(lista_registros),4):
        registros={}
        registros["Registro"]={
            'Localidade':lista_registros[cidade_inicial],
            'Faixa_Cep':lista_registros[cep_inicial]
            }
        s=registros
        with jsonlines.open("registros.jsonl","a") as a:
            a.write(s)
            cidade_inicial += 4
            cep_inicial += 4

# Scrapy_Data_From_buscaFaixaCEP

 O **Scrapy_Data_From_buscafaixaCEP** é um programa desenvolvido em linguagem Python3 por Bernardo Souza de Oliveira, responsavél por extrair dados (Scrappy) da URL **http://www.buscacep.correios.com.br/sistemas/buscacep/buscaFaixaCep.cfm** , retornando um arquivo JSONL com todos os registros coletados.
 
## Pré Requisitos para usar o programa:

- Este programa foi criado para ser executado em máquinas Linux. (Embora tenha como adaptar para Windows)

- Este programa funciona apenas no navegador GoogleChrome.

- Ter o framework selenium instalado.

Comando para a instalação: **pip3 install -U selenium**

- Ter o Beautiful Soup instalado.

Comando para a instalação: **apt-get install python3-bs4** 

- Ter a biblioteca jsonlines instalada.

Comando para a instalação: **pip3 install -U jsonlines**

- Ao baixar o arquivo, verificar se o chromedriver tem permissão para ser executado, se não tiver, utilize o  comando abaixo.

Comando para conceder permissão: **chmod 777 chromedriver**

## Como rodar:

 Execute o programa no seu console, após isso o seu navegador GoogleChrome ira iniciar e você sera redirecionado para o site dos correios na parte de busca faixa de CEP, dando começo ao programa. Após isso o programa ira pedir para que você selecione uma das opções, digitando **[0]** ou **[1]**, onde **[0]** seria a opção para pesquisar por uma UF, e **[1]** para encerrar o programa, selecione a opção **[0]** para pesquisar por uma UF, após isso, o programa ira pedir para você declarar a UF que quer fazer o Scrapy e coletar os registros, digite a UF desejável (apenas abreviaçoes,ex:SC,SP,ES...} e aperte enter, após isso ocorrera a coleta de todos os registros da UF requisitada, e você voltará a parte de opções, repita o processo quantas vezes quiser, e depois apenas digite **[1]** para encerrar o programa.
 
 ## Erro ao encerrar o programa
 
 Se você for encerrar o programa digitando a opção [1], ele ira finalizar mas logo depois acusará um erro, esse erro não influencia em nenhuma parte do programa visto que ele acontece após o encerramento do próprio programa (g.quit), mas achei importante citar ele, poís realmente não achei soluções para resolve-lô.
 

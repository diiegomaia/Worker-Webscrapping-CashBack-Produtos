#from data_base.database import Data_base
""" from resources.cashback.funcoes import raspagem_cupomania as rc
from resources.cashback.funcoes import raspagem_meliuz as me
from resources.produtos_mercado_livre.funcoes import ML_selecionados
from resources.produtos_mercado_livre.funcoes import ML_OMaisbarato """
#from recursos.mercado.funções import sams_club_selecao
from recursos.mercado.funções import ramos_selecao

import time as t



# Funções
print("Iniciando banco de dados")
t.sleep(2)
""" db = Data_base()
db.connect()
db.create_table() """

def msg():
    print('Programa finalizado.')

""" def main_sams_club_selecao():
    print('Iniciando Lista Sams Club')    
    t.sleep(1)
    #Ketchup, Maionese, Arroz, Mussarela
    urls = ['https://www.samsclub.com.br/queijo-mussarela-la-paulina-peca-aprox-4kg-209735000006/p',
            'https://www.samsclub.com.br/ketchup-heinz-1033kg-7896102000122/p',
            'https://www.samsclub.com.br/maionese-caseira-hemmer-pote-500g-7891031412176/p',
            'https://www.samsclub.com.br/file-de-salmao-members-mark-1kg-7891737167301/p',
            'https://www.samsclub.com.br/geleia-de-morango-members-mark-vidro-680g-7891737233754/p',
            'https://www.samsclub.com.br/arroz-parboilizado-tipo-1-prato-fino-5kg-7896290300332/p',
            'https://www.samsclub.com.br/molho-de-tomate-com-manjercao-basilico-cirio-pack-2-unidades-420g-cada-8001440133404/p']

    samsclubs = sams_club_selecao(urls)

    for samsclub in samsclubs:

        fullDataset = (
                samsclub['Data'], samsclub['Produto'], samsclub['Preco']
            )

        db.register_sams_club_selecao(fullDataset) """

def main_ramos_selecao():
    print('Iniciando Lista Ramos')    
    t.sleep(1)

    #Carne, Arroz,etc
    urls = ['https://loja.supermercadosramos.com.br/loja/348/categoria/7046/produto/7025409?origin=searching',
            'https://loja.supermercadosramos.com.br/loja/348/categoria/7043/produto/6851156?origin=categories',
            'https://loja.supermercadosramos.com.br/loja/348/categoria/7046/produto/7025369?origin=searching',
                  
            ]

    ramos  = ramos_selecao(urls)

    for ramo in ramos:

        fullDataset = (
                ramo['Data'], ramo['Produto'], ramo['Preco']
            )

        #db.register_ramos_selecao(fullDataset)




#Controlador
""" main_cashback()
main_ML_selecionados()
main_ML_Omaisbarato() """
#main_sams_club_selecao()
main_ramos_selecao()

msg()


""" Salvar no github
1. git init
2. git add .
3. git commit -m ""
4. git push """
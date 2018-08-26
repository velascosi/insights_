import numpy as np
import pandas as pd

def getSamples():
    score_base = pd.read_csv('sample_data\\sample.csv',delimiter=';')
    return score_base

#Calcula rating mediano atualizado para compras
#Objetivo futuro utilizar scikit learn com modelo de decision tree incrementando informações com crowler do ReclameAqui
def updateRatingComprador(score_base, comprador):
    #filtra comprador selecionado
    score_base = score_base.query('id_empresa_compradora=='+str(comprador))
    
    #calcula rating ponderado
    score_base = score_base.assign(pont_trans_compradora = (score_base['negociacoes_compradora']/score_base['negociacoes_compradora'].max())*score_base['avaliacao_compradora'])
    return score_base

#Calcula rating mediano atualizado para vendas
#Objetivo futuro utilizar scikit learn com modelo de decision tree incrementando informações com crowler do ReclameAqui
def updateRatingVendedor(score_base, vendedor):
    #filtra comprador selecionado
    score_base = score_base.query('id_empresa_vendedora=='+str(vendedor))

    #calcula rating ponderado
    score_base = score_base.assign(pont_trans_vendedora = (score_base['negociacoes_vendedora']/score_base['negociacoes_vendedora'].max())*score_base['avaliacao_vendedora'])
    return score_base

#Lista compradores unicos da base
def getCompradores(score_base):
    return score_base.id_empresa_compradora.unique()

#Lista vendedores unicos da base
def getVendedores(score_base):
    return score_base.id_empresa_vendedora.unique()

#Devolve rating mediano do comprador
def getScoreComprador(score_base, comprador):
    #atualiza calculo de rating do comprador
    updateRatingComprador(score_base, comprador)

    #avalia se o comprador possui mais de 6 interacoes
    if score_base.query('id_empresa_comprador=='+str(comprador)).negociacoes_comprador.max() >= 6:
        #retorna mediana dos valores ponderados e atualizados
        return score_base.query('id_empresa_compradora=='+str(comprador))['pont_trans_compradora'].median()
    else:
        return 0

#Devolve rating mediano do vendedor
def getScoreVendedor(score_base, vendedor):
    #atualiza calculo de rating de vendedor
    updateRatingVendedor(score_base, vendedor)

    #avalia se o vendedor possui mais de 6 interacoes
    if score_base.query('id_empresa_vendedora=='+str(vendedor)).negociacoes_vendedora.max() >= 6:

        #retorna mediana dos valores ponderados e atualizados
        return score_base.query('id_empresa_vendedora=='+str(vendedor))['pont_trans_vendedora'].median()
    else:
        return 0

##### Exemplos de utilizacao

#Exemplo de chamada de lista de vendedores com dados de teste
getVendedores(getSamples())

#Exemplo de chamada de lista de compradores com dados de teste
getCompradores(getSamples())

#Busca de rating de comprador
getScoreComprador(getSamples(),2)

#Busca de rating de vendedor
getScoreVendedor(getSamples(),1)


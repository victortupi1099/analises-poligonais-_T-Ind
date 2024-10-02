#base para arquivos
import pandas as pd 
import geopandas as gpd
import matplotlib.pyplot as plt
df_terras = pd.DataFrame(pd.read_csv('tis_poligonais.csv'))
povos = df_terras["etnia_nome"].unique().tolist()
terra_gerais = df_terras[ 'terrai_nome'].unique().tolist()


# função para exibição de povos catalogados
def exibir(povos):
      print("povos indigenas catalogados: ")
      for i in range(len(povos)):
        print(povos[i])

#  função para exibição de aldeias catalogadas
def exibir_terras(terras_gerais):
      print("povos indigenas catalogados: ")
      for i in range(len(terra_gerais)):
        print(terra_gerais[i])





        
#     função para amostragem de dados seguindo parametro de povos
def povo_escolha(*args):
        ent_usr = input("digite o nome da etnia a ser selecionada: ").strip().capitalize()
        while ent_usr not in povos:
            ent_usr = input("digite o nome da etnia a ser selecionada: ").strip().capitalize()
        print("\n\n")
        completo_simp = input("deseja a exibição completa dos dados ou simplificada ?: ").strip()
        while not(completo_simp == "completa" or completo_simp == "simplificada"):
             completo_simp = input("deseja a exibição completa dos dados ou simplificada ?: ").strip() 
        if completo_simp == "completa":
             print(df_terras.loc[df_terras["etnia_nome"] == ent_usr , :] ) 

        if completo_simp == "simplificada":
             print("os parametros disponiveis são: ")
             print(df_terras.columns)
             parametros = []
             while True:
                      print('digite um novo parametro para ser exibido em sua analise, \n para finalizar os parametros diigite "sair"')    
                      novo_parametro = input("você: ")
                      if novo_parametro != "sair": 
                           parametros.append(novo_parametro)
                      if novo_parametro == "sair": 
                           print(df_terras.loc[df_terras["etnia_nome"] == ent_usr , parametros])
                           break

        


# exibir apenas nome do povo,terra e situação legla
def povo_reduzido():
     ent_usr = input("digite o nome da etnia a ser selecionada: ").strip().capitalize()
     while ent_usr not in povos:
            ent_usr = input("digite o nome da etnia a ser selecionada: ").strip().capitalize()
     print("\n\n")
     df_terras.loc[df_terras["etnia_nome"] == ent_usr, 'etnia_nome','terrai_nome','uf_sigla','fase_ti','modalidade_ti','dominio_uniao',]






#     função para amostragem de dados seguindo parametro de terras
def terra_indigena_escolha(*args):
        ent_usr = input("digite o nome da terra indigena a ser selecionada: ").strip().capitalize()
        while ent_usr not in terra_gerais:
            ent_usr = input("digite o nome da terra indigena a ser selecionada: ").strip().capitalize()
        print("\n\n") 
        completo_simp = input("deseja a exibição completa dos dados ou simplficada ?: ").strip().capitalize()   
        while not (completo_simp == "completo" or completo_simp == "simplificada"):
             completo_simp = input("deseja a exibição completa dos dados ou simplficada ?: ").strip().capitalize()
        if completo_simp == "completo":
             print(df_terras.loc[df_terras['terrai_nome'] == ent_usr , :] ) 

        if completo_simp == "simplificada":
             print("as terras disponiveis são: ")
             exibir_terras()
             while True:
                      parametros = []
                      novo_parametro = input('digite um novo parametro para ser exibido em sua analise, \n para finalizar os parametros diigite "sair"')
                      parametros.append(novo_parametro)
                      if novo_parametro == "sair": 
                           print(df_terras.loc[df_terras['terrai_nome'] == ent_usr , parametros])
                           break




def risco(*args):
     fora_de_risco = ["Regularizada", "Homologada"]
     AREAS_DE_RISCO = df_terras.loc[(~df_terras["fase_ti"].isin((fora_de_risco))), ["terrai_codigo","etnia_nome","terrai_nome","uf_sigla","municipio_nome","fase_ti","modalidade_ti","faixa_fronteira","the_geom"]]
     return AREAS_DE_RISCO





#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# pós analise primaria filtrar desejo do usuario para exibir mapeamento geografico de area por terra terras ou povo escolhido
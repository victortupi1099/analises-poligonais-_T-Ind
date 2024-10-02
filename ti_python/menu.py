#base para arquivos
import pandas as pd 
import geopandas as gpd
import matplotlib.pyplot as plt
import func
df_terras = pd.DataFrame(pd.read_csv('tis_poligonais.csv'))
listnum = [1,2,3,4]
povos = df_terras["etnia_nome"].unique().tolist()
terra_gerais = df_terras[ 'terrai_nome'].unique().tolist()



for i in range(20):
      print('\n')

print('Bem vindo ao menu de seleção!\n\n este programa funciona com a base de dados "tis_poligonais.csv" disponibilizada pela Funai.')
print("ao escolher um parametro defido pode-se acessar diferentes informações sobre terras e povos selecionados.\n")


while True: 
     print("deseja filtrar a manipulação de dados através de quais filtros?")
     print("  povos indigenas registrados : 1 \n terras indigenas registradas : 2 \n povos em situação de homologado e regularizado : 3\n povos fora da situação de homologado ou regularizado : 4\n")
     filtro_1 = int(input("você: "))
     while filtro_1 not in listnum:
           print("\n")
           print("por favor digite um filtro valido \n deseja filtrar a manipulação de dados através dos povos ou aldeias?")
           filtro_1 = int(input("\nvocê: "))


     if  filtro_1 == 1:
           escolha_inicial = input("\ndeseja exibir os povos catalogados? ").strip()
           if escolha_inicial == "sim":
                func.exibir(povos)
                func.povo_escolha()

     if  filtro_1 == 2:     
           escolha_inicial = input("deseja exibir as terras indigenas catalogadas? ").strip()
           if escolha_inicial == "sim":
                func.exibir_terras(terra_gerais)
                func.terra_indigena_escolha()

    # if filtro_1 == "3": 
        

     if filtro_1 == 4:
           func.risco()






#     função para amostragem de dados seguindo parametro de terras

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# pós analise primaria filtrar desejo do usuario para exibir mapeamento geografico de area por terra terras ou povo escolhido
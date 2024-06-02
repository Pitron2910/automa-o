import pyautogui as pg
import time 

link_empresa = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pg.PAUSE = 0.5

# 1) abrir o chrome   

pg.press("win")
pg.write("chrome")
pg.press("enter")

# 2) abir o servidor da empresa

pg.write(link_empresa)
pg.press("enter")
time.sleep(3)

# 3) fazer login:

pg.click(x=702, y=376)

pg.write("pietro.alkmin@gmail.com")

pg.press("tab")

pg.write("citrus91")

pg.press("enter")

# 3) importar a tabela produtos pelo pandas5.0      

import pandas as pd


# Leitura do arquivo CSV
tabela = pd.read_csv("produtos.csv")
print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # Clicar no campo de código
    pg.click(x=750, y=258)
    
    # Preencher o campo
    pg.write(str(tabela.loc[linha, "codigo"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "marca"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "tipo"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "categoria"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "preco_unitario"]))
    pg.press("tab")
    pg.write(str(tabela.loc[linha, "custo"]))
    pg.press("tab")
    
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pg.write(str(obs))
    pg.press("tab")
    pg.press("enter")  # Cadastra o produto (botão enviar)
    pg.scroll(5000)  # Scroll para o topo

# Passo 5: Repetir o processo de cadastro até o fim


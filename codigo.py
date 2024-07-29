import pyautogui
import time


#Pausa de 0.5 segundos entre cada comando
pyautogui.PAUSE = 0.5


#Pressionar a tecla win
pyautogui.press("win")

#Digitar edge
pyautogui.write("edge")

#Pressionar a tecla enter
pyautogui.press("enter")

# Entrar no link https://dlp.hashtagtreinamentos.com/python/intensivao/login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")

pyautogui.press("enter")

#apenas nessa parte do código irá esperar 3 segundos para seguir o próximo comando. 
time.sleep(3)


# Passo 2 - Fazer Login 
pyautogui.click(x=731, y=349)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("amilton_mamede@gmail.com")

# Passar para campo de senha
pyautogui.press("tab")
pyautogui.write("minha senha")

#Clicar em logar
pyautogui.click (x=941, y=515)

# Passo 3 - Importar a base de dados

import pandas

tabelaProdutos= pandas.read_csv("produtos.csv")

# Passo 4 - Cadastrar produtos
for linha in tabelaProdutos.index:

    pyautogui.click(x=966, y=245)


    codigo= str(tabelaProdutos.loc[linha, "codigo"])
    pyautogui.write(codigo)

    marca= str(tabelaProdutos.loc[linha, "marca"])
    pyautogui.press("tab")
    pyautogui.write(marca)

    tipo= str(tabelaProdutos.loc[linha, "tipo"])
    pyautogui.press("tab")
    pyautogui.write(tipo)

    categoria= str(tabelaProdutos.loc[linha, "categoria"])
    pyautogui.press("tab")
    pyautogui.write(categoria)

    preco= str(tabelaProdutos.loc[linha, "preco_unitario"])
    pyautogui.press("tab")
    pyautogui.write(preco)

    custo= str(tabelaProdutos.loc[linha, "custo"])
    pyautogui.press("tab")
    pyautogui.write(custo)

    obs= str(tabelaProdutos.loc[linha, "obs"])
    pyautogui.press("tab")
    if obs != "nan":
        pyautogui.write(obs)

    #Clicando no botão de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(1000)
import pandas
import pyautogui
from time import sleep

# 1
# abrir o chome
pyautogui.press('win')
pyautogui.write('Chome')
pyautogui.press("enter")
sleep(2)
pyautogui.press("tab")
pyautogui.press("enter")
pyautogui.PAUSE = 2.0
sleep(2)

# digitar site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
sleep(3)
# esperar 3s

# fazer login
pyautogui.press('tab')
sleep(2)

pyautogui.write("arieljaks")

pyautogui.press("tab")
pyautogui.write("erickkid123")
pyautogui.press("enter")


tabela = pandas.read_csv("Nova pasta/produtos.csv")

print(tabela)

# Passo 4: Cadastrar 1 produto

for linha in tabela.index:

    pyautogui.press("tab")

    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")  # passar para o próximo campo
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")  # passar para o próximo campo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")
    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

pyautogui.press("tab")  # passar para o próximo campo
preco_unitario = str(tabela.loc[linha, "preco_unitario"])
pyautogui.write(preco_unitario)

pyautogui.press("tab")  # passar para o próximo campo
custo = str(tabela.loc[linha, "custo"])
pyautogui.write(custo)

pyautogui.press("tab")  # passar para o próximo campo
obs = str(tabela.loc[linha, "obs"])

if obs != "nan":
    pyautogui.write(obs)

pyautogui.press("tab")  # passou para o botao enviar
pyautogui.press("enter")

pyautogui.scroll(10000)

# Passo 5: Repetir para todos os produtos

# nan -> Not a Number

pyautogui.press("tab")
pyautogui.press("enter")

pyautogui.scroll(1000)

# Passo 5: Repetir para todos os produtos


# pyautogui.hotkey -> aperta uma combinação de teclas
# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla
# pyautogui.write -> escrever um texto

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/
# Passo 2: Fazer login
# Passo 3: Importar a base de dados
# Passo 4: Cadastrar 1 produto
# Passo 5: Repetir para todos os produtosSS

# pyautogui -> fazer automações com python

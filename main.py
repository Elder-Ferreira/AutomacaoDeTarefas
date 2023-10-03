import pyautogui
import time

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"

pyautogui.write(link)
pyautogui.press("enter")
time.sleep(3)

pyautogui.click(x=576, y=399)
pyautogui.write("testeautomatizado@gmail.com")
pyautogui.press("tab")
pyautogui.write("teste123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(1)
pyautogui.press("enter")


import pandas

tabela = pandas.read_csv("produtos.csv")
# print(tabela)

for linha in tabela.index:
    pyautogui.click(x=625, y=281)

    codigo = tabela.loc[linha, "codigo"]
    marca = tabela.loc[linha, "marca"]

    pyautogui.write(str(codigo))
    pyautogui.press("tab")
    pyautogui.write(str(marca))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pandas.isna(obs):
        pyautogui.write(str(obs))

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(-5000)
    time.sleep(1)
    pyautogui.scroll(+5000)


# enviar_email()

import requests
import sys
import os
import time
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, como Gecko) Chrome/95.0.4638.69 Safari/537.36"
}


os.system("cls")

os.system("clear")

texto = "Seja bem vindo ao progama da D3S3RT0RA"

for letra in texto:
	print(letra, end="",flush=True)
	time.sleep(0.1)
print()
print()
dev = input("Informe o site para extrair o codigo-fonte:\n")
r = requests.get(dev)
sou = BeautifulSoup(r.text, "lxml")
# Exibir o código-fonte no terminal
print(sou.prettify())

with open("semente.txt", "a", encoding="utf-8") as de:
    de.write(sou.prettify())  # Salvar a saída formatada
    de.write("\n\n")  # Adicionar duas quebras de linha para separar as entradas

print("Código-fonte salvo em 'semente.txt'")



'''teste = Functions.DataBase()
teste.insertCommandRequest('e nois', 'piniquinho', 'chupeta', 'linguiça')
teste.insertCommandRequest('seila', 'piniquinho', 'chupeta', 'linguiça')
print(teste.getCommandRequests())
print()
teste.delCommandRequest('e nois')
print(teste.getCommandRequests())
print()

teste.insertHomeWorkManagement('Name', 'plat', 'files', 'seila', 'e nois')
print(teste.getHomeWorkManagement())
teste.delHomeWorkManagement('files')
print(teste.getHomeWorkManagement())'''

'''import requests, json

#KEY: 1d2780d8
#SALTO: 447959

requsição = requests.get('https://api.hgbrasil.com/weather?key=1d2780d8&city_name=Salto,SP')
#requsição = requests.get('http://apiadvisor.climatempo.com.br/api/v1/anl/synoptic/locale/BR?token=8563510d7b01f40d817c7de4c51b6d2e')
clima = json.loads(requsição.text)
date = clima['results']['forecast'][0]['date']
wheather = clima['results']['forecast'][0]['description']
max = clima['results']['forecast'][0]['max']
min = clima['results']['forecast'][0]['min']
city = clima['results']['city']

print(json.dumps(clima, indent= 2))
print(city)'''

'''import json

json_ = open(r'E:\Sexta-Feira(A.I.)-Mark 5\InterfaceInteraction.json', 'w')
dict_ = {"ID": "512", "Data": "1"}
json_.write(json.dumps(dict_, indent=2))
json_.close()

json1 = open(r'E:\Sexta-Feira(A.I.)-Mark 5\InterfaceInteraction.json', 'r')

print(json.load(json1))

json1.close()'''

#===============================================================================
# ENTRAR NO GITHUB
#===============================================================================
'''from selenium import webdriver
from selenium.webdriver import ChromeOptions
from pyautogui import typewrite


ProjectName = str(input('NOME DO PROJETO> '))
NameProject = list()

for c in ProjectName.split():
    NameProject.append(c.title())

NameProject = ''.join(NameProject)

print(NameProject)

options = ChromeOptions()
options.add_argument('--start-maximized')

browser = webdriver.Chrome(r'E:\Sexta-Feira(A.I.)-Mark 5\BrowserBot\chromedriver.exe', options= options)

browser.get('https://www.github.com/')
browser.find_element_by_xpath('/html/body/div[1]/header/div/div[2]/div[2]/a[1]').click()
browser.find_element_by_xpath('//*[@id="login_field"]').click()
typewrite('gabrielsirtoricorrea')
browser.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[2]').click()
typewrite('Gazao015')
browser.find_element_by_xpath('/html/body/div[3]/main/div/form/div[4]/input[9]').click()
browser.find_element_by_xpath('/html/body/div[4]/div/aside[1]/div[2]/div[1]/div/h2/a').click()
browser.find_element_by_xpath('/html/body/div[4]/main/div/form/div[2]/auto-check/dl/dd/input').click()
typewrite(NameProject) # <--- Nome do projeto
browser.find_element_by_xpath('/html/body/div[4]/main/div/form/div[3]/dl/dd/input').click()
typewrite(f'Projeto {NameProject} ') #<- Descrição do projeto
browser.find_element_by_xpath('/html/body/div[4]/main/div/form/div[3]/div[4]/div/label/input[2]').click()
browser.find_element_by_xpath('/html/body/div[4]/main/div/form/div[3]/div[4]/ul/li[2]/details/summary').click()
browser.find_element_by_xpath('/html/body/div[4]/main/div/form/div[3]/div[4]/ul/li[2]/details/div/div/div/div[1]/label[4]').click()
browser.find_element_by_xpath('/html/body/div[4]/main/div/form/div[3]/button').click()

browser.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/div[3]/div[2]/form/button').click()
typewrite('Sexta-FeiraInteraction.py')
browser.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/div/form[2]/div[5]/div[2]/div/div[5]/div[1]/div/div').click()
typewrite('import os \nos.system("git commit -m NovoCommitTest")\nos.system("git push origin maste")')

browser.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div/div/form[2]/div[6]/button').click()

path = f"https://github.cotm/GabrielSirtoriCorrea/{NameProject}.git"

print(path)'''

'''from socket import *
import threading
from time import sleep
import json

serverHost = '192.168.0.5'
serverPort = 5000

sock = socket(AF_INET, SOCK_STREAM, 0)
sock.connect((serverHost, serverPort))


msg = {'RequestID': 'ServerToLocalComunication', 'Command': 'teste'}

msgEncode = json.dumps(msg).encode()

sock.send(msgEncode)'''

'''import os

repository = r'https://github.com/GabrielSirtoriCorrea/BuzzWireGame.git'
Name = repository.split('/')[4].replace('.git', '')
path = f'PROJETOS/{Name}'

os.system(f'git clone {repository} {path}')'''



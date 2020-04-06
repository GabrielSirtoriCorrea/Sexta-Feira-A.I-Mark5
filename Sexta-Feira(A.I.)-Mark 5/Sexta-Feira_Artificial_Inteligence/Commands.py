import Functions, json, requests, re
from datetime import datetime
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from pyautogui import typewrite

def callCommand(command, speech):
    funcs = globals()
    funcs[command](speech)

def Climate(speech):
    requsição = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Salto,BR&appid=c336b96c2d310a1cf64e375dd396ec93')
    response = json.loads(requsição.text)

    climate = (response['weather'][0]['main'])

    if climate == 'Clouds':
        climate = 'Nublado'

    elif climate == 'Rain':
        climate = 'Chuvoso'

    elif climate == 'Clear':
        climate = 'Limpo'

    elif climate == 'Thunderstorm':
        climate = 'Chuvoso com trovoadas'

    Functions.speak(f'Hoje o clima em salto está {climate}')

def Temperature(speech):
    try:
        requsição = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Salto,BR&appid=c336b96c2d310a1cf64e375dd396ec93')
        clima = json.loads(requsição.text)
        print(clima)

        tempo = (clima['main']['temp'])
        tempo += -273.15
        Functions.speak(f'A temperatura em Salto, é de aproximadamente {tempo:.2f} graus Celcius')
    except:
        Functions.speak('Desculpe. Não consegui encontrar a cidade')

def Time(speech):
    Functions.speak(f'Agora são {datetime.now().hour} horas e {datetime.now().minute} minutos')

def Today(speech):
    Functions.speak(f'Hoje é dia {datetime.now().day} do {datetime.now().month} de {datetime.now().year}')

def Wheather(speech):

    requsição = requests.get(f'https://api.hgbrasil.com/weather?key=1d2780d8&city_name=Salto,SP')
    clima = json.loads(requsição.text)

    wheather = clima['results']['forecast'][1]['description']
    max = clima['results']['forecast'][1]['max']
    min = clima['results']['forecast'][1]['min']
    city = clima['results']['city']

    Functions.speak(f'Amanhã em {city} teremos {wheather}, e temperaturas com máxima de aproximadamente até {max} graus, e mínima de aproximadamente até {min} graus')

def sendCloseToInterface(speech):
    Functions.sendToInterface(512, 0)

def sendProjectToInterface(speech):
    Functions.speak('Atualmente esses são os projetos em andamento')
    Functions.sendToInterface(512, 1)

def sendReminderToInterface(speech):
    Functions.speak('Esses são os lembretes que você agendou')
    Functions.sendToInterface(512, 2)

def sendHomeWorkToInterface(speech):
    Functions.speak('Essas são as tarefas pendentes')
    Functions.sendToInterface(512, 3)

def sendTabelaPeriodicaToInterface(speech):
    Functions.speak('Abrindo tabela periódica')
    Functions.sendToInterface(512, 4)

def sendMapaMundiToInterface(speech):
    Functions.speak('Abrindo Mapa mundi')
    Functions.sendToInterface(512, 5)

def sendMapaMundiVegetacaoToInterface(speech):
    Functions.speak('Abrindo mapa mundi vegetação')
    Functions.sendToInterface(512, 6)

def sendBrasilPoliticoToInterface(speech):
    Functions.speak('Abrindo o mapa do brasil político')
    Functions.sendToInterface(512, 7)

def sendDistEletronicaToInterface(speech):
    Functions.speak('Abrindo Distribuição eletrônica de Linus Pauling')
    Functions.sendToInterface(512, 8)

def sendPhysicalEquationsToInterface(speech):
    Functions.speak('Aqui estão algumas equações utilizadas na física mecânica')
    Functions.sendToInterface(512, 9)

def sendAngleTableToInterface(speech):
    Functions.speak('Aqui está a tabela do seno, cosseno e tangente dos Ângulos')
    Functions.sendToInterface(512, 10)

def delHomeWork(speech):
    DataBase = Functions.DataBase()
    HomeWorks = DataBase.getHomeWorkManagement()

    for HomeWork in HomeWorks:
        if HomeWork[2] in speech:
            Functions.speak('Muito bem. Estou removendo essa tarefa da sua lista de tarefas')
            DataBase.delHomeWorkManagement(HomeWork[2])

def CreateNewProject(speech):
    def CreateProjectGithub(ProjectName):
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

        path = f"https://github.com/GabrielSirtoriCorrea/{NameProject}.git"

        print(path)
        browser.quit()
        return path


    NameProject = 'null'
    ProjectPlatforms = list()

    EnablePlatforms = ' python java arduino '

    DataBase = Functions.DataBase()

    speech = speech.replace('como', '')
    speech = speech.split()

    for word in speech:
        if word == 'nome' or 'cham' in word:
            NameProject = speech[speech.index(word) + 1]

    if NameProject == 'null':
        Functions.speak('Certo. Estou criando um repósitorio para o novo projeto no github. Mas como gostaria de chamá-lo?')
        NameProject = Functions.Recognition()

    for word in speech:
        if word in EnablePlatforms:
            ProjectPlatforms.append(word)

    while not ProjectPlatforms:
        Functions.speak('Criando o repositório do novo projeto, mas qual plataformas gostaria de utilizar?')
        platforms = Functions.Recognition()
        for word in platforms:
            if word in EnablePlatforms:
                ProjectPlatforms.append(word)

        if not ProjectPlatforms:
            Functions.speak('Chefe. Atualmente não existem essas plataformas. Escolha uma entre as disponiveis python, java ou arduino')

    ProjectURL = CreateProjectGithub(NameProject)

    DataBase.insertProject(NameProject, ''.join(ProjectPlatforms), ProjectURL)

    Request = {'RequestID': 'ServerToLocalComunication', 'Command': 'CreateNewProject', 'NameProject': NameProject,'Platforms': ''.join(ProjectPlatforms), 'ProjectURL': ProjectURL}
    Functions.ServerToLocalComunication(Request)

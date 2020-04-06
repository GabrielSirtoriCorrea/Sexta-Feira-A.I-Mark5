import speech_recognition as sr
import pyttsx3
import pyaudio
import sqlite3
import serial
import json
import requests
from translate import Translator
import random
from unicodedata import normalize
import time, datetime
from socket import *

def translate(word):
    translator = Translator(to_lang="pt")
    return translator.translate(word)

def ResponseSelector():
    responses = (3, 4, 5)
    responseChosen = random.choices(responses)
    return responseChosen[0]

def speak(text):
    speaker = pyttsx3.init('sapi5')
    speaker.say(text)
    speaker.runAndWait()

def Recognition():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)

        print('=-' * 30)

        print('Fale: ')
        audio = r.listen(source)
        speech = '  ' + r.recognize_google(audio, language='pt').lower() + '  '
        print('Você disse: ', speech)

        return speech

def SerialComunication(cod):
    try:
        portaUSB = serial.Serial('COM8', 9600)
        aux = str(cod)
        portaUSB.write(aux.encode())

    except:
        print()

def ConversationSetup():
    hour = int(datetime.datetime.now().hour)
    if 5 <= hour <= 11:
        speak('Bom dia chefe!')
    elif 12 <= hour <= 17:
        speak('Boa tarde chefe!')
    else:
        speak('Boa noite chefe!')



def languageUnderstanding(phrase):
    phrase = normalize('NFKD', phrase).encode('ASCII', 'ignore').decode('ASCII')
    phrase = phrase.replace(' ', '  ')

    filter = [[' o ', ' a ', ' os ', ' as ', ' um ', ' uma ', ' uns ', ' umas '], [' ante ', ' apos ', ' ate ', ' com ',' contra ', ' de ' ],
              [' desde ', ' entre ', ' para ', ' perante ', ' por ', ' sem ', ' sob ', ' sobre ',
                ' como '], [' e ', ' ainda ', ' tambem ', ' contudo ', ' entretanto ', ' mas ', ' entanto ', ' porem ',
                ' todavia ', ' assim ', ' entao ', ' logo ', ' pois ', ' porque ', ' por ', ' que ', ' para ', ' no ',
                ' na ']]

    phraseFiltered = phrase

    for wordClasses in filter:
        for word in wordClasses:
            if word in phrase:
                phraseFiltered = phraseFiltered.replace(word, '')

    phraseFiltered = phraseFiltered.replace('  ', ' ')

    print(phraseFiltered)
    return phraseFiltered

def sendToInterface(id, data):
    json_ = open(r'E:\Sexta-Feira(A.I.)-Mark 5\InterfaceInteraction.json', 'w')
    dict_ = {"ID": id, "Data": data}
    json_.write(json.dumps(dict_, indent=2))
    json_.close()

    json1 = open(r'E:\Sexta-Feira(A.I.)-Mark 5\InterfaceInteraction.json', 'r')

    print(json.load(json1))

    json1.close()

    time.sleep(1)

    json2 = open(r'E:\Sexta-Feira(A.I.)-Mark 5\InterfaceInteraction.json', 'w')
    dict2 = {"ID": 512, "Data": 1024}
    json2.write(json.dumps(dict2, indent=2))
    json2.close()

def ServerToLocalComunication(msg):
    try:
        serverHost = '192.168.0.4'
        serverPort = 4000

        sock = socket(AF_INET, SOCK_STREAM, 0)
        sock.connect((serverHost, serverPort))

        msgEncode = json.dumps(msg).encode()

        sock.send(msgEncode)
    except:
        print('ServerToLocalComunicationERROR')

class DataBase:
    def __init__(self):
        InteractionSQLPath = 'E:\\Sexta-Feira(A.I.)-Mark 5\\InteractionSQL.db'
        CommandsSQLPath = 'E:\\Sexta-Feira(A.I.)-Mark 5\\CommandsSQL.db'

        self.InteractionDB = sqlite3.connect(InteractionSQLPath)
        self.CommandsDB = sqlite3.connect(CommandsSQLPath)

        self.InteractionCursor = self.InteractionDB.cursor()
        self.CommandsCursor = self.CommandsDB.cursor()

        self.InteractionCursor.execute('CREATE TABLE IF NOT EXISTS Chat(Keyword1 TEXT, Keyword2 TEXT, Keyword3 TEXT, Response1 TEXT, Response2 TEXT, Response3 TEXT)')
        self.InteractionCursor.execute('CREATE TABLE IF NOT EXISTS CommandRequests(Keyword1 TEXT, Keyword2 TEXT, Keyword3 TEXT, Command TEXT)')

        self.CommandsCursor.execute('CREATE TABLE IF NOT EXISTS Projects(NameProject TEXT, ProjectPlatform TEXT, ProjectURL TEXT)')
        self.CommandsCursor.execute('CREATE TABLE IF NOT EXISTS Reminder(ReminderName TEXT, Time TEXT, Date TEXT)')
        self.CommandsCursor.execute('CREATE TABLE IF NOT EXISTS HomeWorkManagement(HomeWorkType TEXT, Subject TEXT, HomeWork TEXT, Delivery TEXT, HomeWorkDescription TEXT)')


        self.InteractionDB.commit()
        self.CommandsDB.commit()

    #Interaction Data Base

    def getChat(self):
        self.InteractionCursor.execute('SELECT * FROM Chat')
        return self.InteractionCursor.fetchall()

    def insertChat(self, key1, key2, key3, res1, res2, res3):
        self.InteractionCursor.execute('INSERT INTO Chat(Keyword1, Keyword2, Keyword3, Response1, Response2, Response3) VALUES (?,?,?,?,?,?)', (key1, key2, key3, res1, res2, res3))
        self.InteractionDB.commit()

    def delChat(self, deleteKey):
        self.InteractionCursor.execute(f'DELETE FROM Chat WHERE Keyword1 = ?', (deleteKey,))
        self.InteractionDB.commit()

    def upChat(self, updateNumber, updateKey, update1, update2, update3, update4, update5, update6):
        self.InteractionCursor.execute(f'UPDATE Chat SET Keyword1 = ?, Keyword2 = ?, Keyword3 = ?, Response1 = ?, Response2 = ?, Response3 = ? WHERE Keyword{updateNumber} = ?', (update1, update2, update3, update4, update5, update6, updateKey))
        self.InteractionDB.commit()

    def getCommandRequests(self):
        self.InteractionCursor.execute('SELECT * FROM CommandRequests')
        return self.InteractionCursor.fetchall()

    def insertCommandRequest(self, key1, key2, key3, command):
        self.InteractionCursor.execute('INSERT INTO CommandRequests(Keyword1, Keyword2, Keyword3, Command) VALUES (?,?,?,?)', (key1, key2, key3, command))
        self.InteractionDB.commit()

    def upCommandRequest(self, updateNumber, updateKey, update1, update2, update3, update4):
        self.InteractionCursor.execute(f'UPDATE CommandRequests SET Keyword1 = ?, Keyword2 = ?, Keyword3 = ?, Command = ? WHERE Keyword{updateNumber} = ?', (update1, update2, update3, update4, updateKey))
        self.InteractionDB.commit()

    def delCommandRequest(self, deleteKey):
        self.InteractionCursor.execute(f'DELETE FROM CommandRequests WHERE Keyword1 = ?', (deleteKey,))
        self.InteractionDB.commit()

    #Commands Data Base

    def getProjects(self):
        self.CommandsCursor.execute('SELECT * FROM Projects')
        return self.CommandsCursor.fetchall()

    def delProject(self, deleteKey):
        self.CommandsCursor.execute(f'DELETE FROM Projects WHERE NameProject = ?', (deleteKey,))
        self.CommandsDB.commit()

    def insertProject(self, name, platform, ProjectURL):
        self.CommandsCursor.execute('INSERT INTO Projects(NameProject, ProjectPlatform, ProjectURL) VALUES (?,?,?)', (name, platform, ProjectURL))
        self.CommandsDB.commit()

    def getReminder(self):
        self.CommandsCursor.execute('SELECT * FROM Reminder')
        return self.CommandsCursor.fetchall()

    def delReminder(self, deleteKey):
        self.CommandsCursor.execute(f'DELETE FROM Reminder WHERE ReminderName = ?', (deleteKey,))
        self.CommandsDB.commit()

    def insertReminder(self, name, time, date):
        self.CommandsCursor.execute('INSERT INTO Reminder(ReminderName, Time, Date) VALUES (?,?,?)', (name, time, date))
        self.CommandsDB.commit()

    def getHomeWorkManagement(self):
        self.CommandsCursor.execute('SELECT * FROM HomeWorkManagement')
        return self.CommandsCursor.fetchall()

    def delHomeWorkManagement(self, deleteKey):
        self.CommandsCursor.execute(f'DELETE FROM HomeWorkManagement WHERE HomeWork = ?', (deleteKey,))
        self.CommandsDB.commit()

    def insertHomeWorkManagement(self, type, subject, homework, delivery, desciption):
        self.CommandsCursor.execute('INSERT INTO HomeWorkManagement(HomeWorkType, Subject, HomeWork, Delivery, HomeWorkDescription) VALUES (?,?,?,?,?)', (type, subject, homework, delivery, desciption))
        self.CommandsDB.commit()



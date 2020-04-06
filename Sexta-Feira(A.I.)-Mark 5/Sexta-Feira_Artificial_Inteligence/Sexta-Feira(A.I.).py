import Functions
from Commands import callCommand

DataBase = Functions.DataBase()

UserInteractions = [DataBase.getChat(), DataBase.getCommandRequests()]

ResponseAccept = False

Functions.ConversationSetup()

while True:
    try:
        speech = Functions.languageUnderstanding(Functions.Recognition())
    except:
        speech = ''

    for interaction in UserInteractions:
        for keyword in interaction:
            if keyword[0] in speech and keyword[1] in speech and keyword[2] in speech and keyword in DataBase.getChat():
                Functions.speak(keyword[Functions.ResponseSelector()])

            elif keyword[0] in speech and keyword[1] in speech and keyword[2] in speech and keyword in DataBase.getCommandRequests():
                callCommand(keyword[3], speech)


import socketserver
from datetime import datetime
import json, Functions, time, os

#myHost = '192.168.0.113'
myHost = '192.168.0.4'
myPort = 5000


class ClientManage(socketserver.BaseRequestHandler):
    def handle(self):

        hora = datetime.now()
        print(f'Conectado por: {self.client_address} as {hora.hour}:{hora.minute}')

        data = self.request.recv(1024).decode('utf-8')
        print(data)

        try:
            data = json.loads(data)

            if data['RequestId'] == 'AppSendHomeWork':
                DataBase = Functions.DataBase()
                DataBase.insertHomeWorkManagement(data['HomeWorkType'], data['Subject'], Functions.languageUnderstanding(data['HomeWork']), data['Delivery'], data['Description'])
                print(DataBase.getHomeWorkManagement())
            elif data['RequestId'] == 'AppStartFriday':
                print(data['RequestId'])
                os.startfile(r'E:\Sexta-Feira(A.I.)-Mark 5\Sexta-Feira_Interface\dist\Sexta-Feira_Interface.jar')
                os.startfile(r'E:\Sexta-Feira(A.I.)-Mark 5\Sexta-Feira_Artificial_Inteligence\Sexta-Feira(A.I.).py')
        except:
            pass


adress = (myHost, myPort)
server = socketserver.ThreadingTCPServer(adress, ClientManage)
server.serve_forever()

from Functions import DataBase

DataBase = DataBase()

print()
print("////////////////////////////////// BEM-VINDO \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ")
print("///////////////////////////////////// AO \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ")
print("///////////////////////////// SEXTA-FEIRA SQL INJECT \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\ ")
print('Digite -help- para ajuda\n')

while True:
    command = str(input('Shell>>> '))

    if command == 'help':
        print('\ngetChat - Retorna todas as palavras chave e respostas de conversa no Banco de dados\n'
              '\nchatInject - Injeta palavras chave e respostas no Banco de dados\n'
              '\ngetCommandRequests   - Retorna as palavras chave e o comando de todas as CommandRequests do Banco de dados\n'
              '\nCommandRequestInject - Injeta palavras chave e um commando no CommandsRequests do Banco de dados\n'
              '\nupChat - Atualiza as palavras chave e respostas de uma conversa do Banco de dados\n'
              '\nupCommandRequest - Atualiza as palavra chave e comando do Banco de dados\n')

    elif command == 'getChat':
        for keyword in DataBase.getChat():
            print(f'Palavras chave: {keyword[0]} \n                {keyword[1]} \n                {keyword[2]}\n')
            print(f'Respostas:      {keyword[3]} \n                {keyword[4]} \n                {keyword[5]}\n')


    elif command == 'getCommandRequests':
        for keyword in DataBase.getCommandRequests():
            print(f'Palavras chave: {keyword[0]} \n                {keyword[1]} \n                {keyword[2]}\n')
            print(f'Comando:        {keyword[3]} \n')


    elif command == 'chatInject':
        inject1 = str(input('Adicione a primeira palavra chave: '))
        inject2 = str(input('Adicione a segunda palavra chave: '))
        inject3 = str(input('Adicione a terceira palavra chave: '))

        response1 = str(input('Resposta 1 para essas palavras:'))
        response2 = str(input('Resposta 2 para essas palavras:'))
        response3 = str(input('Resposta 3 para essas palavras:'))

        DataBase.insertChat(inject1, inject2, inject3, response1, response2, response3)

    elif command == 'CommandRequestInject':
        inject1 = str(input('Adicione a primeira palavra chave: '))
        inject2 = str(input('Adicione a segunda palavra chave: '))
        inject3 = str(input('Adicione a terceira palavra chave: '))

        response1 = str(input('Método a ser chamado:'))

        DataBase.insertCommandRequest(inject1, inject2, inject3, response1)

    elif command == 'upChat':
        updateKey = str(input('Digite uma palavra chave da interação que deseja atualizar: '))
        updateNumber = str(input('Digite o numero dessa palavra chave: '))

        inject1 = str(input('Digite a nova primeira palavra chave: '))
        inject2 = str(input('Digite a nova segunda palavra chave: '))
        inject3 = str(input('Digite a nova terceira palavra chave: '))

        response1 = str(input('Resposta 1 para essas palavras:'))
        response2 = str(input('Resposta 2 para essas palavras:'))
        response3 = str(input('Resposta 3 para essas palavras:'))

        DataBase.upChat(updateNumber, updateKey, inject1, inject2, inject3, response1, response2, response3)

    elif command == 'upCommandRequest':
        updateKey = str(input('Digite uma palavra chave da interação que deseja atualizar: '))
        updateNumber = str(input('Digite o numero dessa palavra chave: '))

        inject1 = str(input('Digite a nova primeira palavra chave: '))
        inject2 = str(input('Digite a nova segunda palavra chave: '))
        inject3 = str(input('Digite a nova terceira palavra chave: '))

        response1 = str(input('Novo comando: '))

        DataBase.upCommandRequest(updateNumber, updateKey, inject1, inject2, inject3, response1)

    elif command == 'delChat':
        delKey = str(input('Digite a primeia palavra chave da conversa que quer deletar: '))
        DataBase.delChat(delKey)

    elif command == 'delCommandRequest':
        delKey = str(input('Digite a primeia palavra chave do CommandRequest que quer deletar: '))
        DataBase.delCommandRequest(delKey)

    elif command == 'getHomeWork':
        print(DataBase.getHomeWorkManagement())

    elif command == 'exit':
        break


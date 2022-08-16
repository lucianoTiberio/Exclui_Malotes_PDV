import mysql.connector
import time



def con():
    print('---------------------------------------')
    ip = input('Qual o ip da maquina?\n')
    print('---------------------------------------')
    print('Deseja voltar o malote ou excluir o malote?\n')
    acao = int(input('1 excluir / 2 voltar\n'))

    try:
        conexao = mysql.connector.connect(

            host=f"{ip}",
            user='root',
            password='',
            database='PDV',
        )

        cursor = conexao.cursor()

        def menu():

            print('Deseja alterar mais Malotes nesse PDV?\n')
            print('---------------------------------------')
            print('1 - Excluir Malotes')
            print('---------------------------------------')
            print('2 - voltar Malotes')
            print('---------------------------------------')
            print('3 - Alterar Malotes em outro PDV')
            print('---------------------------------------')
            print('4 - Sair\n')
            acao = int(input())

            if acao == 1:
                exclui()
            elif acao == 2:
                volta()
            elif acao == 3:
                con()
            elif acao == 4:
                quit()
            else:
                print('opção invalida')

                time.sleep(3)
                menu()

        def exclui():
            print('---------------------------------------')
            data = input('Qual a data do malote? (Ano-Mes-Dia)\n')
            print('---------------------------------------')
            malote = int(input('Qual o numero do malote?\n'))

            comando = f"SELECT numMalote FROM T_Sangria WHERE datafiscal = '{data}' and maloteEnviado = 'N'"

            cursor.execute(comando)

            resultado = cursor.fetchall()  # ler o banco de dados

            lista = [tupla[0] for tupla in resultado]


            if malote not in lista:

                time.sleep(3)
                print('---------------------------------------')
                print("Malote não encontrado")
                print("Verifique as informações e tente novamente")

                con()

            else:

                comando = f"UPDATE T_Sangria SET maloteEnviado = 'S' WHERE numMalote IN ({malote}) AND datafiscal = '{data}'"

                cursor.execute(comando)

                cursor.fetchall()

                print('Status alterado com sucesso\n')
                time.sleep(2)

                menu()

        def volta():
            print('---------------------------------------')
            data = input('Qual a data do malote? (Ano-Mes-Dia)\n')
            print('---------------------------------------')
            malote = int(input('Qual o numero do malote?\n'))

            comando = f"SELECT numMalote FROM T_Sangria WHERE datafiscal = '{data}' and maloteEnviado = 'S'"

            cursor.execute(comando)

            resultado = cursor.fetchall()  # ler o banco de dados

            lista = [tupla[0] for tupla in resultado]

            if malote not in lista:
                time.sleep(3)
                print('---------------------------------------')
                print("Malote não encontrado")
                print("Verifique as informações e tente novamente")

                con()

            else:

                comando = f"UPDATE T_Sangria SET maloteEnviado = 'N' WHERE numMalote IN ({malote}) AND datafiscal = '{data}'"

                cursor.execute(comando)

                cursor.fetchall()

                print('Status alterado com sucesso\n')

                time.sleep(2)

                menu()


        if acao == 1:
            exclui()
        elif acao == 2:
            volta()
        else:
            time.sleep(2)
            print('OPÇÃO INVALIDA')
            con()
    except:
        print('Erro de conexão, verifique o IP e se o PDV esta ligado')
con()
import socket
import threading

from Contaa import Conta
from Cliente import Cliente

class ClienteThread(threading.Thread):
    def __init__(self, clientAddress, clientsocket):
        threading.Thread.__init__(self)
        self.csocket = clientsocket
        print("\nNova Conexão: ", clientAddress)

    def run(self):
        print("Conectado de: ", clientAddress)
        client = ''
        while True:
            recebe = self.csocket.recv(10240).decode()
            recebe = recebe.split(',')
            if recebe[0] == 'bye':
                break

            if recebe[0] == 'login':
                usuario = str(recebe[1])
                senha = str(recebe[2])
                retorno = cad.login(usuario, senha)
                retorno = str(retorno)
                self.csocket.send(retorno.encode())

            elif recebe[0] == 'deposita':
                saldo = recebe[1]
                objeto = recebe[2]
                valor = recebe[3]
                valor = float(valor)
                objeto = int(objeto)
                saldo = float(saldo)
                print(saldo)
                print(objeto)
                print(valor)
                cad.deposita(saldo, objeto, valor)

            elif recebe[0] == 'atualiza':
                objeto = recebe[1]
                objeto = int(objeto)
                retorno = cad.atualiza(objeto)
                retorno = str(retorno)
                self.csocket.send(retorno.encode())

            elif recebe[0] == 'extrato':
                numero = int(recebe[1])
                retorno = cad.extrato(numero)
                retorno = str(retorno)
                self.csocket.send(retorno.encode())

            elif recebe[0] == 'sacar':
                saldo = recebe[1]
                objeto = recebe[2]
                valor = recebe[3]
                valor = float(valor)
                objeto = int(objeto)
                saldo = float(saldo)
                print(saldo)
                print(objeto)
                print(valor)
                cad.sacar(saldo, objeto, valor)

            elif recebe[0] == 'numero':
                numero = recebe[1]
                numero = int(numero)
                retorno = cad.numero_conta(numero)
                retorno = str(retorno)
                self.csocket.send(retorno.encode())

            elif recebe[0] == 'transferir':
                saldo = recebe[1]
                objeto = recebe[2]
                saldo1 = recebe[3]
                objeto1 = recebe[4]
                valor = recebe[5]
                nome = recebe[6]
                nome1 = recebe[7]
                objeto = int(objeto)
                objeto1 = int(objeto1)
                saldo = float(saldo)
                saldo1 = float(saldo1)
                valor = float(valor)
                nome = str(nome)
                nome1 = str(nome1)
                cad.transfere(saldo, objeto, saldo1, objeto1, valor, nome, nome1)

            elif recebe[0] == 'cadastrar':
                usuario = recebe[1]
                usuario = str(usuario)
                retorno = cad.usuario(usuario)
                retorno = str(retorno)
                self.csocket.send(retorno.encode())

            elif recebe[0] == 'cliente':
                nome = recebe[1]
                cpf = recebe[2]
                usuario = recebe[3]
                senha = recebe[4]
                nome = str(nome)
                cpf = str(cpf)
                usuario = str(usuario)
                senha = str(senha)
                retorno = Cliente(nome, cpf, usuario, senha)
                print(retorno)
                print(type(retorno))
                client = retorno

            elif recebe[0] == 'cadastro':
                retorno = cad.cadastrar(client)
                retorno = str(retorno)
                self.csocket.send(retorno.encode())

        print("Client at ", clientAddress, "Disconnected...\n")

cad = Conta()

host = 'localhost'
port = 8001
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
print('Servidor iniciado!')
print('aguardando conexão...')

while True:
    serv_socket.listen(1)
    clientsock, clientAddress = serv_socket.accept()
    newthread = ClienteThread(clientAddress, clientsock)
    newthread.start()

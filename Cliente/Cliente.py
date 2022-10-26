import socket

from tela_cadastro import Tela_Cadastro
from tela_login import Tela_Login
from tela_inicial import Tela_Inicial
from tela_saldo import Tela_Saldo
from tela_deposita import Tela_Deposita
from tela_extrato import Tela_Extrato
from tela_sacar import Tela_Sacar
from tela_transferencia import Tela_Transferencia

import sys
from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QMessageBox, QApplication, QMainWindow, QFileDialog

class Ui_Main(QtWidgets.QWidget):
    def setupUi(self, Main):
        Main.setObjectName('Main')
        Main.resize(640, 480)

        self.QtStack = QtWidgets.QStackedLayout()

        self.stack0 = QtWidgets.QMainWindow()
        self.stack1 = QtWidgets.QMainWindow()
        self.stack2 = QtWidgets.QMainWindow()
        self.stack3 = QtWidgets.QMainWindow()
        self.stack4 = QtWidgets.QMainWindow()
        self.stack5 = QtWidgets.QMainWindow()
        self.stack6 = QtWidgets.QMainWindow()
        self.stack7 = QtWidgets.QMainWindow()

        self.tela_login = Tela_Login()
        self.tela_login.setupUi(self.stack0)

        self.tela_cadastro = Tela_Cadastro()
        self.tela_cadastro.setupUi(self.stack1)

        self.tela_inicial = Tela_Inicial()
        self.tela_inicial.setupUi(self.stack2)

        self.tela_saldo = Tela_Saldo()
        self.tela_saldo.setupUi(self.stack3)

        self.tela_deposita = Tela_Deposita()
        self.tela_deposita.setupUi(self.stack4)

        self.tela_extrato = Tela_Extrato()
        self.tela_extrato.setupUi(self.stack5)

        self.tela_sacar = Tela_Sacar()
        self.tela_sacar.setupUi(self.stack6)

        self.tela_transferencia = Tela_Transferencia()
        self.tela_transferencia.setupUi(self.stack7)

        self.QtStack.addWidget(self.stack0)
        self.QtStack.addWidget(self.stack1)
        self.QtStack.addWidget(self.stack2)
        self.QtStack.addWidget(self.stack3)
        self.QtStack.addWidget(self.stack4)
        self.QtStack.addWidget(self.stack5)
        self.QtStack.addWidget(self.stack6)
        self.QtStack.addWidget(self.stack7)

class Main(QMainWindow,Ui_Main):


    def __init__(self, parent = None):
        super(Main, self).__init__(parent)
        self.setupUi(self)
        self.tela_login.pushButton_2.clicked.connect(self.abrirtelacadastro)
        self.tela_login.pushButton.clicked.connect(self.BotaoLogin)
        self.tela_cadastro.pushButton.clicked.connect(self.botaoCadastra)
        self.tela_cadastro.pushButton_2.clicked.connect(self.voltar)
        self.tela_inicial.pushButton.clicked.connect(self.saldo_main)
        self.tela_inicial.pushButton_2.clicked.connect(self.extrato_main)
        self.tela_inicial.pushButton_3.clicked.connect(self.abrir_transferencia)
        self.tela_inicial.pushButton_4.clicked.connect(self.abrir_sacar)
        self.tela_inicial.pushButton_5.clicked.connect(self.abrir_deposita)
        self.tela_inicial.pushButton_6.clicked.connect(self.voltar1)
        self.tela_saldo.pushButton.clicked.connect(self.voltar2)
        self.tela_deposita.pushButton_2.clicked.connect(self.voltar2)
        self.tela_deposita.pushButton_3.clicked.connect(self.deposita_main)
        self.tela_extrato.pushButton_2.clicked.connect(self.voltar2)
        self.tela_sacar.pushButton_2.clicked.connect(self.voltar2)
        self.tela_sacar.pushButton.clicked.connect(self.sacar_main)
        self.tela_transferencia.pushButton_2.clicked.connect(self.voltar2)
        self.tela_transferencia.pushButton.clicked.connect(self.transferencia_main)

    def botaoCadastra(self):
        nome = self.tela_cadastro.lineEdit.text()
        cpf = self.tela_cadastro.lineEdit_2.text()
        usuario = self.tela_cadastro.lineEdit_3.text()
        senha = self.tela_cadastro.lineEdit_4.text()
        senha1 = self.tela_cadastro.lineEdit_9.text()


        if not(nome == '' or cpf == '' or usuario == '' or senha == '' or senha1 == ''):
            if (senha == senha1):
                client_socket.send(f'cadastrar,{usuario}'.encode())
                retorno = client_socket.recv(10240)
                retorno = eval(retorno)
                if(retorno == None):
                    client_socket.send(f'cliente,{nome},{cpf},{usuario},{senha}'.encode())
                    client_socket.send(f'cadastro'.encode())
                    retorno = client_socket.recv(10240)
                    retorno = eval(retorno)
                    if(retorno == True):
                        QMessageBox.information(None, 'POOII', 'Conta criada com sucesso!')
                        self.tela_cadastro.lineEdit.setText('')
                        self.tela_cadastro.lineEdit_2.setText('')
                        self.tela_cadastro.lineEdit_3.setText('')
                        self.tela_cadastro.lineEdit_4.setText('')
                        self.tela_cadastro.lineEdit_9.setText('')
                        self.QtStack.setCurrentIndex(0)
                    else:
                        QMessageBox.information(None, 'POOII', 'O CPF informado já esta cadastrado!')
                else:
                    QMessageBox.information(None, 'POOII', 'O Usuario informado já esta cadastrado!')
            else:
                QMessageBox.information(None, 'POOII', 'As senhas são diferentes, digite novamente!')
        else:
            QMessageBox.information(None, 'POOII', 'Todos os campos devem ser preenchidos!')

    def BotaoLogin(self):
        usuario = self.tela_login.lineEdit.text()
        senha = self.tela_login.lineEdit_2.text()
        if not(usuario == '' or senha == ''):
            client_socket.send(f'login,{usuario},{senha}'.encode())
            retorno = client_socket.recv(10240)
            retorno = eval(retorno)
            Main.objeto = retorno
            if (retorno != None):
                self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.information(None, 'POOII', 'Usuário ou senha incorreto!')
        else:
            QMessageBox.information(None, 'POOII', 'Todos os valores devem ser preenchidos!')

    def extrato_main(self):
        self.QtStack.setCurrentIndex(5)
        client_socket.send(f'extrato,{Main.objeto[0]}'.encode())
        extrato = client_socket.recv(10240)
        extrato = eval(extrato)
        extrato = '\n'.join(extrato)
        extrat = str(extrato)
        self.tela_extrato.textBrowser.setText(extrat)

    def deposita_main(self):
        valor = self.tela_deposita.lineEdit.text()
        if not(valor == ''):
            valorr = float(valor)
            saldo = Main.objeto[5] + valorr
            client_socket.send(f'deposita,{saldo},{Main.objeto[0]},{valorr}'.encode())
            client_socket.send(f'atualiza,{Main.objeto[0]}'.encode())
            retorno = client_socket.recv(10240)
            retorno = eval(retorno)
            Main.objeto = retorno
            QMessageBox.information(None, 'POOII', 'Valor depositado com sucesso!')
            self.tela_deposita.lineEdit.setText('')
            self.QtStack.setCurrentIndex(2)
        else:
            QMessageBox.information(None, 'POOII', 'Digite o valor a ser depositado!')

    def sacar_main(self):
        valor = self.tela_sacar.lineEdit.text()
        if not(valor == ''):
            valorr = float(valor)
            if(Main.objeto[5] >= valorr):
                saldo = Main.objeto[5] - valorr
                client_socket.send(f'sacar,{saldo},{Main.objeto[0]},{valorr}'.encode())
                client_socket.send(f'atualiza,{Main.objeto[0]}'.encode())
                retorno = client_socket.recv(10240)
                retorno = eval(retorno)
                Main.objeto = retorno
                QMessageBox.information(None, 'POOII', 'Valor sacado com sucesso!')
                self.tela_sacar.lineEdit.setText('')
                self.QtStack.setCurrentIndex(2)
            else:
                QMessageBox.information(None, 'POOII', 'Saldo insuficiente!')
        else:
            QMessageBox.information(None, 'POOII', 'Digite o valor a ser sacado!')

    def transferencia_main(self):
        valor = self.tela_transferencia.lineEdit.text()
        numero = self.tela_transferencia.lineEdit_2.text()
        if not(valor == '' or numero == ''):
            valorr = float(valor)
            numeroo = int(numero)
            client_socket.send(f'numero,{numeroo}'.encode())
            retorno = client_socket.recv(10240)
            retorno = eval(retorno)
            Main.objeto1 = retorno
            if(retorno != None):
                if (retorno[0] != Main.objeto[0]):
                    if (Main.objeto[5] >= valorr):
                        saldo = Main.objeto[5] - valorr
                        saldo1 = Main.objeto1[5] + valorr
                        client_socket.send(f'transferir,{saldo},{Main.objeto[0]},{saldo1},{Main.objeto1[0]},{valorr},{Main.objeto[1]},{Main.objeto1[1]}'.encode())
                        client_socket.send(f'atualiza,{Main.objeto[0]}'.encode())
                        retorno = client_socket.recv(10240)
                        retorno = eval(retorno)
                        Main.objeto = retorno
                        QMessageBox.information(None, 'POOII', 'Transferência realizada com sucesso!')
                        self.tela_transferencia.lineEdit.setText('')
                        self.tela_transferencia.lineEdit_2.setText('')
                        self.QtStack.setCurrentIndex(2)
                    else:
                        QMessageBox.information(None, 'POOII', 'Saldo insuficiente, impossivel realizar a transferencia!')
                else:
                    QMessageBox.information(None, 'POOII', 'Você não pode transferir um valor para você mesmo!')
            else:
                QMessageBox.information(None, 'POOII', 'Não existe uma conta com o numero informado!')
        else:
            QMessageBox.information(None, 'POOII', 'Todos os campos devem ser preenchidos!')

    def abrir_transferencia(self):
        client_socket.send(f'atualiza,{Main.objeto[0]}'.encode())
        retorno = client_socket.recv(10240)
        retorno = eval(retorno)
        Main.objeto = retorno
        self.QtStack.setCurrentIndex(7)

    def abrir_sacar(self):
        client_socket.send(f'atualiza,{Main.objeto[0]}'.encode())
        retorno = client_socket.recv(10240)
        retorno = eval(retorno)
        Main.objeto = retorno
        self.QtStack.setCurrentIndex(6)

    def abrir_deposita(self):
        client_socket.send(f'atualiza,{Main.objeto[0]}'.encode())
        retorno = client_socket.recv(10240)
        retorno = eval(retorno)
        Main.objeto = retorno
        self.QtStack.setCurrentIndex(4)

    def saldo_main(self):
        client_socket.send(f'atualiza,{Main.objeto[0]}'.encode())
        retorno = client_socket.recv(10240)
        retorno = eval(retorno)
        Main.objeto = retorno
        numero = str(Main.objeto[0])
        saldoo = str(Main.objeto[5])
        self.tela_saldo.lineEdit.setText(Main.objeto[1])
        self.tela_saldo.lineEdit_2.setText(Main.objeto[2])
        self.tela_saldo.lineEdit_3.setText(numero)
        self.tela_saldo.lineEdit_4.setText(saldoo)
        self.QtStack.setCurrentIndex(3)

    def abrirtelacadastro(self):
        self.QtStack.setCurrentIndex(1)

    def voltar(self):
        self.tela_cadastro.lineEdit.setText('')
        self.tela_cadastro.lineEdit_2.setText('')
        self.tela_cadastro.lineEdit_3.setText('')
        self.tela_cadastro.lineEdit_4.setText('')
        self.tela_cadastro.lineEdit_9.setText('')
        self.QtStack.setCurrentIndex(0)

    def voltar1(self):
        self.tela_login.lineEdit.setText('')
        self.tela_login.lineEdit_2.setText('')
        self.QtStack.setCurrentIndex(0)

    def voltar2(self):
        self.tela_deposita.lineEdit.setText('')
        self.tela_sacar.lineEdit.setText('')
        self.tela_transferencia.lineEdit.setText('')
        self.tela_transferencia.lineEdit_2.setText('')
        self.QtStack.setCurrentIndex(2)

if __name__ == '__main__':
    ip = 'localhost'
    port = 8001
    addr = ((ip, port))
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client_socket.connect(addr)
        app = QApplication(sys.argv)
        show_main = Main()
        sys.exit(app.exec_())
    except ConnectionRefusedError:
        print('Servidor indisponivel')
    except SystemExit:
        print('Desconectado.')
        client_socket.send('bye'.encode())
    finally:
        client_socket.close()

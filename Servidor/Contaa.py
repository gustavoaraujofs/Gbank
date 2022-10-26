import mysql.connector as mysql
from Historico import Historico

class Conta:

    __slots__ = ['conexao', 'cursor', 'sql', '_num', '_sal', '_tit', 'history']
    def __init__(self):
        self.history = Historico()
        self.conexao = mysql.connect(host="", db="", user="", passwd="")
        self.cursor = self.conexao.cursor()
        self.sql = """CREATE TABLE IF NOT EXISTS Contas (id integer AUTO_INCREMENT PRIMARY KEY,
        nome text NOT NULL, cpf text NOT NULL, usuario text NOT NULL, senha VARCHAR(32) NOT NULL,
        saldo float NOT NULL, transacoes text NOT NULL);"""

    def cadastrar(self, titular):
        existe = self.busca(titular.cpf)
        if (existe == None):
            self.cursor.execute(self.sql)
            self.cursor.execute('INSERT INTO Contas (nome, cpf, usuario, senha, saldo, transacoes) VALUES'
                            f'(%s, %s, %s, MD5(%s), {titular._sal}, "{self.history.data_abertura}")',
                        (titular._name, titular._cpf, titular._usuario, titular._senha))
            self.conexao.commit()
            return True
        else:
            return False

    def busca(self, cpf):
        self.cursor.execute(self.sql)
        self.cursor.execute(f'SELECT cpf from Contas WHERE cpf = "{cpf}"')
        for lp in self.cursor:
            return lp
        return None

    def login(self, usuario, senha):
        self.cursor.execute(self.sql)
        self.cursor.execute(f'SELECT * from Contas WHERE usuario = "{usuario}" and senha = MD5("{senha}")')
        for lg in self.cursor:
            return lg
        return None

    def usuario(self, usuario):
        self.cursor.execute(self.sql)
        self.cursor.execute(f'SELECT usuario from Contas WHERE usuario = "{usuario}"')
        for lu in self.cursor:
            return lu
        return None

    def numero_conta(self, numero):
        self.cursor.execute(self.sql)
        self.cursor.execute(f'SELECT * from Contas WHERE id = "{numero}"')
        for lu in self.cursor:
            return lu
        return None

    def atualiza(self, objeto):
        self.cursor.execute(f'SELECT * from Contas WHERE id = "{objeto}"')
        for i in self.cursor:
            return i

    @property
    def numeros(self):
        return self._num

    @numeros.setter
    def numeros(self, novo):
        self._num = novo

    @property
    def titularr(self):
        return self._tit

    @titularr.setter
    def titularr(self, novo):
        self._tit = novo


    def deposita(self, valor, objeto, valorr):
        self.cursor.execute(f'UPDATE Contas SET saldo = {valor} WHERE id = {objeto}')
        self.cursor.execute(f'UPDATE Contas SET transacoes = concat(transacoes, "\n{f"Deposito realizado no valor de {valorr} R$"}") WHERE id = {objeto}')
        self.conexao.commit()

    def sacar(self, valor, objeto, valorr):
        self.cursor.execute(f'UPDATE Contas SET saldo = {valor} WHERE id = {objeto}')
        self.cursor.execute(
            f'UPDATE Contas SET transacoes = concat(transacoes, "\n{f"Saque realizado no valor de {valorr} R$"}") WHERE id = {objeto}')
        self.conexao.commit()

    def extrato(self, numero):
        self.cursor.execute(f'SELECT transacoes from Contas WHERE id = {numero}')
        for i in self.cursor:
            return i

    def transfere(self, saldo, objeto, saldo1, objeto1, valorr, nome, nome1):
        self.cursor.execute(f'UPDATE Contas SET saldo = {saldo} WHERE id = {objeto}')
        self.cursor.execute(
            f'UPDATE Contas SET transacoes = concat(transacoes, "\n{f"Transferência realizada no valor de {valorr} R$, Para a conta de {nome1}"}") WHERE id = {objeto}')
        self.cursor.execute(f'UPDATE Contas SET saldo = {saldo1} WHERE id = {objeto1}')
        self.cursor.execute(
            f'UPDATE Contas SET transacoes = concat(transacoes, "\n{f"Transferência recebida no valor de {valorr} R$, da conta de {nome}"}") WHERE id = {objeto1}')
        self.conexao.commit()

usuarios = []
contas = list(range(100, 999))
conta_usuario = []
senhas = []
contas_corrente = []
contas_poupanca = []

class ContaCorrente:
    def __init__(self,nome,conta,senha, saldoCC, saldoCP):
        self.nome = nome
        self.conta = conta
        self.senha = senha
        self.__SaldoCC = saldoCC
        self.__SaldoCP = saldoCP

    def getSaldoCC(self):
        return self.__SaldoCC

    def setSaldoCC(self, SaldoCC):
        self.__SaldoCC = SaldoCC

    def getSaldoCP(self):
        return self.__SaldoCP

    def setSaldoCP(self, SaldoCP):
        self.__SaldoCP = SaldoCP

    def mostrar_dados(self, nome, conta, senha):
        if nome in usuarios and senha in senhas:
            index_usuario = usuarios.index(nome)
            index_senha = senhas.index(senha)
            if index_usuario == index_senha:
                print("+--------------------------------------------------+")
                print("Operação realizada com sucesso!")
                print("Nome: ", nome,
                      "\nConta: ", conta,
                      "\nsaldo C/C: R$", contaCorrente.getSaldoCC(),
                      "\nsaldo C/P: R$", contaCorrente.getSaldoCP())
                print("+--------------------------------------------------+")
            else:
                print("Senha inválida!")
        else:
            print("Entre com login e senha validos.")

    def deposito(self, nome, senha):
        if nome in usuarios and senha in senhas:
            index_usuario = usuarios.index(nome)
            index_senha = senhas.index(senha)
            if index_usuario == index_senha:
                tipo = int(input("deposito na C/C = 1 ou C/P = 2 ? "))
                if tipo == 1:
                    deposito = float(input("Qual o valor do deposito? R$"))
                    contaCorrente.setSaldoCC(deposito + contaCorrente.getSaldoCC())
                else:
                    deposito = float(input("Qual o valor do deposito? R$"))
                    contaCorrente.setSaldoCP(deposito + contaCorrente.getSaldoCP())
            else:
                print("Senha inválida!")
        else:
            print("Entre com login e senha validos.")

    def saque(self, nome, senha):
        if nome in usuarios and senha in senhas:
            index_usuario = usuarios.index(nome)
            index_senha = senhas.index(senha)
            if index_usuario == index_senha:
                tipo3 = int(input("Deseja sacar da C/C = 1 ou C/P = 2 ?"))
                valorSacar = float(input("digite o valor R$ "))
                if tipo3 == 1:
                    if valorSacar <= self.getSaldoCC():
                        contaCorrente.setSaldoCC(self.getSaldoCC() - valorSacar)
                    else:
                        print("Operação não realizada. Saldo insuficiente!")
                else:
                    if valorSacar <= self.getSaldoCP():
                        contaCorrente.setSaldoCP(self.getSaldoCP() - valorSacar)
                    else:
                        print("Operação não realizada. Saldo insuficiente!")
            else:
                print("Senha inválida!")
        else:
            print("Entre com login e senha validos.")

    def aplicacao(self, nome, senha):
        if nome in usuarios and senha in senhas:
            index_usuario = usuarios.index(nome)
            index_senha = senhas.index(senha)
            if index_usuario == index_senha:
                transfP = float(input("quanto deseja transferir? "))
                if transfP > self.getSaldoCC():
                    print("Operação não realizada. Saldo insuficiente!")
                else:
                    contaCorrente.setSaldoCC(self.getSaldoCC() - transfP)
                    contaCorrente.setSaldoCP(self.getSaldoCP() + transfP)
            else:
                print("Senha inválida!")
        else:
            print("Entre com login e senha validos.")


class ContaPoupanca(ContaCorrente):
    def __init__(self,nome,conta,senha, saldoCC, saldoCP):
        super().__init__(nome,conta,senha, saldoCC, saldoCP)
        index_usuario = usuarios.index(nome)
        self.__SaldoCC = contas_corrente[index_usuario]
        self.__SaldoCP = contas_poupanca[index_usuario]

    def resgate(self, nome, senha,saldoCC, saldoCP):
        if nome in usuarios and senha in senhas:
            index_usuario = usuarios.index(nome)
            index_senha = senhas.index(senha)
            if index_usuario == index_senha:
                transfC = float(input("quanto deseja transferir? "))
                if transfC > contaCorrente.getSaldoCP():
                    print("Operação não realizada. Saldo insuficiente!")
                else:
                    contaCorrente.setSaldoCP(contaCorrente.getSaldoCP() - transfC)
                    contaCorrente.getSaldoCP()
                    contaCorrente.setSaldoCC(contaCorrente.getSaldoCC() + transfC)
                    contaCorrente.getSaldoCP()
            else:
                print("Senha inválida!")
        else:
            print("Entre com login e senha validos.")



contaCorrente = ContaCorrente
cont = "SIM"
while cont == "SIM":
    print("✦" * 54)
    print("BANCO FUCTURA".center(69))
    print()
    print("➤Criar conta (1)".center(64))
    print("➤Seus Dados (2).".center(64))
    print("➤Deposito (3)".center(61))
    print("➤Saque (4)".center(58))
    print("➤Aplicação (5)".center(61))
    print("➤Resgate (6)".center(60))
    print("➤Sair (7)".center(58))
    print()
    print("✦" * 54)
    selecao = int(input("         Digite a opção desejada: "))
    print("✦" * 50)

    if selecao == 1:
        nome = input("digite seu nome: ")
        usuarios.append(nome)
        senha = input("crie sua senha com 4 digitos: ")
        conta = contas.pop(0)
        conta_usuario.append(conta)
        while len(list(senha)) != 4:
            print("senha invalida.")
            senha = input("digite uma senha com 4 digitos: ")

        else:
            conta_usuario.append(conta)
            senhas.append(senha)
            contas_corrente.append(0)
            contas_poupanca.append(0)
            index_usuario = usuarios.index(nome)
            saldoCC = contas_corrente[index_usuario]
            saldoCP = contas_poupanca[index_usuario]
            contaCorrente = ContaCorrente(nome, conta, senha, saldoCC,saldoCP)
            primeiro_deposito = int(input("Para ativar sua conta é necessario realizar um deposito, deseja realizar agora? sim(1) ou não(2)"))
            if primeiro_deposito == 1:
                contaCorrente.deposito(nome,senha)
                print("Parabéns, sua conta de numero ",conta, " está ativa!")
                contaCorrente.mostrar_dados(nome, conta, senha)
            else:
                print("volte logo!")
                break

    elif selecao == 2:
        nome = input("digite seu login: ")
        senha = input("digite sua senha: ")
        if nome not in usuarios or senha not in senhas:
            print("login ou senha invalidos.")

        else:
            index_conta = usuarios.index(nome)
            conta = conta_usuario[index_conta]
            saldoCC = contaCorrente.getSaldoCC()
            saldoCP = contaCorrente.getSaldoCP()
            contaCorrente.mostrar_dados(nome, conta, senha)

    elif selecao == 3:
        nome = input("digite seu login: ")
        senha = input("digite sua senha: ")
        if nome not in usuarios or senha not in senhas:
            print("login ou senha invalidos.")
        else:
            index_conta = usuarios.index(nome)
            conta = conta_usuario[index_conta]
            saldoCC = contaCorrente.getSaldoCC()
            saldoCP = contaCorrente.getSaldoCP()
            contaCorrente.deposito(nome, senha)
            contaCorrente.mostrar_dados(nome, conta, senha)

    elif selecao == 4:
        nome = input("digite seu login: ")
        senha = input("digite sua senha: ")
        if nome not in usuarios or senha not in senhas:
            print("login ou senha invalidos.")
        else:
            index_conta = usuarios.index(nome)
            conta = conta_usuario[index_conta]
            saldoCC = contaCorrente.getSaldoCC()
            saldoCP = contaCorrente.getSaldoCP()
            contaCorrente.saque(nome, senha)
            contaCorrente.mostrar_dados(nome, conta, senha)

    elif selecao == 5:
        nome = input("digite seu login: ")
        senha = input("digite sua senha: ")
        if nome not in usuarios or senha not in senhas:
            print("login ou senha invalidos.")
        else:
            index_conta = usuarios.index(nome)
            conta = conta_usuario[index_conta]
            contaCorrente.aplicacao(nome, senha)
            contaCorrente.mostrar_dados(nome, conta, senha)

    elif selecao == 6:
        nome = input("digite seu login: ")
        senha = input("digite sua senha: ")
        if nome not in usuarios or senha not in senhas:
            print("login ou senha invalidos.")
        else:
            index_conta = usuarios.index(nome)
            conta = conta_usuario[index_conta]
            saldoCC = contaCorrente.getSaldoCC()
            saldoCP = contaCorrente.getSaldoCP()
            resgatar = ContaPoupanca(nome,conta, senha,saldoCC, saldoCP)
            resgatar.resgate(nome, senha,saldoCC, saldoCP)
            resgatar.mostrar_dados(nome, conta, senha)

    else:
        print("volte sempre!")
        break


contas = list(range(100, 999))
usuarios = []
conta_usuario = []
senhas = []
contas_corrente = []
contas_poupanca = []

class ContaCorrente:
    def __init__(self,nome,conta,senha, saldoCC):
        self.nome = nome
        self.conta = conta
        self.senha = senha
        self.__SaldoCC = saldoCC

    def getSaldoCC(self):
        return self.__SaldoCC

    def setSaldoCC(self, SaldoCC):
        self.__SaldoCC = SaldoCC

    def mostrar_dados(self,usuario,conta):
        print("+--------------------------------------------------+")
        print("Nome: ", usuario,
                "\nConta: ", conta,
                "\nsaldo C/C: R$", contas_corrente[index_usuario],
                "\nsaldo C/P: R$", contas_poupanca[index_usuario])
        print("+--------------------------------------------------+")

    def deposito(self,nCnta,saldoCC):
        contaCorrente.setSaldoCC(contaCorrente.getSaldoCC() + saldoCC)
        contas_corrente[nCnta] = contaCorrente.getSaldoCC()
        print("Operação realizada com sucesso!")

    def saque(self,nCnta,valorSacar):
        if valorSacar <= contaCorrente.getSaldoCC():
            contaCorrente.setSaldoCC(contaCorrente.getSaldoCC() - valorSacar)
            contas_corrente[nCnta] = contaCorrente.getSaldoCC()
            print("Operação realizada com sucesso!")
        else:
            print("Operação não realizada. Saldo insuficiente!")

    def aplicacao(self,nConta,transfP):
        if transfP > contaCorrente.getSaldoCC():
            print("Operação não realizada. Saldo insuficiente!")
        else:
            contaCorrente.setSaldoCC(contaCorrente.getSaldoCC() - transfP)
            contaPoupanca.setSaldoCP(contaPoupanca.getSaldoCP() + transfP)
            contas_corrente[nConta] = contaCorrente.getSaldoCC()
            contas_poupanca[nConta] = contaPoupanca.getSaldoCP()
            print("Operação realizada com sucesso!")

class ContaPoupanca(ContaCorrente):
    def __init__(self, nome, conta, senha, saldoCC,saldoCP):
        super().__init__(nome, conta, senha, saldoCC)
        self.__SaldoCP = saldoCP

    def getSaldoCP(self):
        return self.__SaldoCP

    def setSaldoCP(self, SaldoCP):
        self.__SaldoCP = SaldoCP

    def resgate(self,nConta,transfC):
        if transfC > contaPoupanca.getSaldoCP():
            print("Operação não realizada. Saldo insuficiente!")
        else:
            contaPoupanca.setSaldoCP(contaPoupanca.getSaldoCP() - transfC)
            contaCorrente.setSaldoCC(contaCorrente.getSaldoCC() + transfC)
            contas_corrente[nConta] = contaCorrente.getSaldoCC()
            contas_poupanca[nConta] = contaPoupanca.getSaldoCP()
            print("Operação realizada com sucesso!")

contaCorrente = ContaCorrente
contaPoupanca = ContaPoupanca

app = "SIM"
while app == "SIM":
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
        usuario = input("Nome do titular: ")
        senhaUsuario = input("Crie sua senha com 4 digitos: :")
        while usuario in usuarios or senhaUsuario in senhas:
            print("digite um usuario e senha validos.")
            usuario = input("digite seu nome: ")
            senhaUsuario = input("crie sua senha com 4 digitos: ")
        else:
            while len(list(senhaUsuario)) != 4:
                print("senha invalida.")
                senhaUsuario = input("digite uma senha com 4 digitos: ")
            else:
                usuarios.append(usuario)
                senhas.append(senhaUsuario)
                conta = contas.pop(0)
                conta_usuario.append(conta)
                contas_corrente.append(0)
                contas_poupanca.append(0)
                index_usuario = usuarios.index(usuario)
                saldoCC = contas_corrente[index_usuario]
                saldoCP = contas_poupanca[index_usuario]
                contaCorrente = ContaCorrente(usuario,conta,senhaUsuario,saldoCC)
                ativarConta = int(input("Sua conta está em análise. \nPara ativar sua conta, realize um deposito."
                                        "\nDeseja realizar agora? sim(1) / não(2). "))
                if ativarConta == 1:
                    saldoCC = float(input("Qual o valor do deposito? R$"))
                    contaCorrente.deposito(index_usuario,saldoCC)
                    print("Bem vindo ao Bando Fuctura!\nSua conta de número ", conta, " foi ativada.")
                else:
                    print("Volte logo!")
                    break

    elif selecao == 2:
        usuario = input("Nome do titular: ")
        senhaUsuario = input("Digite sua senha: ")
        cont = 0
        while cont < 2 and senhaUsuario not in senhas:
            print("Senha ou login inválidos!")
            print("Você tem mais ",2 - cont," chances.")
            usuario = input("Nome do titular: ")
            senhaUsuario = input("Digite sua senha: ")
            cont += 1

        else:
            index_usuario = usuarios.index(usuario)
            conta = conta_usuario[index_usuario]
            contaCorrente.mostrar_dados(usuario, conta)

    elif selecao == 3:
        usuario = input("Nome do titular: ")
        senhaUsuario = input("Digite sua senha: ")
        cont = 0
        while cont < 2 and senhaUsuario not in senhas:
            print("Senha ou login inválidos!")
            print("Você tem mais ", 2 - cont, " chances.")
            usuario = input("Nome do titular: ")
            senhaUsuario = input("Digite sua senha: ")
            cont += 1
        else:
            indice = usuarios.index(usuario)
            saldoCC = float(input("Qual o valor do deposito? R$"))
            contaCorrente.deposito(indice,saldoCC)

    elif selecao == 4 :
        usuario = input("Nome do titular: ")
        senhaUsuario = input("Digite sua senha: ")
        cont = 0
        while cont < 2 and senhaUsuario not in senhas:
            print("Senha ou login inválidos!")
            print("Você tem mais ", 2 - cont, " chances.")
            usuario = input("Nome do titular: ")
            senhaUsuario = input("Digite sua senha: ")
            cont += 1
        else:
            valorSacar = float(input("digite o valor R$ "))
            indice = usuarios.index(usuario)
            contaCorrente.saque(indice,valorSacar)

    elif selecao == 5:
        usuario = input("Nome do titular: ")
        senhaUsuario = input("Digite sua senha: ")
        cont = 0
        while cont < 2 and senhaUsuario not in senhas:
            print("Senha ou login inválidos!")
            print("Você tem mais ", 2 - cont, " chances.")
            usuario = input("Nome do titular: ")
            senhaUsuario = input("Digite sua senha: ")
            cont += 1
        else:
            index_usuario = usuarios.index(usuario)
            usuario = usuarios[index_usuario]
            index_conta = usuarios.index(usuario)
            conta = conta_usuario[index_usuario]
            saldoCC = contas_corrente[index_usuario]
            saldoCP = contas_poupanca[index_usuario]
            indice = usuarios.index(usuario)
            transfP = float(input("quanto deseja transferir? "))
            contaPoupanca = ContaPoupanca(usuario, conta, senhaUsuario, saldoCC, saldoCP)
            contaCorrente.aplicacao(indice,transfP)

    elif selecao == 6:
        usuario = input("Nome do titular: ")
        senhaUsuario = input("Digite sua senha: ")
        cont = 0
        while cont < 2 and senhaUsuario not in senhas:
            print("Senha ou login inválidos!")
            print("Você tem mais ", 2 - cont, " chances.")
            usuario = input("Nome do titular: ")
            senhaUsuario = input("Digite sua senha: ")
            cont += 1
        else:
            index_usuario = usuarios.index(usuario)
            usuario = usuarios[index_usuario]
            index_conta = usuarios.index(usuario)
            conta = conta_usuario[index_usuario]
            saldoCC = contas_corrente[index_usuario]
            saldoCP = contas_poupanca[index_usuario]
            indice = usuarios.index(usuario)
            transfC = float(input("quanto deseja transferir? "))
            contaPoupanca = ContaPoupanca(usuario, conta, senhaUsuario, saldoCC,saldoCP)
            contaPoupanca.resgate(indice,transfC)
    else:
        print("Volte logo!")
        break
else: pass



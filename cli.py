from passageiro import Passageiro
from corridas import Corrida
from motorista import Motorista


class SimpleCLI:
    def __init__(self):
        self.commands = {}

    def add_command(self, name, function):
        self.commands[name] = function

    def run(self):
        while True:
            command = input("Enter a command: ")
            if command == "quit":
                print("Goodbye!")
                break
            elif command in self.commands:
                self.commands[command]()
            else:
                print("Invalid command. Try again.")


class MotoristaCLI(SimpleCLI):
    def __init__(self, motorista_model):
        super().__init__()
        self.motorista_model = motorista_model
        self.add_command("create", self.create_motorista)
        self.add_command("read", self.read_motorista)
        self.add_command("update", self.update_motorista)
        self.add_command("delete", self.delete_motorista)

    def create_motorista(self):
        # Criar Passageiro
        nome_passageiro = input("Entre com o nome do passageiro: ")
        documento_passageiro = input("Entre com o documento do passageiro: ")
        passageiro = Passageiro(nome=nome_passageiro, documento=documento_passageiro)

        # Criar Corridas
        corridas = []
        while True:
            print("Criando nova corrida:")
            nota_corrida = float(input("Entre com a nota da corrida: "))
            distancia = float(input("Entre com a distância percorrida (em km): "))
            valor = float(input("Entre com o valor da corrida: "))
            corrida = Corrida(nota=nota_corrida, distancia=distancia, valor=valor, passageiro=passageiro)
            corridas.append(corrida)

            adicionar_mais = input("Deseja adicionar outra corrida? (s/n): ")
            if adicionar_mais.lower() != 's':
                break

        # Criar Motorista
        nota_motorista = float(input("Entre com a nota do motorista: "))
        motorista = Motorista(nota=nota_motorista)

        # Associar as corridas ao motorista
        for corrida in corridas:
            motorista.adicionar_corrida(corrida)

        # Salvar no banco de dados
        self.motorista_model.create_motorista(motorista)

    def read_motorista(self):
        id = input("Entre com o ID do motorista: ")
        motorista = self.motorista_model.read_motorista(id)
        if motorista:
            print(f"Nota do Motorista: {motorista['nota']}")
            print("Corridas:")
            for corrida in motorista['corridas']:
                print(f"  Nota da Corrida: {corrida['nota']}")
                print(f"  Distância: {corrida['distancia']}")
                print(f"  Valor: {corrida['valor']}")
                passageiro = corrida['passageiro']
                print(f"  Passageiro: {passageiro['nome']} - Documento: {passageiro['documento']}")

    def update_motorista(self):
        id = input("Entre com o ID do motorista: ")
        nota = float(input("Entre com a nova nota do motorista: "))
        self.motorista_model.update_motorista(id, nota)

    def delete_motorista(self):
        id = input("Entre com o ID do motorista: ")
        self.motorista_model.delete_motorista(id)

    def run(self):
        print("Bem-vindo ao sistema de gerenciamento de motoristas!")
        print("Comandos disponíveis: create, read, update, delete, quit")
        super().run()

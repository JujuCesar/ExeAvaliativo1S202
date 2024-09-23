from pymongo import MongoClient
from bson.objectid import ObjectId
from motorista import Motorista  # Importar a classe Motorista que criamos

class MotoristaDAO:
    def __init__(self, database):
        self.db = database

    def create_motorista(self, motorista):
        try:
            # Converter objeto Motorista em um dicionário
            motorista_dict = {
                "nota": motorista.nota,
                "corridas": [
                    {
                        "nota": corrida.nota,
                        "distancia": corrida.distancia,
                        "valor": corrida.valor,
                        "passageiro": {
                            "nome": corrida.passageiro.nome,
                            "documento": corrida.passageiro.documento
                        }
                    }
                    for corrida in motorista.corridas
                ]
            }
            res = self.db.collection.insert_one(motorista_dict)
            print(f"Motorista criado com ID: {res.inserted_id}")
            return res.inserted_id
        except Exception as e:
            print(f"Ocorreu um erro ao criar o motorista: {e}")
            return None

    def read_motorista(self, id):
        try:
            res = self.db.collection.find_one({"_id": ObjectId(id)})
            if res:
                print("Motorista encontrado!")
            else:
                print("Motorista não encontrado.")
            return res
        except Exception as e:
            print(f"Ocorreu um erro ao ler o motorista: {e}")
            return None

    def update_motorista(self, id: str, nota: float):
        try:
            res = self.db.collection.update_one({"_id": ObjectId(id)}, {"$set": {"nota": nota}})
            print(f"Motorista atualizado: {res.modified_count} documento(s) modificado(s)")
            return res.modified_count
        except Exception as e:
            print(f"Ocorreu um erro ao atualizar o motorista: {e}")
            return None

    def delete_motorista(self, id):
        try:
            res = self.db.collection.delete_one({"_id": ObjectId(id)})
            print(f"Motorista deletado: {res.deleted_count} documento(s) deletado(s).")
            return res.deleted_count
        except Exception as e:
            print(f"Ocorreu um erro ao deletar o motorista: {e}")
            return None

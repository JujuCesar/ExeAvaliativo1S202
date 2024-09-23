from typing import Collection
import pymongo # pip install pymongo


class Database:
    def __init__(self, database, collection):
        self.connect(database, collection)

    def connect(self, database, collection):
        try:
            connectionString = "mongodb+srv://jucrr2:Sorvetefeitonodia@exeavaliativojuliocesar.zuwy1.mongodb.net/"
            self.clusterConnection = pymongo.MongoClient(
                connectionString,
                tlsAllowInvalidCertificates=True
            )
            self.db = self.clusterConnection[database]
            self.collection = self.db[collection]
            print("Conectado ao banco de dados com sucesso!")
        except Exception as e:
            print(e)

    def resetDatabase(self):
        try:
            self.db.drop_collection(self.collection)
            print("Banco de dados resetado com sucesso!")
        except Exception as e:
            print(e)

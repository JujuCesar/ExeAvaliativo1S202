from database import Database
from motoristaDAO import MotoristaDAO
from cli import SimpleCLI, MotoristaCLI

db = Database(database="atlas-cluster", collection="usuarios")
motoristaModel = MotoristaDAO(database=db)


# Rodar o CLI para operação com Motoristas
cli = MotoristaCLI(motoristaModel)
cli.run()

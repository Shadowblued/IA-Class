"""from faker import Faker
pearson = Faker('pt-BR')
for _ in range(5):
    print(pearson.name())
    print(pearson.address(), pearson.date_of_birth(), '\n')"""

from faker import Faker

listaDeNomes = []
pearson = Faker('pt-BR')
for _ in range(100):
    listaDeNomes.append(pearson.name())
print(listaDeNomes, '\n')
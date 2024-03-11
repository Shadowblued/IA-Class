from faker import Faker

listaDeNomes = []
pearson = Faker('pt-BR')
for _ in range(100):
    listaDeNomes = pearson.name()
    print(pearson.address(), pearson.date_of_birth(), '\n')
from faker import Faker

listaDeNomes = []
pearson = Faker('pt-BR')
for _ in range(100):
    listaDeNomes.extend([pearson.name(), pearson.address(), pearson.date_of_birth()])
print(listaDeNomes)
    
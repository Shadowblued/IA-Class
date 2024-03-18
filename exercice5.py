from faker import Faker
lista = []
person = Faker('pt-BR')
for __ in range(100):
    lista.append([person.name(), person.address(), person.date_of_birth()])

for item in lista:
    print(item)
from faker import Faker
dic = {}
person = Faker('pt-BR')
for __ in range(100):
    dic[person.name()] = (person.address(), person.date_of_birth())

#print(dic)
for chave, item in dic.items():
    print(chave, item)
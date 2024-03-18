from faker import Faker
import datetime

dic = {}
person = Faker('pt-BR')
for _ in range(5):
    dob = person.date_of_birth(minimum_age=18, maximum_age=90)
    age = datetime.date.today().year - dob.year
    dic[person.name()] = (person.address(), age)

for chave, item in dic.items():
    print(chave, item)
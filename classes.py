# criando classes
from dataclasses import dataclass, asdict
import json

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f'{self.nome}, {self.idade}'

uma_pessoa = Pessoa("Carlos", 27)
print(uma_pessoa)

outra_pessoa_dict = { 'nome': 'Jose', 'idade': 15}
print(outra_pessoa_dict)

outra_pessoa = Pessoa(*outra_pessoa_dict.values())
print(outra_pessoa)

uma_outra_pessoa = Pessoa(**{"nome": 'Jacó', 'idade': '100'})
print(uma_outra_pessoa)

# melhor usar assim:
@dataclass
class Animal:
    nome: str
    idade: int

animal = Animal(**{"nome": "Juninho", "idade": 5})
print(animal)

animal_json = '{"nome": "keke", "idade": 1}'

animal_dict = json.loads(animal_json)
print(animal_dict)

uma_keke = Animal(**animal_dict)
print(uma_keke)

uma_keke_json = json.dumps(asdict(uma_keke))
print(uma_keke_json)
from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p1.outro_metodo()
p1.comer('maçã')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('Banana')
p1.parar_falar()
p1.comer('Banana')

p2 = Pessoa('João', 32)
p2.comer('Lichia')

print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())
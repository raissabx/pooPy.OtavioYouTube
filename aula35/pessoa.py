from datetime import datetime
# Criação da classe pessoa.
# A função falar é um MÉTODO da classe Pessoa.
# Classe é como fosse um molde.

#class Pessoa:
#	def falar(self):
#		print('Pessoa está falando...')

#-------------------------------------------------------------------------

# INSTANCIAR um objeto é criar um objeto a partir de uma classe.
# Criar as pessoas p1 e p2 com o molde da class Pessoa.

#p1 = Pessoa()
#p2 = Pessoa()

# Criar uma variável para a instância p1.
# Esta variável da instância p1 é chamada de ATRIBUTO da classe.
# Esta forma de criação de atributo não é a mais usual.

#p1.nome = 'Luiz'


# Apesar de terem o mesmo nome, os parâmetro do construtor e as variáveis self.xxx, não são a mesma coisa.

class Pessoa:

#A variavel ano_atual é diferente das variávels das instancias. Ela é uma variável da classe!
	ano_atual = int(datetime.strftime(datetime.now(),'%Y'))

	def __init__(self, nome, idade, comendo=False, falando=False):
		self.nome = nome # A variável self.nome recebe o valor do parâmetro nome.
		self.idade = idade #O mesmo acontece com os outros self.xxx e os parâmetros.
		self.comendo = comendo
		self.falando = falando

# Esta variável é uma variável local apenas do construtor, caso haja outro método, esta varável não irá funcionar para o outro método.

		#variavel = 'Valor'
		#print(variavel)

# As variáveis self.xxx ela são variáveis globais dentro da classe.

	def outro_metodo(self):
		print(self.nome)

	def comer(self, alimento):
		if self.comendo:
			print(f'{self.nome} já está comendo.')
			return

		if self.falando:
			print(f'{self.nome} não pode comer falando.')
			return

		print(f'{self.nome} está comendo {alimento}.')
		self.comendo = True
	
	def falar(self, assunto):
		if self.comendo:
			print(f'{self.nome} não pode falar comendo.')
			return

		if self.falando:
			print(f'{self.nome} já está falando.')
			return

		print(f'{self.nome} está falando sobre {assunto}')
		self.falando = True
	

	def parar_comer(self):
		if not self.comendo:
			print(f'{self.nome} não está comendo.')
			return

		print(f'{self.nome} parou de comer.')
		self.comendo = False

	
	def parar_falar(self):
		if not self.falando:
			print(f'{self.nome} não está falando.')
			return
		
		print(f'{self.nome} parou de falar.')
		self.falando = False

	def get_ano_nascimento(self):
		return self.ano_atual - self.idade
		
# class Pokemon:
# 	def __init__(self, owner, name, skills):
# 		self.owner = owner
# 		self.name = name
# 		self.skills = skills.split('/')
#
# 	def info(self):
# 		print(f'{self.owner}의 포켓몬은 {self.name}')
# 		skill_list = []
# 		for i in range(len(self.skills)):
# 			print(f'{i+1}: {self.skills[i]}')
#
# 	def attack(self, idx):
# 		print(f'{self.skills[idx]} 공격 시전!')
#
# class Ggoboogi(Pokemon):
# 	def __init__ (self, owner, skills):
# 		super().__init__(owner, skills)
# 		self.name = "꼬부기"
# 		print(f"self.name")
#
# P1 = Pokemon('한지우', '피카츄', '50만 볼트/100만 볼트/번개')
# P1.info()
# P1.attack(1)

class Duck():
	def __init__(self, input_name):
		self.hidden_name = input_name

	def get_name(self):
		print('inside the getter')
		return self.hidden_name

	def set_name(self, input_name):
		print('inside the setter')
		self.hidden_name = input_name
	name = property(get_name, set_name)

don = Duck('Donald')
print(don.get_name())

class player():
	def __init__(self):
		self.MaxHp = 10
		self.Hp = self.MaxHp
		self.name = ""
		
	def self_name(self):
		self.name = raw_input("Enter your name...")
		if self.name == "":
			self.self_name()
	
	def hp_max_total(self):
		if self.Hp > self.MaxHp:
			self.Hp = self.MaxHp
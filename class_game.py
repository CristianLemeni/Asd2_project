class Game:
	def __init__(self):
		self.command_list = ["look","name","fight","heal",'report','move','?']
		self.player = Player()
		self.current_room = Room("home")
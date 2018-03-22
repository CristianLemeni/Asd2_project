class Game:
	def __init__(self):
		self.command_list = ["name"]
		self.player = Player()
		self.current_room = Room("home")

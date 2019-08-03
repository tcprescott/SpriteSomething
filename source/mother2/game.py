import importlib
from ..gamelib import GameParent

class Game(GameParent):
	def __init__(self):
		super().__init__()
		#FIXME: Do we want to translate the game's display name?
		self.name = "EarthBound"    #to be replaced by a name like "Super Metroid"
		self.internal_name = "mother2"        #to be replaced by the specific folder name that this app uses, e.g. "metroid3"
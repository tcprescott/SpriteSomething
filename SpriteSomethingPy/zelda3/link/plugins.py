import json
import os
from tkinter import messagebox
from functools import partial
from SpriteSomethingPy import common
from SpriteSomethingPy import gui_common
from SpriteSomethingPy.pluginslib import PluginsParent
from . import equipment

#FIXME: English

class Plugins(PluginsParent):
	def __init__(self):
		super().__init__()
		plugins = [
			("Download ALttPR Official Sprites",None,self.get_alttpr_sprites),
			("Download SpriteSomething Unofficial Sprites",None,self.get_spritesomething_sprites),
			("Sheet Trawler",None,None)#
			#("Equipment",None,self.equipment_test)
		]
		self.set_plugins(plugins)

	def equipment_test(self, save=False):
		return equipment.equipment_test(save)

	def get_alttpr_sprites(self):
		success = gui_common.get_sprites(
			self,
			"Official ALttPR",
			"zelda3/link/sheets/official",
			"http://alttpr.com/sprites"
		)
		return success

	def get_spritesomething_sprites(self):
		success = gui_common.get_sprites(
			self,
			"Unofficial SpriteSomething Link",
			"zelda3/link/sheets/unofficial",
			"https://raw.githubusercontent.com/Artheau/SpriteSomething/gh-pages/app_resources/zelda3/link/sprites.json"
		)
		return success

from source.spritelib import SpriteParent
from source import common

class Sprite(SpriteParent):
	def __init__(self, filename, manifest_dict, my_subpath):
		super().__init__(filename, manifest_dict, my_subpath)
		self.use_palettes = False

	def import_from_ROM(self, rom):
		pass

	def import_from_binary_data(self,pixel_data,palette_data):
		pass

	def inject_into_ROM(self, rom):
		pass

	def get_rdc_export_blocks(self):
		pass

	def get_palette(self, palettes, default_range, frame_number):
		pass

	def get_alternative_direction(self, animation, direction):
		#suggest an alternative direction, which can be referenced if the original direction doesn't have an animation
		split_string = direction.split("_aim_")
		facing = split_string[0]
		aiming = split_string[1] if len(split_string) > 1 else ""

		if not aiming == "" and not aiming == "neutral":
			return aiming
		if not facing == "":
			return facing
		return "right"

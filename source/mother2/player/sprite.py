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
		direction_dict = self.animations[animation]
		split_string = direction.split("_aim_")
		facing = split_string[0]
		aiming = split_string[1] if len(split_string) > 1 else ""

		#now start searching for this facing and aiming in the JSON dict
		#start going down the list of alternative aiming if a pose does not have the original
		ALTERNATIVES = {
			"diag_up": "ne",
			"diag_down": "se"
		}
		while(self.concatenate_facing_and_aiming(facing,aiming) not in direction_dict):
			if aiming in ALTERNATIVES:
				aiming = ALTERNATIVES[aiming]
			elif facing in direction_dict:   #no aim was available, try the pure facing
				return facing
			else:    #now we are really screwed, so just do anything
				return next(iter(direction_dict.keys()))

		#if things went well, we are here
		return "_aim_".join([facing,aiming])

	def concatenate_facing_and_aiming(self, facing, aiming):
		return "_aim_".join([facing,aiming])

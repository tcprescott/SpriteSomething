#includes routines that load the rom and apply bugfixes
#inherits from the generic romhandler

if __name__ == "__main__":
	raise AssertionError(f"Called main() on utility library {__file__}")

import enum
from source.romhandler import RomHandlerParent

class RomHandler(RomHandlerParent):
	def __init__(self, filename):
		super().__init__(filename)      #do the usual stuff

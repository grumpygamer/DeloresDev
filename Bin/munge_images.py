#!/usr/bin/python

import os
import sys
import string
import subprocess
from sys import exit
import json
from optparse import OptionParser

def mungeImages(game_root, options):

	TEXTURE_PACKER_CMD=os.environ.get("TEXTURE_PACKER_CMD", False)
	if TEXTURE_PACKER_CMD == False:
		if sys.platform == "darwin": TEXTURE_PACKER_CMD="/Applications/TexturePacker.app/Contents/MacOS/TexturePacker"
		if sys.platform == "win32": TEXTURE_PACKER_CMD=False

	if not os.path.isfile(TEXTURE_PACKER_CMD):
		print ("Environment var TEXTURE_PACKER_CMD needs to be set and point to TextturePacker commandline executable")
		exit(1)

	max_size = "4096"
	sheet_folder=game_root+"/SpriteSheets"
	image_dir=game_root+"/Images/"
	for filename in os.listdir(image_dir):
		png_folder=image_dir+filename
		if not os.path.isdir(png_folder):
			continue
		if png_folder.startswith("_"):
			continue

		json_file=sheet_folder+"/"+filename+".json"
		png_file=sheet_folder+"/"+filename+".png"

		if options.force:
			try:
				os.remove(png_file)
			except:
				pass

		if options.quiet:
			subprocess.call([TEXTURE_PACKER_CMD, png_folder,
				"--sheet", png_file,
				"--data", json_file,
				"--max-size", max_size,
				"--png-opt-level", "0",
				"--trim-sprite-names",
				"--allow-free-size",
				"--format", "json",
				"--algorithm", "MaxRects",
				"--disable-rotation",
				"--padding", "2",
				"--quiet"])
		else:
			print("Processing "+filename)
			subprocess.call([TEXTURE_PACKER_CMD, png_folder,
				"--sheet", png_file,
				"--data", json_file,
				"--max-size", max_size,
				"--png-opt-level", "0",
				"--trim-sprite-names",
				"--allow-free-size",
				"--format", "json",
				"--algorithm", "MaxRects",
				"--disable-rotation",
				"--padding", "2"])

def main(args):
	parser = OptionParser(usage="%prog [options]")
	parser.add_option("--force", action="store_true", dest="force", default=False, help="Force writing of files.")
	parser.add_option("--quiet", action="store_true", dest="quiet", default=False, help="No output.")
	(options, args) = parser.parse_args(args)

	GAME_ROOT=os.getenv("DELORES_GAMEROOT", None)
	if GAME_ROOT == None or not os.path.isdir(GAME_ROOT):
		print ("Environment variable DELORES_GAMEROOT is not set or not set to a valid directory.")
		exit(1)

	mungeImages(GAME_ROOT, options)

if __name__ == '__main__':
    main(sys.argv[1:])


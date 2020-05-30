#!/usr/bin/python

import os
import sys
import string
import subprocess
from sys import exit
from optparse import OptionParser
from slice_psd import slicePSD
from munge_images import mungeImages

def touch(fname, times=None):
	with open(fname, 'a'):
		os.utime(fname, times)

GAME_ROOT=os.getenv("DELORES_GAMEROOT", None)
if GAME_ROOT == None or not os.path.isdir(GAME_ROOT):
	print ("Environment variable DELORES_GAMEROOT is not set or not set to a valid directory.")
	exit(1)

ART_ROOT=GAME_ROOT+"/Source"
if not os.path.isdir(ART_ROOT):
	print ("Directory "+ART_ROOT+" is not a valid directory.")
	exit(1)

parser = OptionParser(usage="%prog [options] [folder]")
parser.add_option("--force", action="store_true", dest="force", default=False, help="Force writing of files.")
parser.add_option("--verbose", action="store_true", dest="verbose", default=False, help="Verbose output.")
parser.add_option("--quiet", action="store_true", dest="quiet", default=False, help="No output.")
parser.add_option("--notouch", action="store_true", dest="no_touch", default=False, help="No updating file dates.")
(options, args) = parser.parse_args()

touch_folder = GAME_ROOT+"/.timestamps_psd/"
try:
	os.mkdir(touch_folder)
except:
	pass

try:
	os.remove(touch_folder+args[0])
except:
	pass

psd_folders = [ ART_ROOT+"/Rooms/", ART_ROOT+"/Misc/", ART_ROOT+"/Animation/" ]
images_folder = GAME_ROOT+"/Images/"

if not os.path.exists(images_folder):
	os.mkdir(images_folder)

sliced = False
for psd_folder in psd_folders:
	for root, dirs, files in os.walk(psd_folder):
		for filename in files:
			if filename.startswith("_") or filename.startswith("-"):
				continue
			filename = root+filename
			if filename.endswith(".psd"):
				basename = os.path.splitext(os.path.basename(filename))[0]
				if not options.force and os.path.exists(touch_folder+basename) and os.path.exists(images_folder+"/"+basename) and (os.path.getmtime(touch_folder+basename) > os.path.getmtime(filename)):
					continue
				try:
					os.mkdir(images_folder+"/"+basename)
				except:
					pass
				sliced=True
				exit_code=0
				cmd_options=[]
				print("Slicing "+filename)
				options.image_folder = images_folder+"/"+basename
				if slicePSD(filename, options) == False:
					sys.exit(1)

				if options.no_touch == False:
					touch(touch_folder+basename)

if not os.path.isdir(GAME_ROOT+"/SpriteSheets"):
	sliced = True

if sliced:
	print("Munging images...")
	if mungeImages(GAME_ROOT, options) == False:
		sys.exit(1)
else:
	if not options.quiet:
		print("Nothing to process.")

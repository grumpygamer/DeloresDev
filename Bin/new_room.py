#!/usr/bin/python

# -----------------------------------------------------------------------------
# Set up a new room by writing all the template files.

import os
import sys
import tempfile
import shutil
import string
from os import path
from sys import exit
from  shutil import copyfile
from optparse import OptionParser

parser = OptionParser(usage="%prog [options] RoomName|Folder/RoomName")
parser.add_option("--force", action="store_true", dest="force", default=False, help="Force writing of files.")
(options, args) = parser.parse_args()

GAME_ROOT=""
try:
	GAME_ROOT=os.environ["DELORES_GAMEROOT"]+"/"
except:
	print("Environment variable DELORES_GAMEROOT not set.")
	exit(1)

DATADIR=GAME_ROOT+"/Wimpy"
CODEDIR=GAME_ROOT+"/Scripts"
IMAGEDIR=GAME_ROOT+"/Images"
TEMPLATEDIR=GAME_ROOT+"/Templates"

if not path.isfile(TEMPLATEDIR+"/ROOMNAME.dinky") or not path.isfile(TEMPLATEDIR+"/ROOMNAME.wimpy"):
	print("Can't find Template files in "+TEMPLATEDIR)
	exit(1)

if len(args) != 1:
	parser.print_help()
	exit(1)

temp=args[0].split("/")
if temp == None or len(temp) == 1:
	ROOMPATH=""
	ROOMNAME=args[0]
elif len(temp) == 2:
	ROOMPATH=""+temp[0]
	ROOMNAME=temp[1]
else:
	print "RoomName must be RoomName | Folder/RoomName"
	exit(1)

if ROOMPATH != "":
	if not path.isdir(CODEDIR+"/Rooms/"+ROOMPATH):
		print "Folder "+CODEDIR+"/Rooms/"+ROOMPATH+" does not exist."
		exit(1)
	if not path.isdir(DATADIR+"/"+ROOMPATH):
		print "Folder "+DATADIR+"/"+ROOMPATH+" does not exist."
		exit(1)
	ROOMNAME_DINKY=CODEDIR+"/Rooms/"+ROOMPATH+"/"+ROOMNAME+".dinky"
	ROOMNAME_WIMPY=DATADIR+"/"+ROOMPATH+"/"+ROOMNAME+".wimpy"
else:
	ROOMNAME_DINKY=CODEDIR+"/Rooms/"+ROOMNAME+".dinky"
	ROOMNAME_WIMPY=DATADIR+"/"+ROOMNAME+".wimpy"

TEMPLATE_DINKY=TEMPLATEDIR+"/ROOMNAME.dinky"
TEMPLATE_WIMPY=TEMPLATEDIR+"/ROOMNAME.wimpy"
DEFINE_ROOMS=CODEDIR+"/Defines/DefineRooms.dinky"

dinky_exists = False
wimpy_exists = False

if path.isfile(ROOMNAME_DINKY) and options.force == False:
	print ROOMNAME_DINKY+" already exists. Skipping."
	dinky_exists = True

if path.isfile(ROOMNAME_WIMPY) and options.force == False:
	print ROOMNAME_WIMPY+" already exists. Skipping."
	wimpy_exists = True

print "Creating "+ROOMNAME

# Replace and write ROOMNAME.dinky file

if not dinky_exists:
	try:
		text = open(TEMPLATE_DINKY, "r").read()
		text = string.replace(text, "__ROOMNAME__", ROOMNAME)
		try:
			open(ROOMNAME_DINKY, "w").write(text)
		except:
			print "Can't write "+ROOMNAME_DINKY
			exit(1)
	except:
		print "Can't read "+TEMPLATE_DINKY
		exit(1)

# Replace and write ROOMNAME.wimpy file

if not wimpy_exists:
	try:
		text = open(TEMPLATE_WIMPY, "r").read()
		text = string.replace(text, "__ROOMNAME__", ROOMNAME)
		try:
			open(ROOMNAME_WIMPY, "w").write(text)
		except:
			print "Can't write "+ROOMNAME_WIMPY
			exit(1)
	except:
		print "Can't read "+TEMPLATE_WIMPY
		exit(1)

# Add include() and defineRoom() to DEFINE_ROOMS

try:
	text = open(DEFINE_ROOMS, "r").read()

	text_import = 'import("'+ROOMNAME+'.dinky")'
	text_define = 'defineRoom('+ROOMNAME+')'
	if text.find(text_import) == -1:
		text = string.replace(text, "// INCLUDE", text_import+"\n// INCLUDE")
	if text.find(text_define) == -1:
		text = string.replace(text, "// DEFINE", text_define+"\n// DEFINE")
	try:
		open(DEFINE_ROOMS, "w").write(text)
	except:
		print "Can't write "+DEFINE_ROOMS
		exit(1)
except:
	print "Can't read "+DEFINE_ROOMS
	exit(1)

# Create Images/ROOMNAME

try:
	os.makedirs(IMAGEDIR+"/"+ROOMNAME)
except:
	pass

print ""
print "Then run bin/munge_psd.py to export new images."
print ""
print "Done."





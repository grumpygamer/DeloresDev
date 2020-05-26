#!/usr/bin/python

import os
import sys
from PIL import Image
from optparse import OptionParser
from psd_tools import PSDImage

# Globals
source_size = None
emited_files = {}

def visit_layer(psd, layer, options):
	global source_size, emited_files

	name=layer.name
	if name.endswith(".png") and not name.startswith("-"):
		if name in emited_files:
			print("ERROR layer "+name+" appears in the .psd twice and was already emitted.")
			return False
		emited_files[name] = True
		if layer.is_group():
			bounds = None
			width = None
			height = None
			for child in layer:
				if child.name == "@bounds":
					if child.kind == "shape":
						bounds = (
						    int(round(child.vector_mask.bbox[0] * psd.width)),
						    int(round(child.vector_mask.bbox[1] * psd.height)),
						    int(round(child.vector_mask.bbox[2] * psd.width)),
						    int(round(child.vector_mask.bbox[3] * psd.height)),
						)
						width = bounds[2]-bounds[0]
						height = bounds[3]-bounds[1]
					elif child.kind == "solidcolorfill":
						bounds = child.bbox
						bounds = ( bounds[0], bounds[1], bounds[2], bounds[3] )
						width = bounds[2]-bounds[0]
						height = bounds[3]-bounds[1]
					else:
						bounds = child.bbox
						# Adjustments are due to psd-tools not capturing the bounds correctly. Is this true anymore?
						bounds = ( bounds[0]+1, bounds[1]+1, bounds[2]-1, bounds[3]-1 )
						width = child.width-2
						height = child.height-2
					child.visible = False
			layer.visible = True
			image = layer.composite()
			if bounds != None:
				if options.verbose:
					print("@bounds: "+str(width)+","+str(height))
				new_image = Image.new("RGBA", (width, height))
				image_bounds = layer.bbox
				try:
					new_x = image_bounds[0]-bounds[0]
					new_y = image_bounds[1]-bounds[1]
					new_image.paste(image, (new_x, new_y))
				except:
					pass
				if not options.quiet:
					print("Saving "+name+" @bounds ("+str(width)+","+str(height)+")")
				try:
					new_image.save(options.image_folder+"/"+name)
				except:
					print("ERROR saving "+name)
					return False
			else:
				if not options.quiet:
					print("Saving "+name)
				try:
					image.save(options.image_folder+"/"+name)
				except:
					print("ERROR composing "+name)
					return False
		else:
			layer.visible = True
			image = layer.composite()
			if not options.quiet:
				print("Saving "+name)
			try:
				image.save(options.image_folder+"/"+name)
			except:
				print("ERROR saving "+name)
				return False
	if layer.is_group():
		layer.visible = True
		for child in layer:
			visit_layer(psd, child, options)

def slicePSD(psd_filename, options):
	global source_size, emited_files

	try:
		psd = PSDImage.open(psd_filename)
	except:
		print("Error reading "+psd_filename)
		return False

	source_size = psd.size
	emited_files = {}

	for layer in psd:
		if visit_layer(psd, layer, options) == False:
			return False

	return True

def main(args):
	parser = OptionParser(usage="%prog [options]")
	parser.add_option("--quiet", action="store_true", dest="quiet", default=False, help="Quiet flag")
	parser.add_option("--images", action="store", dest="image_folder", default="./", help="Folder to place images into")
	parser.add_option("--verbose", action="store_true", dest="verbose", default=False, help="Verbose output")
	(options, args) = parser.parse_args(args)

	if len(args) == 0:
		print("Missing .psd file. Did you mean to call munge_psd.py?")
		sys.exit(1)

	if (options.quiet):
		options.verbose = False

	if slicePSD(args[0], options) == False:
		sys.exit(1)

if __name__ == '__main__':
    main(sys.argv[1:])

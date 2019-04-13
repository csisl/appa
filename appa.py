#!/usr/bin/python3
import argparse
import sys
from PIL import Image, ImageMath

# COLOR CODES
CRESET = '\33[0m'
CGREEN = '\33[32m'
CRED   = '\33[31m'

def binary_conversion(msg):
	binary_msg = ' '.join(format(ord(char), 'b') for char in msg)
	if debug or report: print_status("BINARY STRING:",binary_msg)
	return binary_msg

def get_image(img):
	try:
		# open the image in read only mode so we don't modify the original image
		image = Image.open(img, 'r')
	except IOError:
		print("[-] Error opening image {}".format(img))
		sys.exit()

	return image.copy()

# Purpose:	To inject binary data into the image we need to made values in the pixel
#			bit map even/odd based on the binary value and the (R,G,B) values
# Notes:	We need 3 * the length of the message pixels because letters are 8 bit 
def get_pixels(pixel_count, image):
	pixels = list(image.getdata())[0:pixel_count]
	if debug or report: print_status("PIXELS TO BE MODIFIED:\n", pixels)
	return pixels

def mod_bits(msg, pixels):
	# get the pixels
	for bit in msg: 
		print("{}".format(bit))
	return

def get_pixel_count(image):
	width, height = image.size
	return width * height

# Purpose:	print the status to the screen when in debug mode 
#			with fancy formatting that now doesn't have to be copied & pasted a ton
def print_status(message, value):
	print(CGREEN + "\n[!] " + CRESET, end="")
	print("{} {}\n".format(message, value))
	return

if __name__ == "__main__":
	global debug
	global report
	debug = False
	report = False

	parser = argparse.ArgumentParser(description="Interactive steganography")

	parser.add_argument("message",
			help="Message to inject in the image")
	parser.add_argument("image",
			help="Image to inject a message into")
	parser.add_argument("-d", "--debug", action="store_true",
			help="Debug mode")
	parser.add_argument("-r", "--report", action="store_true",
			help="Create report of what was done during processing")

	args = parser.parse_args()

	if args.debug:
		debug = True
	if args.report:
		report = True

	image = get_image(args.image)
	pixel_count = len(args.message) * 3
	pixels = get_pixels(pixel_count, image)
	binary_msg = binary_conversion(args.message)

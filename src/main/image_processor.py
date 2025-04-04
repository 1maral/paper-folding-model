from PIL import Image
import numpy as np

class ImageProcessor:

	# fields:
	# No fields at the moment
	def __init__(self):
		pass

	# Gives a single image and makes it a bitmap representation
	@staticmethod
	def img_bitmap(img):
		imgp = Image.open(img)
		ary = np.array(imgp)

		# Split the three channels
		r,g,b = np.split(ary, 3, axis=2)
		r = r.reshape(-1)
		g = r.reshape(-1)
		b = r.reshape(-1)

		# Standard RGB to grayscale 
		bitmap = 0.299 * r + 0.587 * g + 0.114 * b
		bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])

		# Convert to 1s and 0s
		bitmap_binary = (bitmap < 128).astype(int)

		bitmap = np.dot((bitmap < 128).astype(float),255)
		im = Image.fromarray(bitmap.astype(np.uint8))
		im.save(img.split('.')[0] + ".bmp")

		return(bitmap_binary)
	
	# =============================================================
	# Comment: would it make more sense to make `img_arr` a field?
	# =============================================================

	# process all the images in the array through the local function
	# returns the bitmap representation of the image and the information
	def img_process(self, img_arr):
		processed_img = []
		for x in range (0, len(img_arr)):
			processed_img.append(self.img_bitmap(img_arr[x]))
		return(processed_img)
	
	@staticmethod
	# Note (delete later): Used in the `fold` and `unfold` methods.
	def reflect(image, fold_line):
		pass

	@staticmethod
	def or_operation(image1, image2):
        # A union-like operation is performed on the pixels of the two images.
        # A pixel that is white in either image becomes white in the new one. 
        # Otherwise, the pixel will be black in the new image.
		return np.maximum(image1, image2)
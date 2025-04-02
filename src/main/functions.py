from PIL import Image
import numpy as np

class ImageClass:

	# fields:
	# array of images are given
	def __init__(self, img_arr):
		self.img_arr = img_arr

	# ========================================================================
	# COMMENTS:
	# I THINK WE SHOULD ALSO MAKE ANOTHER BITMAP OF 0'S AND 1'S IF WE WANT 
	# TO IMPLEMENT IT THE WAY THE PAPER DOES? AND MAYBE MAKE IT RETURN AS A
	# 2D ARRAY INSTEAD OF AN IMAGE OBJECT (MAKES IT EASIER FOR THE 
	# PAPER_FOLDING FXNS I THINK). THEN, MAKE A SEPARATE FXN TO TRANSFORM A 
	# BITMAP INTO AN IMAGE OBJECT?
	# ========================================================================
	
	# Gives a single image and makes it a bitmap representation
	@staticmethod
	def img_bitmap(img):
		imgp = Image.open(img)
		ary = np.array(imgp)

		# Split the three channels
		r,g,b = np.split(ary, 3, axis=2)
		r=r.reshape(-1)
		g=r.reshape(-1)
		b=r.reshape(-1)

		# Standard RGB to grayscale 
		bitmap = 0.299 * r + 0.587 * g + 0.114 * b
		bitmap = np.array(bitmap).reshape([ary.shape[0], ary.shape[1]])
		bitmap = np.dot((bitmap < 128).astype(float),255)
		im = Image.fromarray(bitmap.astype(np.uint8))
		im.save(img.split('.')[0] + ".bmp")
		return(im)

	# process all the images in the array through the local function
	# returns the bitmap representation of the image and the information
	def img_process(self):
		processed_img = []
		for x in range (0, len(self.img_arr)):
			processed_img.append(self.img_bitmap(self.img_arr[x]))
		return(processed_img)
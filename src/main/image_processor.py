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
		im = Image.fromarray(image.astype(np.uint8))
		im.save("src/image/test-1.jpg")

		coord1_x = fold_line[0][0]
		coord1_y = fold_line[0][1]
		coord2_x = fold_line[1][0]
		coord2_y = fold_line[1][1]

		# Check x-coords
		max_x = coord1_x
		min_x = coord2_x
		if coord2_x > coord1_x:
			max_x = coord2_x
			min_x = coord1_x

		# Check if fold line is horizontal or vertical
		# Note: x of 2D array refers to "y-axis" and yoord of 2D array refers to "x-axis" 
		# but it's flipped (or normal) for the fold line coords...

		# MAYBE SHOULD SWITCH X AND Y FOR CLARITY B/C X ACTUALLY REPRESENTS THE Y-COORD AND Y 
		# ACTUALLY THE X-COORD ON A XY-PLANE B/C I GOT SO CONFUSED

		# Horizontal fold: (vertical reflection)
		if (coord2_y - coord1_y) == 0:
			for x in range(min_x, max_x):
				row = image[x]
				for y in range(len(row)):
					if image[x][y] == 1:
						reflected_x = coord1_x - (x - coord1_x)
						reflected_y = y

						# Swap pixels
						temp = image[reflected_x][reflected_y]
						image[reflected_x][reflected_y] = image[x][y]
						image[x][y] = temp
			return image
		
		# Vertical fold: (horizontal reflection)
		if (coord2_x - coord1_x) == 0:
			for x in range(len(image)):
				row = image[x]
				for y in range(len(row)):
					if image[x][y] == 1:
						reflected_x = x
						reflected_y = coord1_y - (y - coord1_y)

						# Swap pixels
						temp = image[reflected_x][reflected_y]
						image[reflected_x][reflected_y] = image[x][y]
						image[x][y] = temp
			return image


		# For diagonal folds:
		# Calculating fold line 
		slope = (float)(coord2_y - coord1_y) / (coord2_x - coord1_x)
		C = coord1_y - slope * coord1_x

		reflection_line = []

		# Find pixels on reflection line
		for x in range(min_x, max_x):
			row = image[x]
			for y in range(len(row)):
				if (y == slope * x + C):
					reflection_line.append((x, y))

		print(reflection_line)
		im = Image.fromarray(image.astype(np.uint8))
		# im.save("src/image/test-1.jpg")

		for x in range(min_x, max_x):
			row = image[x]
			for y in range(len(row)):
				if image[x][y] == 1:
					print("original x =" + str(x) + ",", "original y =" + str(y))
					# d = (Ax + By + C) / A^2 + B^2
					A = -1 * slope
					d = (A * x + y + -1 * C) / (A ** 2 + 1)
					reflected_x = round(x - 2 * A * d) - 1
					reflected_y = round(y - 2 * d) - 1
					print("reflected_x =" + str(reflected_x) + ",", "reflected_y =" + str(reflected_y))

					# Swap pixels
					temp = image[reflected_x][reflected_y]
					image[reflected_x][reflected_y] = image[x][y]
					image[x][y] = temp

		return image

	@staticmethod
	def or_operation(image1, image2):
    	# A union-like operation is performed on the pixels of the two images.
    	# A pixel that is white in either image becomes white in the new one. 
    	# Otherwise, the pixel will be black in the new image.
		return np.maximum(image1, image2)
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
	
	# for non-jpg conversions
	def img_process1(self, img_arr):
		processed_img = []
		for x in range (0, len(img_arr)):
			processed_img.append(self.img_bitmap1(img_arr[x]))
		return(processed_img)
	
	# To convert from bmp to bitmap (from Claude)
	@staticmethod
	def img_bitmap1(img):
		"""Converts image to binary bitmap representation.
		Preserves white (255) as 1 and black (0) as 0.
		"""
		try:
			# Read image
			image = Image.open(img)
			
			# Convert to grayscale if RGB
			if image.mode == 'RGB':
				image = image.convert('L')
			
			# Convert to numpy array
			ary = np.array(image)
			
			# Normalize to binary (0 and 1)
			# White (255) becomes 1, Black (0) becomes 0
			return (ary > 128).astype(int)
			
		except Exception as e:
			print(f"Error processing image {img}: {e}")
			return None

	
	@staticmethod
	# Note (delete later): Used in the `fold` and `unfold` methods.
	def reflect(image, fold_line):

		coord1_x = fold_line[0][0]
		coord1_y = fold_line[0][1]
		coord2_x = fold_line[1][0]
		coord2_y = fold_line[1][1]

		# Correct coords of fold_line for horizontal & vertical folds 
		if coord2_y - coord1_y == 1: # horizontal fold line
			coord1_y += 1 # arbitrary increment to get the coords on the same row
		if coord2_x - coord1_x == 1: # vertical fold line
			coord1_x += 1 # arbitrary increment to get the coords on the same col
		# Adjust if coord is near end bound b/c end bound is exclusive 
		if coord1_x == len(image[0]) - 1:
			coord1_x += 1
		if coord2_x == len(image[0]) - 1:
			coord2_x += 1
		if coord1_y == len(image) - 1:
			coord1_y += 1
		if coord2_y == len(image) - 1:
			coord2_y += 1
			
		# Check x-coords
		max_x = coord1_x
		min_x = coord2_x
		if coord2_x > coord1_x:
			max_x = coord2_x
			min_x = coord1_x

		# # # Check if fold line is horizontal or vertical
		# # # Note: x of 2D array refers to "y-axis" and yoord of 2D array refers to "x-axis" 
		# # # but it's flipped (or normal) for the fold line coords...

		# # # MAYBE SHOULD SWITCH X AND Y FOR CLARITY B/C X ACTUALLY REPRESENTS THE Y-COORD AND Y 
		# # # ACTUALLY THE X-COORD ON A XY-PLANE B/C I GOT SO CONFUSED

		# Horizontal fold: (vertical reflection)
		if (coord2_y - coord1_y) == 0:
			# Determine which half above or below fold line is bigger.
			img_height = len(image)
			if img_height - coord1_y > coord1_y - 0:
				begin = coord1_y
				end = img_height
			else: 
				begin = 0
				end = coord1_y

			for x in range(begin, end): # the bigger half (up or down)
				row = image[x]
				for y in range(len(row)):
					if x < coord1_y: # px is above fold line
						reflected_x = (coord1_y - x) + coord1_y
					else: # px is below fold line
						reflected_x = coord1_y - (x - coord1_y) 
					reflected_y = y

					# Only swap pixels if not out of bound
					if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
						temp = image[reflected_x][reflected_y]
						image[reflected_x][reflected_y] = image[x][y]
						image[x][y] = temp
					else: 
						# if out of bounds, still want to change the pixel to 
						# black (just don't try to access the reflected px). 
						# Otherwise you'll get weird strips of white
						image[x][y] = 0

			return image
		
		# Vertical fold: (horizontal reflection)
		if (coord2_x - coord1_x) == 0:
			# Determine which half left or right of the fold line is bigger.
			img_width = len(image[0])
			if img_width - coord1_x > coord1_x - 0:
				begin = coord1_x
				end = img_width
			else: 
				begin = 0
				end = coord1_x
			
			for x in range(len(image)): # the height of the img
				for y in range(begin, end): # the bigger half (left or right)
					if y < coord1_x:
						reflected_y = (coord1_x - y) + coord1_x
					else: 
						reflected_y = coord1_x - (y - coord1_x) 
					reflected_x = x

					# Only swap pixels if not out of bound
					if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
						temp = image[reflected_x][reflected_y]
						image[reflected_x][reflected_y] = image[x][y]
						image[x][y] = temp
					else: 
						# if out of bounds, still want to change the pixel to 
						# black (just don't try to access the reflected px). 
						# Otherwise you'll get weird strips of white
						image[x][y] = 0
			return image

		# Calculating fold line 
		slope = (float)(coord2_y - coord1_y) / (coord2_x - coord1_x)
		C = coord1_y - slope * coord1_x

		# reflection_line = []
		# Find pixels on reflection line
		# for x in range(min_x, max_x):
		# 	reflection_line.append(slope * x + C - 1)

		# print(reflection_line)

		for x in range(min_x, max_x):
			# row = image[x]
			for y in range(coord1_y, coord2_y):
				# if image[x][y] == 0:
				# if x < reflection_line[x - min_x]:
				# if x == 160:
					# print("original x =" + str(x) + ",", "original y =" + str(y))
				# d = (Ax + By + C) / A^2 + B^2
				A = -1 * slope
				d = (A * x + y + -1 * C) / (A ** 2 + 1)

				# have to adjust code so that it reflects the bigger section (left or right from the reflection line)!
				# then have to deal with the calculation of the reflected pt based on that?

				if d >= 0:
					reflected_x = round(x - 2 * A * d) - 1
					reflected_y = round(y - 2 * d) - 1 
					# if x == 160:
					# 	print("reflected_x =" + str(reflected_x) + ",", "reflected_y =" + str(reflected_y))

					# Only swap pixels if not out of bound
					if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
					# if x == 160 and y == 280:
					# 	print("Original val", image[x][y], "Reflected coords:", reflected_x, ",", reflected_y)
						temp = image[reflected_x][reflected_y]
						image[reflected_x][reflected_y] = image[x][y]
						image[x][y] = temp
					else: 
						# if out of bounds, still want to change the pixel to 
						# black (just don't try to access the reflected px). 
						# Otherwise you'll get weird strips of white
						image[x][y] = 0
					# if x == 160 and y == 280:
					# 	print("New val", image[x][y])
		return image

	@staticmethod
	def or_operation(image1, image2):
    	# A union-like operation is performed on the pixels of the two images.
    	# A pixel that is white in either image becomes white in the new one. 
    	# Otherwise, the pixel will be black in the new image.
		return np.maximum(image1, image2)
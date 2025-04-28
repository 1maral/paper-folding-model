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
	# - not sure.
	# =============================================================

	# process all the images in the array through the local function
	# returns the bitmap representation of the image and the information
	def img_process(self, img_arr):
		processed_img = []
		for x in range (0, len(img_arr)):
			if img_arr[x].split('.')[1] == "jpg":
				processed_img.append(self.img_bitmap(img_arr[x]))
			else:
				processed_img.append(self.img_bitmap1(img_arr[x]))
		return(processed_img)

    # convert numpy array to image and save in testing folder with a given name
	def bmp_image(arr, img_name, show):
		arr = np.dot((arr > 0).astype(float),255)
		im = Image.fromarray(arr.astype(np.uint8))
		im.save("src/image/" + img_name + ".bmp")
		if show == True:
			im.show()
		return
	
	# To convert from png to bitmap (from Claude)
	@staticmethod
	def img_bitmap1(img):
		"""Converts a PNG image to a black & white bitmap and saves it."""
		try:
			# Open and convert to grayscale
			image = Image.open(img).convert('L')
			ary = np.array(image)

			# Change: 128 to 200 so the light blue px gets converted to white 
			# in bitmap
			# Apply threshold (128) to get binary array
			binary_array = (ary < 200).astype(np.uint8) * 255

			# Create black & white image with explicit 'L' mode
			bw_image = Image.fromarray(binary_array, mode='L')
			
			# Save BMP
			bw_image.save(img.split('.')[0] + ".bmp")

			return (binary_array // 255).astype(int)
		except Exception as e:
			print(f"Error processing image {img}: {e}")
			return None
		
	# To convert from bmp to bitmap (from Claude)
	@staticmethod
	def img_bitmap2(img):
		"""Converts a bmp image to a black & white bitmap and saves it."""
		try:
			# Open and convert to grayscale
			image = Image.open(img).convert('L')
			ary = np.array(image)

			# Apply threshold (128) to get binary array
			binary_array = (ary < 128).astype(np.uint8) * 255

			# Create black & white image with explicit 'L' mode
			bw_image = Image.fromarray(binary_array, mode='L')
			
			# Save BMP
			bw_image.save(img.split('.')[0] + ".bmp")

			return (binary_array // 255).astype(int)
		except Exception as e:
			print(f"Error processing image {img}: {e}")
			return None

	@staticmethod
	# Note (delete later): Used in the `fold` and `unfold` methods.
	def reflect(image, fold_line):

		# x-axis (= cols) is left to right. y-axis (= rows) is top to bottom.
		coord1_x = fold_line[0][0]
		coord1_y = fold_line[0][1]
		coord2_x = fold_line[1][0]
		coord2_y = fold_line[1][1]

		# Account for how fold line is returned by op_stack
		# Correct coords of fold_line for horizontal & vertical folds 
		if coord2_y - coord1_y == 1: # horizontal fold line
			coord1_y += 1 # arbitrary increment to get the coords on the same row
		if coord2_x - coord1_x == 1: # vertical fold line
			coord1_x += 1 # arbitrary increment to get the coords on the same col

		# Creating a copy of the image to be reflected
		reflected_img = np.copy(image)

		# Determine type of fold.

		# Horizontal fold: (vertical reflection)
		if (coord2_y - coord1_y) == 0:
			for y in range(len(image)):
				for x in range(len(image[0])):
					if image[y][x] == 1:
						if y < coord1_y: # px is above fold line
							reflected_y = (coord1_y - y) + coord1_y
						else: # px is below fold line
							reflected_y = coord1_y - (y - coord1_y) 
						reflected_x = x

						# Only swap pixels if not out of bound
						if 0 <= reflected_x < len(image[0]) and 0 <= reflected_y < len(image):
							temp = reflected_img[reflected_y][reflected_x]
							reflected_img[reflected_y][reflected_x] = reflected_img[y][x]
							reflected_img[y][x] = temp
						else: 
							# If out of bounds, still want to change the pixel to 
							# black (just don't try to access the reflected px). 
							# Otherwise you'll get weird strips of white.
							reflected_img[y][x] = 0

			return reflected_img

		# Vertical fold: (horizontal reflection)
		if (coord2_x - coord1_x) == 0:
			for y in range(len(image)): 
				for x in range(len(image[0])): 
					if image[y][x] == 1:
						if x < coord1_x: # px is left of fold line
							reflected_x = (coord1_x - x) + coord1_x
						else: # px is right of fold line
							reflected_x = coord1_x - (x - coord1_x) 
						reflected_y = y

						# Only swap pixels if not out of bound
						if 0 <= reflected_x < len(image[0]) and 0 <= reflected_y < len(image):
							temp = reflected_img[reflected_y][reflected_x]
							reflected_img[reflected_y][reflected_x] = reflected_img[y][x]
							reflected_img[y][x] = temp
						else: 
							reflected_img[y][x] = 1
			return reflected_img

		# Calculating fold line 
		slope = (float)(coord2_y - coord1_y) / (coord2_x - coord1_x)
		C = coord1_y - slope * coord1_x

		# reflection_line = []
		# Find pixels on reflection line
		# for x in range(min_x, max_x):
		# 	reflection_line.append(slope * x + C - 1)

		# print(reflection_line)

		for y in range(0, len(image)):
			for x in range(0, len(image[0])):
				# d = (Ax + By + C) / A^2 + B^2
				A = -1 * slope
				d = (A * y + x + -1 * C) / (A ** 2 + 1)

				# if d >= 0:
				# If it's white pixel we swap in a copy of the image.
				if image[y][x] == 1:
					# floor added
					reflected_y = round(y - 2 * A * d) # int(np.floor(...))
					reflected_x = round(x - 2 * d) # int(np.floor(...))
					# Only swap pixels if not out of bound
					if 0 <= reflected_x < len(image[0]) and 0 <= reflected_y < len(image):
						temp = reflected_img[reflected_y][reflected_x]
						reflected_img[reflected_y][reflected_x] = reflected_img[y][x]
						reflected_img[y][x] = temp
					else: 
						reflected_img[y][x] = 0
		return reflected_img

	@staticmethod
	def or_operation(image1, image2):
    	# A union-like operation is performed on the pixels of the two images.
    	# A pixel that is white in either image becomes white in the new one. 
    	# Otherwise, the pixel will be black in the new image.
		return np.maximum(image1, image2)
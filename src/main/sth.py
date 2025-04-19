        # # Calculating fold line 
		slope = (coord2_y - coord1_y) / (coord2_x - coord1_x)
		C = coord1_y - slope * coord1_x
		# A = -1 * slope

		# reflection_line = []
		# Find pixels on reflection line
		# for x in range(min_x, max_x):
		# 	reflection_line.append(slope * x + C - 1)

		# print(reflection_line)

		# Check x-coords
		# max_x = coord1_x
		# min_x = coord2_x
		# if coord2_x > coord1_x:
		# 	max_x = coord2_x
		# 	min_x = coord1_x

		# Calculating fold line 
		# slope = (coord2_y - coord1_y) / (coord2_x - coord1_x)
		# C = coord2_x * coord1_y - coord1_x * coord2_y # coord1_x * coord2_y - coord2_x * coord1_y
		# A = coord1_y - coord2_y
		# B = coord2_x - coord1_x

		# If the fold line is short, extend its end coordinates.
		# ...


		# Note: by min_x, max_x, I mean the begin and end bounds for the cols. 
		# min_y, max_y = begin, end for rows. (for-loop)

		# Determine which side from the fold line is bigger (to reflect)
		# A perfect diagonal line or a more horizontal diagonal line
		# if abs(slope) == 1 or abs(slope) < 1: 
		# 	# Calculate area above line, which is a trapezoid: 
		# 	# (1/2 * (base1 + base2) * height) 
		# 	b_1 = coord1_y
		# 	b_2 = coord2_y
		# 	h = abs(coord1_x - coord2_x)
		# 	area = 0.5 * (b_1 + b_2) * h

		# 	# Bounds: entire width of image
		# 	min_x = 0
		# 	max_x = img_width

		# 	if area >= 0.5 * img_height * img_width:
		# 		# Bounds: top half
		# 		min_y = 0
		# 		max_y = coord2_y
		# 		side = "above"
		# 	else: 
		# 		# Bounds: bottom half
		# 		min_y = coord1_y
		# 		max_y = img_height
		# 		side = "below"

		# else: # A more vertical diagonal line
		# 	# Calculate area left of line, which is a trapezoid: 
		# 	# (1/2 * (base1 + base2) * height) 
		# 	b_1 = coord1_x
		# 	b_2 = coord2_x
		# 	h = img_height # abs(coord1_y - coord2_y)
		# 	area = 0.5 * (b_1 + b_2) * h

		# 	# Bounds: entire height of image
		# 	min_y = 0
		# 	max_y = img_height

		# 	if area >= 0.5 * img_height * img_width:
		# 		side = "left"
		# 		# Bounds: left half
		# 		min_x = 0
		# 		if slope > 0:
		# 			max_x = coord1_x
		# 		else: 
		# 			max_x = coord2_x
		# 	else: 
		# 		side = "right"
		# 		# Bounds: right half
		# 		max_x = img_width
		# 		if slope > 0:
		# 			min_x = coord2_x
					
		# 		else: 
		# 			max_x = coord1_x

		# for x in range(min_y, max_y):
		# 	for y in range(min_x, max_x):
		# 		b = coord1_y - slope * coord1_x
		# 		d = (A * x + B * y + C) / np.sqrt(A * A + B * B) # (A * x + y + -1 * C) / (A ** 2 + 1)
		# 		if side == "above":
		# 			if x < slope * y + b: # if point is above line
		# 				reflected_x = round(x - 2 * A * d)
		# 				reflected_y = round(y - 2 * B * d)

		# 				# Only swap pixels if not out of bound
		# 				if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
		# 					temp = image[reflected_x][reflected_y]
		# 					image[reflected_x][reflected_y] = image[x][y]
		# 					image[x][y] = temp
		# 				else: 
		# 					# if out of bounds, still want to change the pixel to 
		# 					# black (just don't try to access the reflected px). 
		# 					# Otherwise you'll get weird strips of white
		# 					image[x][y] = 0
		# 		elif side == "below":
		# 			if x > slope * y + b: # if point is below line
		# 				reflected_x = round(x - 2 * A * d)
		# 				reflected_y = round(y - 2 * d)

		# 				# Only swap pixels if not out of bound
		# 				if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
		# 					temp = image[reflected_x][reflected_y]
		# 					image[reflected_x][reflected_y] = image[x][y]
		# 					image[x][y] = temp
		# 				else: 
		# 					image[x][y] = 0
		# 		elif side == "left":
		# 			if y < round((y - b) / slope): # if point is below line
		# 				reflected_x = round(x - 2 * A * d)
		# 				reflected_y = round(y - 2 * d)

		# 				# Only swap pixels if not out of bound
		# 				if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
		# 					temp = image[reflected_x][reflected_y]
		# 					image[reflected_x][reflected_y] = image[x][y]
		# 					image[x][y] = temp
		# 				else: 
		# 					image[x][y] = 0
		# 		else: # side == "right"
		# 			if y > round((y - b) / slope): # if point is below line
		# 				reflected_x = round(x - 2 * A * d)
		# 				reflected_y = round(y - 2 * d)

		# 				# Only swap pixels if not out of bound
		# 				if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
		# 					temp = image[reflected_x][reflected_y]
		# 					image[reflected_x][reflected_y] = image[x][y]
		# 					image[x][y] = temp
		# 				else: 
		# 					image[x][y] = 0
				# image[x][y]

				# A = -1 * slope
				# d = (A * x + B * y + C) / np.sqrt(A * A + B * B) # (A * x + y + -1 * C) / (A ** 2 + 1)

				# if d >= 0:
				# 	reflected_x = round(x - 2 * A * d) - 1
				# 	reflected_y = round(y - 2 * d) - 1 
				# 	# Only swap pixels if not out of bound
				# 	if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
				# 		temp = image[reflected_x][reflected_y]
				# 		image[reflected_x][reflected_y] = image[x][y]
				# 		image[x][y] = temp
				# 	else: 
				# 		# if out of bounds, still want to change the pixel to 
				# 		# black (just don't try to access the reflected px). 
				# 		# Otherwise you'll get weird strips of white
				# 		image[x][y] = 0

		# ====================================================================

		# Original Original Code:
		
		reflected_img = image.copy()

		# b = oord1_y - slope * coord1_x 

		# A = -1 * slope
		# B = 1
		# C = -1 * b
		
		A = coord1_x - coord2_x
		B = coord2_y - coord1_y
		C = coord1_x * coord2_y - coord2_x * coord1_y

		for x in range(img_height):
			for y in range(img_width):
				# if image[x][y] == 0:
				# if x < reflection_line[x - min_x]:
				# if x == 160:
					# print("original x =" + str(x) + ",", "original y =" + str(y))
				# d = (Ax + By + C) / A^2 + B^2

				# have to adjust code so that it reflects the bigger section (left or right from the reflection line)!
				# then have to deal with the calculation of the reflected pt based on that?
				
				# Only reflect white pixels.
				if image[x][y] == 1:
					# A = -1 * slope
					# d = (A * x + y + -1 * C) / (A ** 2 + 1)
					d = (A * x + B * y + C) / (A ** 2 + B ** 2)
					
					reflected_x = round(x - 2 * A * d) # - 1
					reflected_y = round(y - 2 * B *  d) # - 1 
					# if x == 160:
					# 	print("reflected_x =" + str(reflected_x) + ",", "reflected_y =" + str(reflected_y))

					# Only swap pixels if not out of bound
					if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
					# if x == 160 and y == 280:
					# 	print("Original val", image[x][y], "Reflected coords:", reflected_x, ",", reflected_y)
						temp = reflected_img[reflected_x][reflected_y]
						reflected_img[reflected_x][reflected_y] = reflected_img[x][y]
						reflected_img[x][y] = temp
					else: 
						# if out of bounds, still want to change the pixel to 
						# black (just don't try to access the reflected px). 
						# Otherwise you'll get weird strips of white
						reflected_img[x][y] = 0
					# if x == 160 and y == 280:
					# 	print("New val", image[x][y])

		# ====================================================================

		# CLAUDERS:

		# # Calculate line equation: ax + by + c = 0
		# a = coord2_y - coord1_y
		# b = coord1_x - coord2_x
		# c = coord2_x * coord1_y - coord1_x * coord2_y

		# # Count pixels on each side
		# above_line = 0
		# below_line = 0
		# for x in range(len(image)):
		# 	for y in range(len(image[0])):
		# 		# Calculate distance from point to line
		# 		d = (a * x + b * y + c) / (a * a + b * b)
		# 		if d > 0:
		# 			above_line += 1
		# 		elif d < 0:
		# 			below_line += 1

		# # Use the larger side for reflection
		# if above_line > below_line:
		# 	# Reflect points where d >= 0
		# 	above_line = True # which part is bigger (pt above line)
		# 	d_threshold = 0
		# else:
		# 	# Reflect points where d <= 0
		# 	d_threshold = 0
		# 	above_line = False # pt below line



		# for x in range(len(image)):
		# 	for y in range(len(image[0])):
		# 		# Then in your main reflection loop:
		# 		if above_line:
		# 			if d >= 0:  
		# 				reflected_x = round(x - 2 * A * d) - 1
		# 				reflected_y = round(y - 2 * d) - 1
		# 			# Only swap pixels if not out of bound
		# 				if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
		# 					temp = image[reflected_x][reflected_y]
		# 					image[reflected_x][reflected_y] = image[x][y]
		# 					image[x][y] = temp
		# 				else: 
		# 					image[x][y] = 0
		# 		else:
		# 			if d <= 0:
		# 				reflected_x = round(x - 2 * A * d) - 1
		# 				reflected_y = round(y - 2 * d) - 1

		# 				# Only swap pixels if not out of bound
		# 				if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
		# 					temp = image[reflected_x][reflected_y]
		# 					image[reflected_x][reflected_y] = image[x][y]
		# 					image[x][y] = temp
		# 				else: 
		# 					image[x][y] = 0

		

		# ====================================================================

		# for x in range(min_x, max_x):
		# 	# row = image[x]
		# 	for y in range(coord1_y, coord2_y):
		# 		# if image[x][y] == 0:
		# 		# if x < reflection_line[x - min_x]:
		# 		# if x == 160:
		# 			# print("original x =" + str(x) + ",", "original y =" + str(y))
		# 		# d = (Ax + By + C) / A^2 + B^2
		# 		A = -1 * slope
		# 		d = (A * x + y + -1 * C) / (A ** 2 + 1)

		# 		# have to adjust code so that it reflects the bigger section (left or right from the reflection line)!
		# 		# then have to deal with the calculation of the reflected pt based on that?

		# 		if d >= 0:
		# 			reflected_x = round(x - 2 * A * d) - 1
		# 			reflected_y = round(y - 2 * d) - 1 
		# 			# if x == 160:
		# 			# 	print("reflected_x =" + str(reflected_x) + ",", "reflected_y =" + str(reflected_y))

		# 			# Only swap pixels if not out of bound
		# 			if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
		# 			# if x == 160 and y == 280:
		# 			# 	print("Original val", image[x][y], "Reflected coords:", reflected_x, ",", reflected_y)
		# 				temp = image[reflected_x][reflected_y]
		# 				image[reflected_x][reflected_y] = image[x][y]
		# 				image[x][y] = temp
		# 			else: 
		# 				# if out of bounds, still want to change the pixel to 
		# 				# black (just don't try to access the reflected px). 
		# 				# Otherwise you'll get weird strips of white
		# 				image[x][y] = 0
		# 			# if x == 160 and y == 280:
		# 			# 	print("New val", image[x][y])


		# ====================================================================

		# Original Original Code:
		# for x in range(min_x, max_x):
		# 	# row = image[x]
		# 	for y in range(coord1_y, coord2_y):
		# 		# if image[x][y] == 0:
		# 		# if x < reflection_line[x - min_x]:
		# 		# if x == 160:
		# 			# print("original x =" + str(x) + ",", "original y =" + str(y))
		# 		# d = (Ax + By + C) / A^2 + B^2
		# 		A = -1 * slope
		# 		d = (A * x + y + -1 * C) / (A ** 2 + 1)

		# 		# have to adjust code so that it reflects the bigger section (left or right from the reflection line)!
		# 		# then have to deal with the calculation of the reflected pt based on that?

		# 		if d >= 0:
		# 			reflected_x = round(x - 2 * A * d) - 1
		# 			reflected_y = round(y - 2 * d) - 1 
		# 			# if x == 160:
		# 			# 	print("reflected_x =" + str(reflected_x) + ",", "reflected_y =" + str(reflected_y))

		# 			# Only swap pixels if not out of bound
		# 			if 0 <= reflected_x < len(image) and 0 <= reflected_y < len(image[0]):
		# 			# if x == 160 and y == 280:
		# 			# 	print("Original val", image[x][y], "Reflected coords:", reflected_x, ",", reflected_y)
		# 				temp = image[reflected_x][reflected_y]
		# 				image[reflected_x][reflected_y] = image[x][y]
		# 				image[x][y] = temp
		# 			else: 
		# 				# if out of bounds, still want to change the pixel to 
		# 				# black (just don't try to access the reflected px). 
		# 				# Otherwise you'll get weird strips of white
		# 				image[x][y] = 0
		# 			# if x == 160 and y == 280:
		# 			# 	print("New val", image[x][y])

		return reflected_img
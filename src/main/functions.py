class FunctionsClass:

	# fields:
	# array of images are given
	def __init__(self, img_arr):
		self.img_arr = img_arr

	# Gives a single image and makes it a bitmap representation
	@staticmethod
	def img_bitmap(img):
		return("processed!")

	# process all the images in the array through the local function
	def img_process(self):
		processed_img = []
		for x in range (0, len(self.img_arr)):
			print(x)
			processed_img.append(self.img_bitmap(self.img_arr[x]))
		return(processed_img)
from functions import ImageClass

# Fields: 

# Image stack keeps track of images that represent the layers of folds
img_stack = []
# Operations stack keeps track of the operations that are performed on the images as folds occur
op_stack = []

# Input: sequence of images that represent the state of the folded paper in each time-slice.
# Diameter of punch: 27 px, Radius: 13.5 px
# Size of paper: 320 x 320 px
img_arr = ['src/image/in1.jpg', 'src/image/in2.jpg', 'src/image/in3.jpg']

# An instance of the Image Class is initiated with the proper input
img_processor = ImageClass(img_arr)

# 1D array of processed bitmap images in Image type for each state
state_img = img_processor.img_process()

def initialize():
    blank_img = 'src/image/start.jpg'
    # Process the unfolded paper(blank) to bitmap representation
    blank_img = img_processor.img_bitmap(blank_img)
    # Add the initial image to Image Stack
    img_stack.append(blank_img)

# Initialize operation sets up the model
initialize()
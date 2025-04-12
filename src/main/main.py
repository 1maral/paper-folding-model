from image_processor import ImageProcessor
from paper import Paper
import numpy as np
from PIL import Image

# Fields: 
# The model:
# Image stack keeps track of images that represent the layers of folds
img_stack = []
# Operations stack keeps track of the operations that are performed on the images as folds occur
op_stack = []
# An instance of the Image Processor is initiated
img_processor = ImageProcessor()
# Create a paper for the paper folding task.
paper = Paper(img_stack, op_stack)

# =============================================================================
# Functions:
def initialize():
    blank_img = 'src/image/start.jpg'
    # Process the unfolded paper(blank) to bitmap representation
    blank_bitmap = img_processor.img_bitmap(blank_img)
    # Add the initial image to Image Stack
    img_stack.append(blank_bitmap)

def pick_solution(unfolded_paper, solutions):
    """Selects the image that most resembles the unfolded paper after 
    folding and punching."""

    rows = len(unfolded_paper)
    cols = len(unfolded_paper[0])
    matching_percentage = np.zeros(len(solutions))

    # Compare each solution to the unfolded paper.
    for i in range(len(solutions)):
        curr_solution = solutions[i]
        matching_px = 0

        # Count the number of matching pixels.
        for row in range(rows):
            for col in range(cols):
                if unfolded_paper[row][col] == curr_solution[row][col]:
                    matching_px += 1

        # Calculate the similarity in percentage.
        matching_percentage[i] = matching_px / (rows * cols) * 100

    # Return the most similar solution.
    return np.argmax(matching_percentage)

# =============================================================================

# WE SHOULD WRITE A MAIN FXN FOR ORGANIZATION!

# Input: sequence of images that represent the state of the folded paper in each time-slice.
# Diameter of punch: 27 px, Radius: 13.5 px
# Size of paper: 320 x 320 px
input_arr = ['src/image/in1.jpg', 'src/image/in2.jpg', 'src/image/in3.jpg']
solutions_img = ['src/image/sol1.jpg', 'src/image/sol2.jpg', 'src/image/sol3.jpg', 'src/image/sol4.jpg', 'src/image/sol5.jpg']

# 1D array of processed bitmap images in Image type for each state
input_bitmap = img_processor.img_process(input_arr)
solutions_bitmap = img_processor.img_process(solutions_img)

# =============================================================================
# For testing:
solutions_img.append('src/image/in3.jpg')
# =============================================================================
# Initialize operation sets up the model
initialize()

# Fold, punch a hole, and unfold the paper.
paper.fold()
paper.punch()
# unfolded_paper = paper.unfold()

# =============================================================================
# Some testing code for `unfold`: (can't figure out the ModuleNotFoundError in 
# `test.py`)

# Two layers: in3.jpg & in3.jpg on image stack
# in3_img = "src/image/in3.jpg"
# in3_bitmap = img_processor.img_bitmap(in3_img)
# img_stack.append(in3_bitmap)
# img_stack.append(in3_bitmap)
# op_stack.append([159, 159], [0, 0])

# paper = Paper(img_stack, op_stack)
# unfolded_paper = paper.unfold()

# # result is in3.jpg
# print(unfolded_paper)
# # =============================================================================

# # Choose the solution that resembles the unfolded paper the most.
# prediction = pick_solution(unfolded_paper, solutions_bitmap)
# print("Solution", prediction, "is the answer.")

# =============================================================================
# Testing for reflect
# originally src/image/w2.jpg
bitmap1 = img_processor.img_bitmap('src/image/w2.jpg')
# Horizontal Fold: (vertical reflection)
# reflected = img_processor.reflect(bitmap1, [(0, 160), (320, 160)])
# Vertical Fold: (horizontal reflection)
# reflected = img_processor.reflect(bitmap1, [(160, 0), (160, 320)])
# Diagonal Fold: 
reflected = img_processor.reflect(bitmap1, [(320, 160), (160, 320)])
# reflected = img_processor.reflect(bitmap1, [(0, 0), (320, 320)])
# reflected = img_processor.reflect(bitmap1, [(320, 0), (0, 320)])

reflected = np.dot((reflected > 0).astype(float),255)
im = Image.fromarray(reflected.astype(np.uint8))
im.save("src/image/reflected.jpg")

# =============================================================================
# Testing for unfold
base = img_processor.img_bitmap('src/image/w1.jpg')
flap = img_processor.img_bitmap('src/image/w2.jpg')
# op = [(0, 160), (320, 160)] # Horizontal Fold (vertical Reflection)
paper1 = Paper([base, base, flap, flap], [[(0, 160), (320, 160)], [(0, 160), (320, 160)], [(0, 160), (320, 160)]])
unfolded_paper = paper1.unfold()
unfolded_paper = np.dot((unfolded_paper > 0).astype(float),255)
im = Image.fromarray(unfolded_paper.astype(np.uint8))
im.save("src/image/unfolded.bmp")
# UNFOLD SEEMS TO WORK SO FAR!
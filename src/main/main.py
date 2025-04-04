from image_processor import ImageProcessor
from paper import Paper
import numpy as np

# Fields: 
# ...

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


# The model:
# Image stack keeps track of images that represent the layers of folds
img_stack = []
# Operations stack keeps track of the operations that are performed on the images as folds occur
op_stack = []

# Input: sequence of images that represent the state of the folded paper in each time-slice.
# Diameter of punch: 27 px, Radius: 13.5 px
# Size of paper: 320 x 320 px
input_arr = ['src/image/in1.jpg', 'src/image/in2.jpg', 'src/image/in3.jpg']
solutions_img = ['src/image/sol1.jpg', 'src/image/sol2.jpg', 'src/image/sol3.jpg', 'src/image/sol4.jpg', 'src/image/sol5.jpg']

# =============================================================================
# For testing:
solutions_img.append('src/image/in3.jpg')
# =============================================================================

# An instance of the Image Processor is initiated with the proper input
img_processor = ImageProcessor()

# 1D array of processed bitmap images in Image type for each state
input_bitmap = img_processor.img_process(input_arr)
solutions_bitmap = img_processor.img_process(solutions_img)

# Initialize operation sets up the model
# initialize()

# Create a paper for the paper folding task.
paper = Paper(img_stack, op_stack)

# Fold, punch a hole, and unfold the paper.
paper.fold()
paper.punch()
# unfolded_paper = paper.unfold()

# =============================================================================
# Some testing code for `unfold`: (can't figure out the ModuleNotFoundError in 
# `test.py`)

# Two layers: in3.jpg & in3.jpg on image stack
in3_img = "src/image/in3.jpg"
in3_bitmap = img_processor.img_bitmap(in3_img)
img_stack.append(in3_bitmap)
img_stack.append(in3_bitmap)
op_stack.append([159, 159])

paper = Paper(img_stack, op_stack)
unfolded_paper = paper.unfold()

# result is in3.jpg
print(unfolded_paper)
# =============================================================================

# Choose the solution that resembles the unfolded paper the most.
prediction = pick_solution(unfolded_paper, solutions_bitmap)
print("Solution", prediction, "is the answer.")
from functions import ImageClass
from paper_folding import PaperFolding
import numpy as np

# Fields: 

# Image stack keeps track of images that represent the layers of folds
img_stack = []
# Operations stack keeps track of the operations that are performed on the images as folds occur
op_stack = []

# Input: sequence of images that represent the state of the folded paper in each time-slice.
# Diameter of punch: 27 px, Radius: 13.5 px
# Size of paper: 320 x 320 px
img_arr = ['src/image/in1.jpg', 'src/image/in2.jpg', 'src/image/in3.jpg']

# ====================
# Comment:
# Need a list possible solutions as Images. Then, convert those to bitmaps. ??
# ====================
possible_solutions = np.zeros((320, 320))
solution_bitmaps = np.zeros((320, 320))

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

# Create a paper for the paper folding task.
paper = PaperFolding(img_stack, op_stack)

# Fold, punch a hole, and unfold the paper.
paper.fold()
paper.punch()
unfolded_paper = paper.unfold()

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

        # Calculate how similarity in percentage.
        matching_percentage[i] = matching_px / (rows * cols) * 100

    # Return the most similar solution.
    return solutions[np.argmax(matching_percentage)]

# Choose the solution that resembles the unfolded paper the most.
prediction = pick_solution(unfolded_paper, solution_bitmaps)
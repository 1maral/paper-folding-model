from image_processor import ImageProcessor
from paper import Paper
import numpy as np
from PIL import Image

class Model:
    # Fields: 
    # The model:
    def __init__(self):
        # Image stack keeps track of images that represent the layers of folds
        self.img_stack = []
        # Operations stack keeps track of the operations that are performed on the images as folds occur
        self.op_stack = []
        
        # An instance of the Image Processor is initiated
        self.img_processor = ImageProcessor()
        
        self.initialize()

        # Create a paper for the paper folding task.
        self.paper = Paper(self.img_stack, self.op_stack)
        # maybe this should be: self.paper = Paper([], []) -- no image and op 
        # stacks for the model; leave that in Paper?

    # =============================================================================
    # Functions:
    def initialize(self):
        blank_img = 'src/image/start.jpg'
        # Process the unfolded paper(blank) to bitmap representation
        blank_bitmap = self.img_processor.img_bitmap(blank_img)
        # Add the initial image to Image Stack
        self.img_stack.append(blank_bitmap)

    def pick_solution(self, unfolded_paper, solutions):
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
            for row in range(0, rows):
                for col in range(0, cols):
                    if unfolded_paper[row][col] == curr_solution[row][col]:
                        matching_px += 1

            # Calculate the similarity in percentage.
            matching_percentage[i] = (matching_px / (rows * cols)) * 100

        print(matching_percentage)

        # Return the most similar solution.
        return np.argmax(matching_percentage) + 1 # to return the actual solution number, not the index!

    # =============================================================================

if __name__ == "__main__":
    # Input: sequence of images that represent the state of the folded paper in each time-slice.
    # Diameter of punch: 27 px, Radius: 13.5 px
    # Size of paper: 320 x 320 px
    # input_arr = ['src/image/in1.jpg', 'src/image/in2.jpg', 'src/image/in3.jpg']
    solutions_img = ['src/image/sol1.jpg', 'src/image/sol2.jpg', 'src/image/sol3.jpg', 'src/image/sol4.jpg', 'src/image/sol5.jpg']

    #------------------------------------------------------------------------------
    input_arr = ['src/image/2in1.png', 'src/image/2in2.png', 'src/image/2in3.png', 'src/image/2in4.png', 'src/image/2in5.png']
    
    model = Model()
    # 1D array of processed bitmap images in Image type for each state
    input_bitmap = model.img_processor.img_process(input_arr)
    solutions_bitmap = model.img_processor.img_process(solutions_img)

    # =============================================================================
    # For testing:
    # solutions_img.append('src/image/in3.jpg')
    # =============================================================================
    # Initialize operation sets up the model -- do this in constructor?
    # model.initialize()

    # Fold, punch a hole, and unfold the paper.
    folded = model.paper.fold(input_bitmap)
    model.paper.punch(input_bitmap)
    unfolded_paper = model.paper.unfold()

    # =============================================================================
    # Unfolded_paper numpy array is processed into image bmp, then it
    # is saved in the testing folder as unfolded and shown as boolean is TRUE
    ImageProcessor.bmp_image(unfolded_paper, "testing/unfolded", True)

    # =============================================================================
    # IGNORE THIS SECTION? JUST USE THE LAST SECTION FOR TESTING UNFOLD!
    
    # Some testing code for `unfold`: (can't figure out the ModuleNotFoundError in 
    # `test.py`)

    # Two layers: in3.jpg & in3.jpg on image stack
    # in3_img = "src/image/in3.jpg"
    # in3_bitmap = self.img_processor.img_bitmap(in3_img)
    # self.img_stack.append(in3_bitmap)
    # self.img_stack.append(in3_bitmap)
    # op_stack.append([159, 159], [0, 0])

    # paper = Paper(self.img_stack, op_stack)
    # unfolded_paper = paper.unfold()

    # # result is in3.jpg
    # print(unfolded_paper)
    # # =============================================================================

    # Choose the solution that resembles the unfolded paper the most.
    prediction = model.pick_solution(unfolded_paper, solutions_bitmap)
    print("Solution", prediction, "is the answer.")

    # =============================================================================
    # Testing for reflect
    # originally src/image/w2.jpg
    # bitmap1 = ImageProcessor.img_bitmap1("src/image/testing/flap-fig-3.bmp")
    # bitmap1 = ImageProcessor.img_bitmap1("src/image/2in1.bmp")
    # bitmap1 = ImageProcessor.img_bitmap("src/image/2in1.jpg")

    # reflected = np.dot((bitmap1 > 0).astype(float),255)
    # im = Image.fromarray(reflected.astype(np.uint8))
    # im.save("src/image/testing/flap-fig-3.jpg")
    # im.show()

    # Horizontal Fold: (vertical reflection)
    # reflected = ImageProcessor.reflect(bitmap1, [(0, 160), (320, 160)])
    # reflected = ImageProcessor.reflect(bitmap1, [(0, 220), (320, 220)])
    # Vertical Fold: (horizontal reflection)
    # reflected = ImageProcessor.reflect(bitmap1, [(160, 0), (160, 320)])
    # reflected = ImageProcessor.reflect(bitmap1, [(40, 0), (40, 320)])
    # reflected = ImageProcessor.reflect(bitmap1, [(240, 0), (240, 320)])
    # Diagonal Fold: 
    # reflected = ImageProcessor.reflect(bitmap1, [(320, 160), (160, 320)])
    # reflected = ImageProcessor.reflect(bitmap1, [(0, 0), (320, 320)])
    # reflected = ImageProcessor.reflect(bitmap1, [(320, 0), (0, 320)])

    # reflected = np.dot((reflected > 0).astype(float),255)
    # im = Image.fromarray(reflected.astype(np.uint8))
    # im.save("src/image/reflected.jpg")
    # im.show()

    # # =============================================================================
    # Testing for unfold
    # model1 = Model()
    # base1 = model1.img_processor.img_bitmap('src/image/w1.jpg')
    # base2 = model1.img_processor.img_bitmap('src/image/w1.jpg')
    # flap1 = model1.img_processor.img_bitmap('src/image/w2.jpg')
    # flap2 = model1.img_processor.img_bitmap('src/image/w2.jpg')
    # op = [(0, 160), (320, 160)] # Horizontal Fold (vertical Reflection)
    # paper1 = Paper([base1, base2, flap1, flap2], [[(0, 160), (320, 160)], [(320, 160), (160, 320)], [(320, 160), (160, 320)]])
    # unfolded_paper = paper1.unfold()
    # unfolded_paper = np.dot((unfolded_paper > 0).astype(float),255)
    # im = Image.fromarray(unfolded_paper.astype(np.uint8))
    # im.save("src/image/unfolded.bmp")
    # im.show()

    # prediction = model.pick_solution(unfolded_paper, solutions_bitmap)
    # print("Solution", prediction, "is the answer.")
    # UNFOLD WORKS! It's just finnicky b/c of `reflect`
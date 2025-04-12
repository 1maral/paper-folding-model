import numpy as np
from image_processor import ImageProcessor
from PIL import Image

class Paper:
    # Not sure what the fields should be if we're planning on keeping the
    # image and operations stacks in `main.py`, so I'm just passing them into
    # the constructor for now although it doesn't make sense.
    def __init__(self, img_stack, op_stack):
        """Initializes Paper with an image and an operations stack."""
        # This represents the layer(s) of the paper.
        # The top of the stack is at the beginning of the list and the bottom 
        # is at the end of the list. 
        self.img_stack = img_stack

        # This stack will contain folds represented as coordinates of the fold
        # line. (list of lists?)
        self.op_stack = op_stack

    def extend_paper(self, old_img):
        copied_img = old_img.copy()
        rows, cols = old_img.shape
        for row in range(rows):
            for col in range(cols):
                if old_img[row, col] == 1:
                    if row - 1 >= 0: # Extend up
                        copied_img[row - 1, col] = 1
                    if row + 1 < rows: # Extend down
                        copied_img[row + 1, col] = 1
                    if col - 1 >= 0: # Extend left
                        copied_img[row, col - 1] = 1
                    if col + 1 < cols: # Extend right
                        copied_img[row, col + 1] = 1
        return copied_img
    
    def compute_max_min_coord(self, flip_line):
        # find min & max row
        rows, cols = flip_line.shape
        topRow = rows-1
        bottomRow = 0
        for row in range(rows):
            for col in range(cols):
                if flip_line[row, col]:
                    if row <= topRow:
                        topRow = row
                    if row >= bottomRow:
                        bottomRow = row

        # lstMin = [col1, col2, col3...]
        # lstMax = [col1, col2, col3...]
        lstTop = []
        lstBottom = []
        for col in range(cols):
            if flip_line[bottomRow, col] == 255:
                lstBottom.append(col)
            if flip_line[topRow, col] == 255:
                lstTop.append(col)

        finalCoordinates = []
        # Case 1:       Case 3:              Case 4:
        # ...           .................    :
        #    ...                             :
        #       ...                          :
        #          ...                       :
        #                                    :
        if lstBottom[0] >= lstTop[0]:
            finalCoordinates = [[topRow, lstTop[0]], [bottomRow, lstBottom[-1]]]
        # Case 2: 
        #          ...
        #       ...
        #    ...
        # ...
        elif lstBottom[0] < lstTop[0]:
            finalCoordinates = [[topRow, lstTop[-1]], [bottomRow, lstBottom[0]]]
        return finalCoordinates

    def fold(self, inputs):
        # create an white paper and put it into the stack
        unfolded_paper = np.ones((320, 320), dtype=int)
        stack = []
        stack.append(unfolded_paper)

        for input_img in inputs[:-1]:
            stack_length = len(stack)
            for cur in range(stack_length):
                stack_img = stack[cur] # pop from stack

                # Figure 3: intersection of fliped input image and stack image
                flip = 1 - input_img # flip the input bitmap
                intersect = np.logical_and(flip, stack_img).astype(int)

                # Figure 4: replace image in stack with the intersection of input image and stack image
                stack[cur] = stack_img & input_img

                # Figure 5:
                extended_input_img = self.extend_paper(input_img) # Extend input_img
                extended_intersect = self.extend_paper(intersect) # Extend intersect
                flip_line = np.logical_and(extended_input_img, extended_intersect).astype(int) # find flip line, flipline = 1
                flip_line = np.dot((flip_line > 0).astype(float),255)
                
                # find max and min coordinates
                coord = self.compute_max_min_coord(flip_line)

                ## reflect
                #stack.append(reflect)

        return stack

    def punch(self, inputs, stack):
        """Simulates punching the paper after folding."""
        input_w_punch = inputs[-1]

        # punch for each img in stack
        for i in len(stack):
            result_array = np.logical_and(input_w_punch, stack[i]).astype(int) # 1 if both pixel is 1
            stack[i] = result_array
        return stack

    def unfold(self):
        """Simulates unfolding the paper.""" 
        # Base case: Stop unfolding when only one layer remains.
        if len(self.img_stack) == 1:
            return self.img_stack.pop()
        
        # Unfold one layer. Reconstruct the state of the paper by combining 
        # the images on the top and bottom of the image stack.
        new_img_stack = []

        while len(self.img_stack) != 0: 
            # Take the very top and very bottom layers of the image stack.
            folded_flap = self.img_stack.pop()
            base_layer = self.img_stack.pop(0)

            # Unfold the top layer of the paper, which is a flap. 
            fold_line = self.op_stack.pop()
            unfolded_flap = ImageProcessor.reflect(folded_flap, fold_line)

            # Combine these two layers. (Reconstruct a state of the unfolded 
            # paper?)
            unfolded_layer = ImageProcessor.or_operation(unfolded_flap, 
                                                         base_layer)

            # Add this partly unfolded paper to a new image stack.
            new_img_stack.append(unfolded_layer)

        # Keep unfolding the paper. 
        self.img_stack = new_img_stack
        return self.unfold()
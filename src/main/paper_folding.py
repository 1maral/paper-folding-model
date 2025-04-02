import numpy as np

class PaperFolding:
    # Not sure what the fields should be if we're planning on keeping the
    # image and operations stacks in `main.py`, so I'm just passing them into
    # the constructor for now although it doesn't make sense.
    def __init__(self, img_stack, op_stack):
        """Initializes PaperFolding with an image and an operations stack."""
        # This represents the layer(s) of the paper.
        # The top of the stack is at the beginning of the list and the bottom 
        # is at the end of the list. 
        self.img_stack = img_stack

        # This stack will contain folds represented as coordinates of the fold
        # line. (list of lists?)
        self.op_stack = op_stack

    def fold(self):
        """Simulates folding the paper."""
        pass

    def punch(self):
        """Simulates punching the paper after folding."""
        pass

    def unfold(self):
        """Simulates unfolding the paper.""" 
        # Unfold one layer. Reconstruct the state of the paper by combining 
        # the images on the top and bottom of the image stack.

        new_img_stack = []

        while len(self.img_stack) != 0: 
            # Take the very top and very bottom layers of the image stack.
            folded_flap = self.img_stack.pop()
            base_layer = self.img_stack.pop(0)

            # Unfold the top layer of the paper, which is a flap. 
            fold_line = self.op_stack.pop()
            unfolded_flap = self._reflect(folded_flap, fold_line)

            # Combine these two layers. (Reconstruct a state of the unfolded 
            # paper?)
            unfolded_layer = self._or_operation(unfolded_flap, base_layer)

            # Add this partly unfolded paper to a new image stack.
            new_img_stack.append(unfolded_layer)

        # Keep unfolding the paper. 
        self.img_stack = new_img_stack
        self.unfold()

    # ---------------
    # Helper Methods -- might move these to `functions.py`?
    # ---------------

    # Note (delete later): Used in the `fold` and `unfold` methods.
    def _reflect(self, image, fold_line):
        pass

    def _or_operation(self, image1, image2):
        # A union-like operation is performed on the pixels of the two images.
        # A pixel that is white in either image becomes white in the new one. 
        # Otherwise, the pixel will be black in the new image.
        return np.maximum(image1, image2)
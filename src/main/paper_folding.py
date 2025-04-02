class PaperFolding:
    # Not sure what the fields should be if we're planning on keeping the
    # image and operations stacks in `main.py`, so I'm just passing them into
    # the constructor for now although it doesn't make sense.
    def __init__(self, img_stack, op_stack):
        """Initializes PaperFolding with an image and an operations stack."""
        self.img_stack = img_stack
        self.op_stack = op_stack

    def fold(self):
        """Simulates folding the paper."""
        pass

    def punch(self):
        """Simulates punching the paper after folding."""
        pass

    def unfold(self):
        """Simulates unfolding the paper.""" 
        pass

    # This might be moved to `main.py` later.
    def pick_solution(self):
        """Selects the image that most resembles the unfolded paper after 
        folding and punching."""
        pass
    
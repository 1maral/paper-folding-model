from image_processor import ImageProcessor
import unittest
import numpy as np
from PIL import Image

class TestImageProcessor(unittest.TestCase):

    def test_reflect_png(self):
        # Test the diagonal fold
        bitmap1 = ImageProcessor.img_bitmap1("src/image/2in1.png")
        
        # # Specify the fold axis for diagonal fold
        # fold_line = [(160, 160), (0, 320)]
        # # fold_line = [(160, 160), (240, 320)]
        # reflected = ImageProcessor.reflect(bitmap1, fold_line)
        
        # # Convert back to image and save/show
        # ImageProcessor.bmp_image(bitmap1, "testing/reflected_png", True)
        
        # Add assertion to ensure image is not unchanged
        # self.assertFalse(np.array_equal(bitmap1, reflected), "Reflection did not change the image")

if __name__ == '__main__':
    unittest.main()

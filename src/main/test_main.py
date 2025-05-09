from image_processor import ImageProcessor
import unittest
import numpy as np
from PIL import Image

class TestImageProcessor(unittest.TestCase):

    def test_reflect_horizontal_fold(self):
        # Test the horizontal fold (vertical reflection)
        bitmap1 = ImageProcessor.img_bitmap1("src/image/2in1.png")

        
        # Specify the fold axis for horizontal fold (vertical reflection)
        fold_line = [(0, 160), (320, 160)]
        reflected = ImageProcessor.reflect(bitmap1, fold_line)
        # Convert back to image and save/show
        ImageProcessor.bmp_image(reflected, "testing/reflected_horizontal", False)
        
        # Add assertion to ensure image is not unchanged, assuming reflection changes image
        self.assertFalse(np.array_equal(bitmap1, reflected), "Reflection did not change the image")

    def test_reflect_vertical_fold(self):
        # Test the vertical fold (horizontal reflection)
        bitmap1 = ImageProcessor.img_bitmap1("src/image/2in1.png")
        
        # Specify the fold axis for vertical fold (horizontal reflection)
        fold_line = [(160, 0), (160, 320)]
        reflected = ImageProcessor.reflect(bitmap1, fold_line)
        
        # Convert back to image and save/show
        ImageProcessor.img_bitmap1(reflected, "testing/reflected_vertical", False)

        # Add assertion to ensure image is not unchanged
        self.assertFalse(np.array_equal(bitmap1, reflected), "Reflection did not change the image")

    def test_reflect_diagonal_fold(self):
        # Test the diagonal fold
        bitmap1 = ImageProcessor.img_bitmap1("src/image/2in2.png")
        
        # Specify the fold axis for diagonal fold
        fold_line = [(160, 160), (0, 320)]
        # fold_line = [(160, 160), (240, 320)]
        reflected = ImageProcessor.reflect(bitmap1, fold_line)
        reflected = ImageProcessor.reflect(reflected, fold_line)
        
        # Convert back to image and save/show
        ImageProcessor.bmp_image(reflected, "testing/reflected_diagonal", False)
        
        # Add assertion to ensure image is not unchanged
        self.assertFalse(np.array_equal(bitmap1, reflected), "Reflection did not change the image")

    def test_reflect_png(self):
        # Test the diagonal fold
        bitmap1 = ImageProcessor.img_bitmap1("src/image/8in3.png")
        
        # Specify the fold axis for diagonal fold
        fold_line = [(0, 160), (320, 160)]
        # fold_line = [(160, 160), (240, 320)]
        reflected = ImageProcessor.reflect(bitmap1, fold_line)        
        # Convert back to image and save/show
        ImageProcessor.bmp_image(reflected, "testing/reflected_png", True)
        
        # Add assertion to ensure image is not unchanged
        self.assertFalse(np.array_equal(bitmap1, reflected), "Reflection did not change the image")

if __name__ == '__main__':
    unittest.main()
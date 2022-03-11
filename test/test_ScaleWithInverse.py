from scalum import ScaleWithInverse
import unittest
import numpy as np

class TestScaleWithInverse(unittest.TestCase):

    def test_construction(self):
        ScaleWithInverse(640,640)

    def test_resize(self):
        image = np.zeros((480,640,3),dtype=np.uint8)
        scale = ScaleWithInverse(160,160)
        scaled_image,inverse_function = scale(image)
        result = inverse_function(0,20)
        expected = (0,0)
        self.assertEqual(result,expected)

        result = inverse_function(0,20)
        expected = (0,0)
        self.assertEqual(result,expected)

        result = inverse_function(20,40)
        expected = (80,80)
        self.assertEqual(result,expected)
    
    def test_edgecases(self):
        image = np.zeros((480,640,3),dtype=np.uint8)
        scale = ScaleWithInverse(160,160)
        scaled_image,inverse_function = scale(image)

        result = inverse_function(0,0)
        expected = (0,0)
        self.assertEqual(result,expected)
        
                
        result = inverse_function(-11,-22)
        expected = (0,0)
        self.assertEqual(result,expected)

if __name__ == "__main__":
    unittest.main()


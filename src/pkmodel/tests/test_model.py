import unittest
import pkmodel as pk
import numpy as np
from pkmodel.model import Model, IV, SC


# class ModelTest(unittest.TestCase):
#         """
#         Tests the :class: 'Model' class.
#         """
#         def test_create(self):
#                 """
#                 Tests model creation
#                 """
#                 model = Model(value=42)
#                 self.assertEqual(model, 42)
#                 self.assertIsInstance(model, Model, 'Error initiated wrong class')
                
class ModelTest(unittest.TestCase):
    """
    Tests the :class: 'Model' class.
    """
    def test_create(self):

        model = Model(value=42)
        self.assertEqual(model.value, 42)  # Check if the 'value' attribute is set correctly
        self.assertIsInstance(model, Model, 'Error initiated wrong class')

        if __name__ == '__main__':
                unittest.main()




        def test_paramIV(self):
                """
                Tests output of IV function
                """
                model = IV
                t = np.linspace(0, 1, 1000)
                y = np.array([1, 1]) 
                
                self.parametersIV = [2, 2, 4, 2, 1]

                output = model.paramIV(self, y,t)

                self.assertEqual(output[1], 0.35)
                self.assertEqual(output[0], 0.65)
                self.assertIsInstance(output[1], float), 'Error, output not correct object type'
                self.assertIsInstance(output[0], float), 'Error, output not correct object type'
                   
                
        def test_paramSC(self):
                """
                Tests output of SC function
                """
                model = SC
                self.parametersSC = [2, 2, 4, 2, 1, 2]
                y = np.array([1, 1, 1])
                t = np.linspace(0, 1, 1000)
                
                output = model.paramSC(self,y, t)
                
                self.assertEqual(output[0], 2.65)
                self.assertEqual(output[1], 0.35)
                self.assertEqual(output[2], -2.0)
                
                self.assertIsInstance(output[0], float), 'Error, output not correct object type'
                self.assertIsInstance(output[1], float), 'Error, output not correct object type'
                self.assertIsInstance(output[2], float), 'Error, output not correct object type'  
                         

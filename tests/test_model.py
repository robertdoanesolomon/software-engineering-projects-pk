import unittest
import pkmodel as pk
import numpy as np

class ModelTest(unittest.TestCase):
        """
        Tests the :class: 'Model' class.
        """
        def test_create(self):
                """
                Tests model creation
                """
                model = pk.Model()
                self.assertEqual(model.value, 42)
                self.assertIsInstance(model, pk.Model, 'Error initiated wrong class')
                
        
                
        
        def test_paramIV(self):
                """
                Tests output of IV function
                """
                model = pk.Model
                t = np.array(0, 1, 1000)
                y = np.array([1, 1]) 
                
                self.parameters = [2, 2, 4, 2, 1]
        
 
                output = model.paramIV(y, t)

                self.assertEqual(output[1], 0.5)
                self.assertEqual(output[0], 0.5)
                self.assertIsInstance(output[1], float), 'Error, output not correct object type'
                self.assertIsInstance(output[0], float), 'Error, output not correct object type'
                   
                
        def test_paramSC(self):
                """
                Tests output of SC function
                """
                model = pk.Model
                self.parameters = [2, 2, 4, 2, 1, 2]
                y = [1, 1, 1]
                t = np.array(0, 1, 1000)
                
                output = model.paramSC(y, t)
                
                self.assertEqual(output[0], 0.5)
                self.assertEqual(output[1], 0.5)
                self.assertEqual(output[2], -1)
                
                self.assertIsInstance(output[0], float), 'Error, output not correct object type'
                self.assertIsInstance(output[1], float), 'Error, output not correct object type'
                self.assertIsInstance(output[2], float), 'Error, output not correct object type'  
                         

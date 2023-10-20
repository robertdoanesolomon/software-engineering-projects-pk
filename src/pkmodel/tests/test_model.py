import unittest
import pkmodel as pk
import numpy as np
from pkmodel.model import Model, IV, SC


class ModelTest(unittest.TestCase):
        """
        Tests the :class: 'Model' class.
        """
        def test_create(self):
                """
                Tests model creation
                """
                model = Model
                self.assertEqual(model.value, 42)
                self.assertIsInstance(model, Model, 'Error initiated wrong class')
                
        
                
        
        def test_paramIV(self):
                """
                Tests output of IV function
                """
                model = IV
                t = np.linspace(0, 1, 1000)
                y = np.array([1, 1]) 
                
                self.parametersIV = [2, 2, 4, 2, 1]
        
 
                output = model.paramIV(self, y,t)

                self.assertEqual(output[1], 0.5)
                self.assertEqual(output[0], 0.5)
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
                
                self.assertEqual(output[0], 0.5)
                self.assertEqual(output[1], 0.5)
                self.assertEqual(output[2], -1)
                
                self.assertIsInstance(output[0], float), 'Error, output not correct object type'
                self.assertIsInstance(output[1], float), 'Error, output not correct object type'
                self.assertIsInstance(output[2], float), 'Error, output not correct object type'  
                         

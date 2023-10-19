import unittest
import pkmodel as pk


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
        
        def test_dose(self):
                model = pk.Model
                t = 2
                X = 5
                result = model.dose(t, X)
                self.assertEqual(result, 5)
                assert isinstance(result, int), 'Error, output not correct object type'
        
        def test_param(self):
                """
                Tests output of IV function
                """
                model = pk.Model
                t = np.array(0, 1, 1000)
                y = np.array([1, 1]) 
                Q_p1 = 2
                V_c = 2
                V_p1 = 4
                CL = 2
                X = 1
 
                output = model.IV(t, y, Q_p1, V_c, V_p1, CL, X)

                self.assertEqual(output[1], 0.5)
                self.assertEqual(output[0], )
                assert isinstance(output[1], float), 'Error, output not correct object type'
                assert isinstance(output[0], float), 'Error, output not correct object type'
                   
                
        #def test_SC(self):
               # model = pk.Model

#Length args = length reqiured for the models
#Test variables required for the models 

#
# Model class
#
import matplotlib.pylab as plt
import numpy as np
import scipy.integrate
from scipy.integrate import odeint

class Model:
    """A Pharmokinetic (PK) model

    Parameters
    ----------

    value: numeric, optional
        an example paramter

    """
    def __init__(self, value=42):
        self.value = value   

class IV(Model):
    # Your class definition here
    def __init__(self, parametersIV=[0, 0, 0, 0, 0]):
        super().__init__()
        self.parametersIV = parametersIV

    def paramIV(self, y, t=None):
        [Q_p1, V_c, V_p1, CL, X] = parametersIV
        q_c=y[0]
        q_p1=y[1]
        #q_c, q_p1 = y
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = X - q_c / V_c * CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]
    
    def integrate(self):
        t_eval = np.linspace(0, 1, 1000)
        y0 = [0.0, 0.0]
        solution = odeint(self.paramIV, y0, t_eval)
        q_c, q_p1 = solution.T
        return np.array([q_c,q_p1])

###########TESTING IF CLASS WORKS
parametersIV = [0.7, 1, 2, 3, 4]
test0 = IV(parametersIV=parametersIV)
test1 = test0.integrate()
#test1=IV.integrate()
#print('test1',test1.shape)

############INTEGRATION OUTSIDE THE CLASS
# # Create an instance of the IV class
# iv_instance = IV()

# # Define the time points at which you want to evaluate the solution
# t_eval = np.linspace(0, 1, 1000)

# # Initial conditions
# y0 = [0.0, 0.0]

# # Parameters
# parameters = [0.7, 1, 2, 3, 4]

# # Set the parameters in the instance
# iv_instance.parameters = parameters

# # Solve the ODEs using odeint
# solution = odeint(iv_instance.paramIV, y0, t_eval)

# # Extract the results
# q_c, q_p1 = solution.T

# Print the results
# print(q_c)
# print(q_p1)


class SC(Model):
    "subcutaneous model"
    def __init__(self, parametersSC=[0, 0, 0, 0, 0,0]):
        super().__init__()
        self.parametersSC = parametersSC

    def paramSC(self, y, t=None):
        [Q_p1, V_c, V_p1, CL, X, ka] = parametersSC
        q_c=y[0]
        q_p1=y[1]
        q_0= y[2]
        dq0_dt = X - ka*q_0
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = ka*q_0 - q_c / V_c * CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt,dq0_dt]

    def integrate(self):

        t_eval = np.linspace(0, 1, 1000)
        y0 = [0.0, 0.0, 0.0]
        
        solution = odeint(self.paramSC, y0, t_eval)
        q_c, q_p1, q_0 = solution.T
        return np.array([q_c,q_p1,q_0])


############TESTING IF CLASS WORKS
parametersSC = [0.7, 1, 2, 3, 4,6]
test0 = SC(parametersSC=parametersSC)
test1 = test0.integrate()
#test1=IV.integrate()
print('test1',test1.shape)

############INTEGRATION OUTSIDE THE CLASS
# # Create an instance of the IV class
# sc_instance = SC()

# # Define the time points at which you want to evaluate the solution
# t_eval = np.linspace(0, 1, 1000)

# # Initial conditions
# y0 = [0.0, 0.0,0]

# # Parameters
# parameters = [0.7, 1, 2, 3, 4,7]

# # Set the parameters in the instance
# sc_instance.parameters = parameters

# # Solve the ODEs using odeint
# solution = odeint(sc_instance.paramSC, y0, t_eval)

# print(solution.shape)

# # Extract the results
# # print(solution.T.shape)
# q_c, q_p1, q_0 = solution.T

# # Print the results
# # print(q_c.shape)
# # print(q_p1.shape)
# # print(solution.y[0, :])

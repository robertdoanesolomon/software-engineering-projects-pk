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
        #return(value)

class IV(Model):
    "intravenous model"
    # Your class definition here
    def __init__(self, parametersIV=[0, 0, 0, 0, 0]):
        super().__init__()
        self.parametersIV = parametersIV

    def paramIV(self, y, t=None):
        [Q_p1, V_c, V_p1, CL, X] = self.parametersIV
        q_c = y[0]
        q_p1 = y[1]
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = X - q_c / V_c * CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt]

    def integrate(self):
        t_eval = np.linspace(0, 1, 1000)
        y0 = [0.0, 0.0]
        solution = odeint(self.paramIV, y0, t_eval)
        q_c, q_p1 = solution.T
        return np.array([q_c, q_p1])


class SC(Model):
    "subcutaneous model"
    def __init__(self, parametersSC=[0, 0, 0, 0, 0,0]):
        super().__init__()
        self.parametersSC = parametersSC

    def paramSC(self, y, t=None):
        [Q_p1, V_c, V_p1, CL, X, ka] = self.parametersSC
        q_c = y[0]
        q_p1 = y[1]
        q_0 = y[2]
        dq0_dt = X - ka*q_0
        transition = Q_p1 * (q_c / V_c - q_p1 / V_p1)
        dqc_dt = ka*q_0 - q_c / V_c * CL - transition
        dqp1_dt = transition
        return [dqc_dt, dqp1_dt, dq0_dt]

    def integrate(self):

        t_eval = np.linspace(0, 1, 1000)
        y0 = [0.0, 0.0, 0.0]

        solution = odeint(self.paramSC, y0, t_eval)
        q_c, q_p1, q_0 = solution.T
        return np.array([q_c, q_p1, q_0])

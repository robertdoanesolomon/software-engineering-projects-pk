.. NERC Group 1 Project documentation master file, created by
   sphinx-quickstart on Fri Oct 20 11:36:53 2023.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.


Welcome to NERC Group 1 Project's documentation!
================================================

.. toctree::
   :maxdepth: 2
   :caption: Contents:

Pharmokinetic Model - NERC DTP Group 1
========================================

About
-----

The field of Pharmacokinetics (PK) provides a quantitative basis for describing the delivery of a drug to a patient, the diffusion of that drug through 
the plasma/body tissue, and the subsequent clearance of the drug from the patient's system. PK is used to ensure that there is sufficient concentration 
of the drug to maintain the required efficacy of the drug, while ensuring that the concentration levels remain below the toxic threshold (See Fig 1).

.. image:: https://sabs-r3.github.io/software-engineering-projects/fig/pk1.jpg
   :alt: Fig 1

There are two PK models that this package solves, Intravenous Bolus Dosing, and Subcutaneous Dosing. The models are described in the following sections.

Intravenous Bolus Dosing Protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example PK model describes a two-compartment model. The time-dependent variables to be solved are the drug quantity in the central and 
peripheral compartments, ``q_c`` and ``q_{p1}`` (units: [ng]) respectively.

.. math::

   \frac{d q_c}{dt} &= \text{Dose}(t) - \frac{q_c}{V_c} CL - Q_{p1}\left( \frac{q_c}{V_c} - \frac{q_{p1}}{V_p1}\right)\\
   \frac{d q_1}{dt} &= Q_{p1}\left( \frac{q_c}{V_c} - \frac{q_{p1}}{V_p1}\right)

Subcutaneous Dosing Protocol
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following example PK model describes a three-compartment model. The time-dependent variables to be solved are the drug quantity in a compartment 
before the central compartment, the central, and peripheral compartments, ``q_0``, ``q_c``, and ``q_{p1}`` (units: [ng]) respectively.

.. math::

   \frac{d q_0}{dt} &= \text{Dose}(t) - k_0 q_0  \\
   \frac{d q_c}{dt} &=  k_0 q_0 - 
   \frac{q_c}{V_c} CL - Q_{p1}\left( \frac{q_c}{V_c} - \frac{q_{p1}}{V_p1}\right)\\
   \frac{d q_1}{dt} &= Q_{p1}\left( \frac(q_c}{V_c} - \frac{q_{p1}}{V_p1}\right)

Installation of Model
---------------------

1. Download package from GitHub:
    1. `git clone git@github.com:robertdoanesolomon/software-engineering-projects-pk.git`
    2. `cd software-engineering-projects-pk`
    3. `git checkout --track origin/branch-name` Optionally switch branch for development.
2. Setup virtual environment:
    1. `python3 -m venv venv` Setup virtual environment
    2. `source venv/bin/activate` Activate virtual environment
3. Install package:
    1. `pip install -e .` Install package
4. Test
    1. `python run_test.py` for example on how to call and use the model

Example Model Use
-----------------

After installing the `pkmodel` package, you can select the dosing protocol, run the model, and save a visualization of the results as follows:

Note that:
- the model simulates 1 hour only of drug delivery, calculated with 1000 timesteps,
- the model only simulates continuous, steady-state, drug delivery over the one simulated hour, with the dose set in the parameters - see example below,
- this example is also available in `run_test.py` in the root directory of the package.

Python code example for running the IV model:

```python
import pkmodel

# Example run of the IV model

# Choose parameters for the model
# params = [Q_p1, V_c, V_p1, CL, X], where X is dose in each time step
params = [1, 1, 1, 1, 1]

# Initialize the model with the parameters
model_to_use = pkmodel.model.IV(parameters=params)

# Integrate the model to obtain a solution
# The output of model_to_use.integrate() is a numpy array of dimension
# (2, 1000) where 1000 is the number of time steps, and 3 is the number of
# compartments in the order [q_c, q_p1, q_0]
solution = model_to_use.integrate()

# Visualize the solution and save it to a file
pkmodel.solution.visualize(solution, 'figure_IV.png')


Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

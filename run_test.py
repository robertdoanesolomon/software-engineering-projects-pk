import pkmodel

# Test the IV model
params = [0, 1, 2, 3, 4]
model_to_use = pkmodel.model.IV(parameters=params)
solution = model_to_use.integrate()
pkmodel.solution.visualise(solution, 'figure_IV.png')


# Test the SC model
params = [0, 1, 2, 3, 4, 5]
model_to_use = pkmodel.model.SC(parameters=params)
solution = model_to_use.integrate()
pkmodel.solution.visualise(solution, 'figure_SC.png')

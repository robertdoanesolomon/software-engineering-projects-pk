import pkmodel

# Test the IV model
params = [1, 1, 1, 1, 1]
model_to_use = pkmodel.model.IV(parametersIV=params)
solution = model_to_use.integrate()
pkmodel.solution.visualise(solution, 'figure_IV.png')


# Test the SC model
params = [1, 1, 1, 1, 1, 1]
model_to_use = pkmodel.model.SC(parametersSC=params)
solution = model_to_use.integrate()
pkmodel.solution.visualise(solution, 'figure_SC.png')

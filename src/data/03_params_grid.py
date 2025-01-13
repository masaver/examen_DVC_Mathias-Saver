import pickle

# Define the hyperparameter grid
param_grid = {
    'n_estimators': [50, 100, 200],
    'max_depth': [None, 10, 20, 30],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'max_features': ['sqrt', 'log2'],
}

# Save the dictionary to a .pkl file
with open("./models/param_grid.pkl", "wb") as file:  # "wb" means write in binary mode
    pickle.dump( param_grid , file )

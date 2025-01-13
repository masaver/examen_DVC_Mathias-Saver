# import libraries
import os
import pickle
import pandas as pd
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestRegressor

# Suppress all warnings
import warnings
warnings.filterwarnings("ignore")

# Read input datasets
data_dir = os.path.join( os.path.dirname(__file__) , '../../data/processed_data' )
x_train_s = pd.read_csv( os.path.join( data_dir , 'X_train_scaled.csv' ) , index_col = 0 )
x_test_s = pd.read_csv( os.path.join( data_dir , 'X_test_scaled.csv' ) , index_col = 0 )
y_train = pd.read_csv( os.path.join( data_dir , 'y_train.csv' ) , index_col = 0 )
y_test = pd.read_csv( os.path.join( data_dir , 'y_test.csv' ) , index_col = 0 )
y_train = y_train['silica_concentrate']
y_test = y_test['silica_concentrate']

# Define the RandomForestRegressor
rf = RandomForestRegressor(random_state=17)

# Define the hyperparameter grid
# Load the scaler
with open("./models/param_grid.pkl", 'rb') as f:
    param_grid = pickle.load(f)

print( param_grid )

# Set up GridSearchCV
grid_search = GridSearchCV(
    estimator=rf,
    param_grid=param_grid,
    scoring='neg_mean_squared_error',    # Use negative MSE as the scoring metric
    cv=5,                                # Number of cross-validation folds
    n_jobs=-1,                           # Use all available CPUs
    verbose=2                            # Print progress
)

# Fit the grid search to the training data
grid_search.fit( x_train_s , y_train )

# Save the trained model to a .pkl file
with open("./models/cv_reg_model.pkl", "wb") as file:  # "wb" means write in binary mode
    pickle.dump( grid_search , file )

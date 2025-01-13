# import libraries
import os
import json
import pickle
import pandas as pd
from sklearn.metrics import r2_score, root_mean_squared_error

# Suppress all warnings
import warnings
warnings.filterwarnings("ignore")

# Load the trained model
with open("./models/cv_reg_model.pkl", 'rb') as f: reg_cv = pickle.load(f)

# Read input datasets
data_dir = os.path.join( os.path.dirname(__file__) , '../../data/processed_data' )
x_train_s = pd.read_csv( os.path.join( data_dir , 'X_train_scaled.csv' ) , index_col = 0 )
x_test_s = pd.read_csv( os.path.join( data_dir , 'X_test_scaled.csv' ) , index_col = 0 )
y_train = pd.read_csv( os.path.join( data_dir , 'y_train.csv' ) , index_col = 0 )
y_test = pd.read_csv( os.path.join( data_dir , 'y_test.csv' ) , index_col = 0 )

# Add predictions to the training and test sets
y_train['pred'] = reg_cv.predict( x_train_s )
y_test['pred'] = reg_cv.predict( x_test_s )

# save the updated datasets
y_train.to_csv( os.path.join( data_dir , 'y_train_preds.csv' ) )
y_test.to_csv( os.path.join( data_dir , 'y_test_preds.csv' ) )

# calculate the R2 and RMSE
r2_train = r2_score( y_train['silica_concentrate'] , y_train['pred'] )
r2_test = r2_score( y_test['silica_concentrate'] , y_test['pred'] )
rmse_train = root_mean_squared_error( y_train['silica_concentrate'] , y_train['pred'] )
rmse_test = root_mean_squared_error( y_test['silica_concentrate'] , y_test['pred'] )

# print metrics to a json file
metrics = {
    "r2_train": r2_train,
    "r2_test": r2_test,
    "rmse_train": rmse_train,
    "rmse_test": rmse_test
}

print( metrics )

# save metrics to a json file
with open("./metrics/metrics.json", "w") as file:
    json.dump( metrics , file )

# import requiered libraries
import os
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Create an instance of StandardScaler
scaler = StandardScaler()

# read the train/test datasets
data_dir = os.path.join( os.path.dirname(__file__) , '../../data/processed_data' )
x_train = pd.read_csv( os.path.join( data_dir , 'X_train.csv' ) , index_col=0 )
x_test = pd.read_csv( os.path.join( data_dir , 'X_test.csv' ) , index_col=0 )

# Create an instance of StandardScaler. Fit it to the train set
scaler = StandardScaler()
scaler.fit( x_train )

# Generate the sscaled data.frames
x_train_s = pd.DataFrame( scaler.transform( x_train ) , columns = x_train.columns )
x_test_s = pd.DataFrame( scaler.transform( x_test ) , columns = x_test.columns )
print( x_train_s.head() )
print( x_test_s.head() )

# save the scaled feature sets
data_dir = os.path.join( os.path.dirname(__file__) , '../../data/processed_data' )
x_train_s.to_csv( os.path.join( data_dir , 'X_train_scaled.csv' ) )
x_test_s.to_csv( os.path.join( data_dir , 'X_test_scaled.csv' ) )

# import requiered libraries
import os
import pandas as pd
from sklearn.model_selection import train_test_split

# read the input data
raw_path = os.path.join( os.path.dirname(__file__) , '../../data/raw_data/raw.csv' )
raw_data = pd.read_csv( raw_path , index_col=0 )
print( raw_data.head() )

# train/test split
features = raw_data.drop( 'silica_concentrate' , axis = 1 )
target = raw_data[['silica_concentrate']]
x_train,x_test,y_train,y_test = train_test_split( features , target , test_size=0.2 )

# save the Train/Test data
data_dir = os.path.join( os.path.dirname(__file__) , '../../data/processed_data' )
x_train.to_csv( os.path.join( data_dir , 'X_train.csv' ) )
x_test.to_csv( os.path.join( data_dir , 'X_test.csv' ) )
y_train.to_csv( os.path.join( data_dir , 'y_train.csv' ) )
y_test.to_csv( os.path.join( data_dir , 'y_test.csv' ) )
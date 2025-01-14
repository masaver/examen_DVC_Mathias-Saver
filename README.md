# Examen DVC et Dagshub
Dans ce dépôt vous trouverez l'architecture proposé pour mettre en place la solution de l'examen. 

```bash       
├── examen_dvc          
│   ├── data       
│   │   ├── processed      
│   │   └── raw       
│   ├── metrics       
│   ├── models      
│   │   ├── data      
│   │   └── models        
│   ├── src       
│   └── README.md.py       
```
List of pipeline stages:
1. **Data Splitting**: `dvc stage add -n data_split \
  -d ./src/data/01_data_splitting.py \
  -d ./data/raw_data/raw.csv \
  -o ./data/processed_data/X_train.csv \
  -o ./data/processed_data/X_test.csv \
  -o ./data/processed_data/y_train.csv \
  -o ./data/processed_data/y_test.csv \
  python ./src/data/01_data_splitting.py`

2. **Data Normalization**: `dvc stage add -n normalization \
  -d ./data/processed_data/X_train.csv \
  -d ./data/processed_data/X_test.csv \
  -o ./data/processed_data/X_train_scaled.csv \
  -o ./data/processed_data/X_test_scaled.csv \
  python ./src/data/02_data_normalization.py`

3. **Params Grid Deffinition**: `dvc stage add -n params_grid_def \
  -o ./models/param_grid.pkl \
  python ./src/data/03_params_grid.py`

4. **Model Training**: `dvc stage add -n model_training \
-d ./data/processed_data/X_train_scaled.csv \
-d ./data/processed_data/X_test_scaled.csv \
-d ./data/processed_data/y_train.csv \
-d ./data/processed_data/y_test.csv \
-o ./models/cv_reg_model.pkl \
python ./src/data/04_model_training.py`
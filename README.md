# Examen DVC et Dagshub
This repo contains my solution for the DVC & DagsHub exam.
The tree/folder structure of this repo is as follows:
```bash       
├── README.md
├── data
│   ├── README.md
│   ├── processed_data
│   │   ├── X_test.csv
│   │   ├── X_test_scaled.csv
│   │   ├── X_train.csv
│   │   ├── X_train_scaled.csv
│   │   ├── y_test.csv
│   │   ├── y_test_preds.csv
│   │   ├── y_train.csv
│   │   └── y_train_preds.csv
│   └── raw_data
│       └── raw.csv
├── dvc.lock
├── dvc.yaml
├── experiments
│   └── 01_exp_test.py
├── metrics
│   └── metrics.json
├── models
│   ├── cv_reg_model.pkl
│   └── param_grid.pkl
└── src
    ├── data
    │   ├── 01_data_splitting.py
    │   ├── 02_data_normalization.py
    │   ├── 03_params_grid.py
    │   ├── 04_model_training.py
    │   └── 05_model_evaluation.py
    └── models     
```

And the respective DagsHub repo can be found at:
**`https://dagshub.com/masaver/exam_DVC_Mathias-Saver`**
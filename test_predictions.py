
import mlflow

sample_data = sample_values = {
    "Gender": "Female",
    "Age": 69,
    "HasDrivingLicense": 1,
    "RegionID": 31.0,
    "Switch": 1,
    "PastAccident": "Yes",
    "AnnualPremium": 131.50
}

# logged_model = 'runs:/d39581ecf7934f96b22e64f8ea67f8dd/model'
logged_model = 'put your run id here'

# Load model as a PyFuncModel.
loaded_model = mlflow.pyfunc.load_model(logged_model)

# Predict on a Pandas DataFrame.
import pandas as pd
print(loaded_model.predict(pd.DataFrame(sample_data, index=[0])))
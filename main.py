from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pickle
import numpy as np
import pandas as pd
import uvicorn
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split

# Load the saved model
with open("absenteeism_model.pkl", "rb") as f:
    model = pickle.load(f)

data = pd.read_csv("Absenteeism_at_work.csv")
target_names = data.iloc[:, -1]

# Define the input data format for prediction
class AbsenteeismData(BaseModel):
    features: List[float]

# Initialize FastAPI app
app = FastAPI()

# Define prediction endpoint
@app.post("/predict")
def predict(absenteeism_data: AbsenteeismData):
    # Make prediction
    prediction = model.predict([absenteeism_data.features])[0]
    prediction_name = target_names[prediction]
    
    return {"prediction": int(prediction), "prediction_name": prediction_name}

# Define a root endpoint
@app.get("/")
def read_root():
    return {"message": "Abseenteism at Work Model API"}

# Run the server
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)

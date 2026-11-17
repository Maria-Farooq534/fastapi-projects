from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import json
# import pandas as pd

with open("model.pkl" , "rb") as file:
    model = pickle.load(file)
    

app = FastAPI()

class UserInput(BaseModel):
    age: Annotated[int, Field(..., title="age", gt=0, lt=150)]
    weight: Annotated[float, Field(..., title="Weight in KG", gt=0)]
    height: Annotated[float, Field(..., gt=0, title="Height in meters")]
    income_lpa: Annotated[float, Field(..., title="Income", gt=0)]
    smoker: Annotated[bool, Field(..., title="Is smoker?")]
    city: Annotated[str, Field(..., title="city")]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., title="occupation")]
    
    
    @computed_field
    @property
    def bmi(self) -> float:
        return round(self.height /(self.weight ** 2),2)
    
    
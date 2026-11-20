from fastapi import FastAPI
from pydantic import BaseModel, Field, computed_field
from typing import Literal, Annotated
import pickle
import json
import pandas as pd

with open("model.pkl" , "rb") as file:
    model = pickle.load(file)
    

app = FastAPI()

tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]

tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

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
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return "high"
        elif self.smoker or self.bmi > 27:
            return "medium"
        else:
            return "low"
    
    
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age < 25:
            return "young"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle age"
        return "senior"
    
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3
    

# @app.post("/predict")
# def predict(input_data):
    
#     pd.DataFrame()
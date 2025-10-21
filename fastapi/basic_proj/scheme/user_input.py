from pydantic import BaseModel, Field, computed_field, field_validator
from typing import Annotated, Literal, Optional
from config.city_tier import tier_1_cities, tier_2_cities

# pydantic model to validate input data from the user
class Input(BaseModel):
    age: int = Field(..., ge=1, le=100)
    weight: float = Field(..., ge=1, le=300, description="Weight in kgs")
    height: float = Field(..., ge=1, le=2.5, description="Height in meters")
    income_lpa : float = Field(..., description="Income in lakhs per annum", ge=0)
    smoker: bool = Field(..., description="Is the person a smoker?")
    city: str = Field(..., description="City of residence")
    occupation: Literal['private_job', 'unemployed', 'business_owner', 'retired', 'student','government_job', 'freelancer'] = Field(..., description="Occupation of the person")
    
    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight / (self.height / 100) ** 2
    
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
            return "youth"
        elif self.age < 45:
            return "adult"
        elif self.age < 60:
            return "middle_age"
        return "senior"
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3
    
    @field_validator('city')
    @classmethod
    def normalize_city(cls, v) -> str:
        return v.strip().title()

from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    prediction: str = Field(..., description="Predicted insurance premium category", examples=["low", "medium", "high"])

    confidence: float = Field(..., description="Confidence score of the prediction")
    
    class_probabilities: Dict[str, float] = Field(..., description="Probabilities for each insurance premium category", examples={"low": 0.7, "medium": 0.2, "high": 0.1})
from fastapi import FastAPI, Path, HTTPException, Query
# HTTPException is used to raise an custom exception msg
import json
from pydantic import BaseModel, Field
from typing import Annotated, Literal

app = FastAPI()

class Patient(BaseModel):
    ID: Annotated[int, Field(..., description="The ID of the patient", gt=0)]
    name: Annotated[str, Field(..., description="The name of the patient", min_length=1)]
    age: Annotated[int, Field(..., description="The age of the patient", gt=0, lt=100)]
    gender: Annotated[Literal["male", "female", "other"], Field(..., description="The gender of the patient", min_length=1)]

def load_data():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/about")
async def about():
    return {"message": "vansh visariya"}

@app.get("/patient/{patient_id}")
async def read_item(patient_id: str = Path(..., description="The ID of the patient to get")):
    # ... -> required
    # ge -> greater than or equal to
    # le -> less than or equal to
    complete_id = "patient"+patient_id
    if complete_id not in load_data():
        raise HTTPException(status_code=404, detail="Patient not found")
    return load_data()[complete_id]

@app.get("/sort")
def sort_patient(sort_by: str = Query(..., description="The field to sort by"), 
                 order: str = Query('asc', description="The order to sort by")):
    valid_fields =['age']
    if sort_by not in valid_fields:
        raise HTTPException(status_code=400, detail="Invalid field to sort by")
    
    valid_orders = ['asc', 'desc']
    if order not in valid_orders:
        raise HTTPException(status_code=400, detail="Invalid order to sort by")
    
    data = load_data()
    sorted_data = sorted(data.values(), key=lambda x: x[sort_by], reverse=(order == 'desc'))
    return sorted_data

@app.post('/create')
def create_patient(patient: Patient):
    data = load_data()
    new_id = f"patient{patient.ID}"
    # Check if patient with same ID already exists
    if new_id in data:
        raise HTTPException(status_code=400, detail="Patient with this ID already exists")
    
    data[new_id] = patient.model_dump()
    
    with open('data.json', 'w') as f:
        json.dump(data, f)
    
    return JSONResponse(status_code=201, content={"message": "Patient created successfully", "patient": patient.model_dump()})
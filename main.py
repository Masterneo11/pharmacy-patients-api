import json

import uuid

from fastapi import FastAPI
from models import Patient


app = FastAPI()

with open("patients.json", "r") as f:
    data = json.load(f)

patients = []
for patient_data in data:
    patient_id = uuid.uuid4()
    patient = Patient(id=patient_id, **patient_data)
    patients.append(patient)

@app.get("/patients")
async def get_patients() -> list[Patient]:
    return patients

@app.post("/patients")
async def add_new_patient(patient: Patient):
    patients.append(patient)

@app.put("/patients/{p_id}")
async def update_patient_info(p_id: uuid.UUID, updated_patient: Patient) -> None:
    for i, patient in enumerate(patients):
        if patient.id == p_id:
            patients[i] = updated_patient
            return 

@app.delete("/patients/{p_id}")
async def delete_patient(p_id: uuid.UUID) -> None:
    for i, patient in enumerate(patients):
        if patient.id == p_id:
            patients.pop(i)
            return 

# Use the first name as the unique identifier. For example,
# in the PUT route, you'd have something like this: "/patients/{first_name}"

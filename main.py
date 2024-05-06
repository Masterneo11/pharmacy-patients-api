import json

from fastapi import FastAPI
from models import Patient

app = FastAPI()

with open("patients.json", "r") as f:
    data = json.load(f)

patients = []
for patient_data in data:
    patient = Patient(**patient_data)
    patients.append(patient)

@app.get("/patients")
async def get_patients() -> list[Patient]:
    return patients

@app.post("/patients")
async def add_new_patient(patient: Patient):
    patients.append(patient)

@app.put("/patients/{first_name}")
async def update_patient_info(first_name: str, updated_patient: Patient) -> None:
    index = int
    found = False
    for i, patient in enumerate(patients):
        if patient.first_name.lower() == first_name.lower():
            found = True
            index = i
    if found:
        patients[index] = updated_patient
    else:
        patients.append(updated_patient)

@app.delete("/patients/{first_name}")
async def delete_patient(first_name: str) -> None:
    for i, patient in enumerate(patients):
        if patient.first_name.lower() == first_name.lower():
            patients.pop(i)
            return 

# Use the first name as the unique identifier. For example,
# in the PUT route, you'd have something like this: "/patients/{first_name}"

from fastapi import FastAPI, HTTPException, Query, status
from typing import Dict
from models import (
    PersonBase, PersonCreate, PersonRead, PersonUpdate,
    AddressBase, AddressCreate, AddressRead, AddressUpdate
)

app = FastAPI(
    title="Person/Address API",
    description="Demo FastAPI app using Pydantic v2 models for Person and Address",
    version="1.0.0"
)

# In-memory storage
persons_db: Dict[str, PersonBase] = {}
addresses_db: Dict[str, AddressBase] = {}


# ============== HEALTH ENDPOINTS ==============

@app.get("/health")
def get_health_no_path(echo: str | None = Query(None)):
    return {"status": "healthy", "echo": echo, "path_echo": None}


@app.get("/health/{path_echo}")
def get_health_with_path(path_echo: str, echo: str | None = Query(None)):
    return {"status": "healthy", "echo": echo, "path_echo": path_echo}


# ============== PERSON ENDPOINTS ==============

@app.post("/persons", response_model=PersonRead, status_code=201)
def create_person(person: PersonCreate):
    if person.uni in persons_db:
        raise HTTPException(status_code=400, detail=f"Person with UNI {person.uni} already exists")
    new_person = PersonBase(**person.model_dump())
    persons_db[person.uni] = new_person
    return new_person


@app.get("/persons", response_model=list[PersonRead])
def get_persons():
    return list(persons_db.values())


@app.get("/persons/{person_id}", response_model=PersonRead)
def get_person(person_id: str):
    if person_id not in persons_db:
        raise HTTPException(status_code=404, detail="Person not found")
    return persons_db[person_id]


@app.put("/persons/{person_id}", response_model=PersonRead)
def update_person(person_id: str, person_update: PersonUpdate):
    if person_id not in persons_db:
        raise HTTPException(status_code=404, detail="Person not found")
    stored_person = persons_db[person_id]
    update_data = person_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(stored_person, field, value)
    return stored_person


@app.delete("/persons/{person_id}", status_code=204)
def delete_person(person_id: str):
    if person_id not in persons_db:
        raise HTTPException(status_code=404, detail="Person not found")
    del persons_db[person_id]


# ============== ADDRESS ENDPOINTS ==============

@app.post("/addresses", response_model=AddressRead, status_code=201)
def create_address(address: AddressCreate):
    import uuid
    new_address = AddressBase(id=str(uuid.uuid4()), **address.model_dump())
    addresses_db[new_address.id] = new_address
    return new_address


@app.get("/addresses", response_model=list[AddressRead])
def get_addresses():
    return list(addresses_db.values())


@app.get("/addresses/{address_id}", response_model=AddressRead)
def get_address(address_id: str):
    if address_id not in addresses_db:
        raise HTTPException(status_code=404, detail="Address not found")
    return addresses_db[address_id]


@app.put("/addresses/{address_id}", response_model=AddressRead)
def update_address(address_id: str, address_update: AddressUpdate):
    if address_id not in addresses_db:
        raise HTTPException(status_code=404, detail="Address not found")
    stored_address = addresses_db[address_id]
    update_data = address_update.model_dump(exclude_unset=True)
    for field, value in update_data.items():
        setattr(stored_address, field, value)
    return stored_address


@app.delete("/addresses/{address_id}", status_code=204)
def delete_address(address_id: str):
    if address_id not in addresses_db:
        raise HTTPException(status_code=404, detail="Address not found")
    del addresses_db[address_id]


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
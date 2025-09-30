# Sprint Completion Status Report

**Student Name:** Colin J. Emmanuel  
**Sprint Number:** Sprint 0  
**Duration:** [Your dates] - September 19, 2025  
**Report Date:** September 19, 2025

## 1. Sprint Goal 🎯

**Defined Goal:**
Clone Professor Ferguson's Simple Microservices Repository and create my own version with:
- Two different resources (Person and Address)
- Full CRUD operations
- Auto-generated OpenAPI documentation

**Outcome:** ✅ Achieved

**Notes:** Successfully implemented all required functionality. Both Person and Address resources are fully functional with complete CRUD operations.

## 2. Completed Work ✅

### Resource 1: Person API
- **Model**: PersonBase with fields: uni, first_name, last_name, email, phone (optional), birth_date (optional)
- **Endpoints**:
  - ✅ GET /persons - List all persons
  - ✅ POST /persons - Create new person
  - ✅ GET /persons/{person_id} - Get person by UNI
  - ✅ PUT /persons/{person_id} - Update person
  - ✅ DELETE /persons/{person_id} - Delete person

### Resource 2: Address API  
- **Model**: AddressBase with fields: id (UUID), street, city, state, postal_code, country
- **Endpoints**:
  - ✅ GET /addresses - List all addresses
  - ✅ POST /addresses - Create new address
  - ✅ GET /addresses/{address_id} - Get address by ID
  - ✅ PUT /addresses/{address_id} - Update address
  - ✅ DELETE /addresses/{address_id} - Delete address

### Additional Features
- ✅ Health check endpoints (/health and /health/{path_echo})
- ✅ Pydantic v2 models with proper validation
- ✅ Auto-generated OpenAPI documentation at /docs
- ✅ In-memory data storage
- ✅ Proper HTTP status codes (201 for creation, 204 for deletion)

### Resource 1

Note: my model
```python
class PersonBase(BaseModel):
    """Person model with university-specific fields"""
    uni: str = Field(
        ...,
        description="Columbia University UNI (2-3 lowercase letters + 1-4 digits).",
        json_schema_extra={"example": "abc1234"}
    )
    first_name: str = Field(
        ...,
        description="Given name.",
        json_schema_extra={"example": "Ada"}
    )
    last_name: str = Field(
        ...,
        description="Family name.",
        json_schema_extra={"example": "Lovelace"}
    )
    email: str = Field(
        ...,
        description="Primary email address.",
        json_schema_extra={"example": "ada@example.com"}
    )
    phone: Optional[str] = Field(
        None,
        description="Contact phone number in any reasonable format.",
        json_schema_extra={"example": "+1-212-555-0199"}
    )
    birth_date: Optional[date] = Field(
        None,
        description="Date of birth (YYYY-MM-DD).",
        json_schema_extra={"example": "1815-12-10"}
    )
```
  ### Resource 2
  ```python
  class AddressBase(BaseModel):
    """Address model with UUID identifier"""
    id: str = Field(
        default_factory=lambda: str(uuid.uuid4()),
        description="Persistent Address ID (server-generated).",
        json_schema_extra={"example": "550e8400-e29b-41d4-a716-446655440000"}
    )
    street: str = Field(
        ...,
        description="Street address and number.",
        json_schema_extra={"example": "123 Main St"}
    )
    city: str = Field(
        ...,
        description="City or locality.",
        json_schema_extra={"example": "New York"}
    )
    state: Optional[str] = Field(
        None,
        description="State/region code if applicable.",
        json_schema_extra={"example": "NY"}
    )
    postal_code: Optional[str] = Field(
        None,
        description="Postal or ZIP code.",
        json_schema_extra={"example": "10001"}
    )
    country: str = Field(
        ...,
        description="Country name or ISO label.",
        json_schema_extra={"example": "USA"}
    )

  ### main.py Routes
  # Health endpoints
  @app.get("/health")
  def get_health_no_path(echo: str | None = Query(None)):
      return {"status": "healthy", "echo": echo, "path_echo": None}

  @app.get("/health/{path_echo}")
  def get_health_with_path(path_echo: str, echo: str | None = Query(None)):
      return {"status": "healthy", "echo": echo, "path_echo": path_echo}

  # Person CRUD examples
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

  @app.delete("/persons/{person_id}", status_code=204)
  def delete_person(person_id: str):
      if person_id not in persons_db:
          raise HTTPException(status_code=404, detail="Person not found")
      del persons_db[person_id]

  # Address CRUD examples
  @app.post("/addresses", response_model=AddressRead, status_code=201)
  def create_address(address: AddressCreate):
      import uuid
      new_address = AddressBase(id=str(uuid.uuid4()), **address.model_dump())
      addresses_db[new_address.id] = new_address
      return new_address

  @app.get("/addresses", response_model=list[AddressRead])
  def get_addresses():
      return list(addresses_db.values())
```

### OpenAPI Document (Partial)
docs/OpenAPI_screenshot.png

Screenshot included showing Swagger UI with all endpoints.

## 3. Incomplete Work ❌

None - All planned features were completed.

## 4. OpenAPI Documentation

✅ Successfully generated at http://0.0.0.0:8000/docs
- All endpoints documented with proper schemas
- Request/response models auto-generated from Pydantic classes
- Interactive testing interface available

## 5. Demo Recording

[Link to demo video - https://youtu.be/4j3zvbIkjRw]

## 6. GitHub Repository

https://github.com/Colin-J-Emmanuel/COMSW-4153-Cloud-Computing

---

**Sprint Status:** ✅ COMPLETE
**Date Completed:** September 19, 2025
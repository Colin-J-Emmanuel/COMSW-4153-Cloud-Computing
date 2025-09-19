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
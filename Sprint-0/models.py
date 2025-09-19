from pydantic import BaseModel, Field
from typing import Optional
from datetime import date
import uuid


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


# Response models
class PersonCreate(PersonBase):
    pass


class PersonRead(PersonBase):
    pass


class PersonUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    email: Optional[str] = None
    phone: Optional[str] = None
    birth_date: Optional[date] = None


class AddressCreate(BaseModel):
    street: str
    city: str
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: str


class AddressRead(AddressBase):
    pass


class AddressUpdate(BaseModel):
    street: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None
    postal_code: Optional[str] = None
    country: Optional[str] = None

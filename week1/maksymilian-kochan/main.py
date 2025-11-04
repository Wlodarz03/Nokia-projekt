from pydantic import BaseModel, EmailStr, field_validator, ValidationError, PositiveInt, Field
from typing import Optional

class Address(BaseModel):
    city: str
    street: str
    postal_code: Optional[str] = None

class User(BaseModel):
    id: int = Field(..., gt=0)
    email: EmailStr
    name: str
    age: PositiveInt
    address: Address

    @field_validator("age")
    def validate_age(cls, value):
        if value > 150:
            raise ValueError("Age must be less than or equal to 150")
        return value

def main():
    print("Creating valid User:")
    try:
        user1 = User(
            id=1,
            email="user@example.com",
            name="John Doe",
            age=30,
            address=Address(city="Krakow", street="Szewska")
        )
        print("User1 created successfully.")
        print(user1)
    except ValidationError as e:
        print(e)

    print("\nCreating User with invalid email and age:")
    try:
        user2 = User(
            id=2,
            email="invalid-email",
            name="Jane Doe",
            age=200,
            address=Address(city="Warszawa", street="Jana Pawla II")
        )
        print("User2 created successfully.")
        print(user2)
    except ValidationError as e:
        print(e)

    print("\nCreating User with negative id:")
    try:
        user3 = User(
            id=-1,
            email="address@example.com",
            name="Alice",
            age=25,
            address=Address(city="Chicago", street="Michigan Avenue")
        )
        print("User3 created successfully.")
        print(user3)
    except ValidationError as e:
        print(e)

    print("\nCreating User with age as string:")
    try:
        user4 = User(
            id=3,
            email="address@example.com",
            name="Bob",
            age="40",
            address=Address(city="Wroclaw", street="Dluga", postal_code="50-123")
        )
        print("User4 created successfully.")
        print(user4)
    except ValidationError as e:
        print(e)

    print("\nCreating User with age as string(not integer):")
    try:
        user5 = User(
            id=3,
            email="address@example.com",
            name="Bob",
            age="40b",
            address=Address(city="Wroclaw", street="Dluga", postal_code="50-123")
        )
        print("User5 created successfully.")
        print(user5)
    except ValidationError as e:
        print(e)

    print("\nCreating User with postal_code as integer:")
    try:
        user6 = User(
            id=4,
            email="address@example.com",
            name="Emily",
            age=40,
            address=Address(city="Łódź", street="Piotrkowska", postal_code=54)
        )
        print("User6 created successfully.")
        print(user6)
    except ValidationError as e:
        print(e)

if __name__ == '__main__':
    main()

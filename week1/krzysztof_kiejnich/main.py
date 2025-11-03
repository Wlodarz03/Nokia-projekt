from pydantic import BaseModel, Field, EmailStr, field_validator, ValidationError
from typing import Optional, List
from datetime import datetime


class User(BaseModel):
    id: int
    name: str = Field(..., min_length=2, max_length=50)
    email: EmailStr
    phone: Optional[str] = None
    is_active: bool = True

    @field_validator("name")
    @classmethod
    def name_must_start_capital(cls, v: str):
        if not v[0].isupper():
            raise ValueError("Imię musi zaczynać się wielką literą.")
        return v
    
class Product(BaseModel): 
    id: int 
    name: str = Field(..., min_length=2)
    price: float = Field(..., gt=0)
    tags: List[str] = [] 
    description: Optional[str] = None 
    in_stock: bool = True


class Car(BaseModel):
    id: int
    brand: str = Field(..., min_length=2)
    model: str = Field(..., min_length=1)
    year: int = Field(..., ge=1886, le=datetime.now().year)
    price: float = Field(..., gt=0)
    electric: bool = False

def main():
    try:
        user = User(id=1, name="Adam", email="Adam@przyklad.com", phone="555666777")

        car = Car(
            id=1,
            brand="Tesla",
            model="Model 3",
            year=2024,
            price=219999.99,
            electric=True,
        )

        product = Product(id=1, name="Laptop", price=9999999.99, tags=["electronics"])

    except ValidationError as e:
        print(e)
        

    print("\nBłędne dane (price < 0):")
    try:
        _ = Car(id=1, brand="BMW", model="X5", year=2020, price=-99999999999.0)
    except ValidationError as e:
        print(e)


    print("\nBłędne dane (year > 2025):")
    try:
        _ = Car(id =2, brand ="Audi", model='A1', year = 2050, price=9999999999.0)
    except ValidationError as e:
        print(e)


if __name__ == "__main__":
    main()

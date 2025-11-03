from pydantic import BaseModel, Field, PositiveInt, ValidationError
from typing import Optional, List

class User(BaseModel):
    id : int
    age : PositiveInt
    info : str = Field(..., description='Info o uzytkowniku')
    rank : float = Field(0.0, ge=0.0, le=100.0, description='Ranga nie może być mniejsza niż 0, ale też nie może być zbyt duży')

class Product(BaseModel):
    id : int
    name : str
    price : float = Field(0.0, ge=0.0, description='Cena nie może być ujemna')

class Koszyk(BaseModel):
    id : int
    user : User
    lista_produktow : Optional[List[Product]] = None

def main():
    # poprawne
    user = User(id=1, age=25, info="Student", rank=75.5)
    product1 = Product(id=10, name="Laptop", price=4500.0)
    product2 = Product(id=20, name="Ciastko", price=5.0)
    koszyk = Koszyk(id=100, user=user, lista_produktow=[product1, product2])

    print(koszyk.model_dump_json(indent=2))  # ładny JSON

    #  błędny przypadek (wiek ujemny)
    print("\n Błędne dane (age < 0):")
    try:
        bad_user = User(id=2, age=-5, info="Zły wiek", rank=10)
    except ValidationError as e:
        print(e)
    
    #  błędny przypadek (brak pola 'info')
    print("\n Błędne dane (brak 'info'):")
    try:
        bad_user2 = User(id=3, age=20)
    except ValidationError as e:
        print(e)

    #  błędny przypadek (price < 0)
    print("\n Błędne dane (price < 0):")
    try:
        bad_product = Product(id=5, name="Myszka", price=-15.0)
    except ValidationError as e:
        print(e)


if __name__ == '__main__':
    main()

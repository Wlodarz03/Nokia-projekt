from pydantic import BaseModel, PositiveInt, field_validator
import json


class Product(BaseModel):
    model_config = {
        "validate_default": True # ustawienia modelu - walidacja domyślnie przypisanych wartości
    }

    name: str
    price: float # maybe don't keep money as floats in actual production code
    description: str = "Example of a description."
    tags: list[str]
    note: str | None = None # możliwie puste pole; przypisanie defaultowej wartości

    # użycie field_validator do sprawdzania wartości przypisanych do pól obiektów
    @field_validator('price')
    @classmethod
    def validate_price(cls, p):
        if p < 0:
            raise ValueError("Price cannot be negative")
        return p


    # jakaś funkcja (tutaj silnia) - użycie ograniczenia na wartość numeryczną
    def very_hard_task(self, n: PositiveInt) -> PositiveInt:
        if n == 1:
            return 1
        return n * self.very_hard_task(n - 1)


def main():
    # zczytywanie danych z JSON + walidacja typów
    with open('./products.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    products = [Product.model_validate(p) for p in data['products']]

    print('produkty: ')
    for p in products:
        print(p)
    print('\n')

    if len(products) == 0:
        print('no products loaded')
        return

    # użycie typu PositiveInt
    print('powinno się udać: ', products[0].very_hard_task(3))
    try:
        print('to nigdy się stać nie powinno: ', products[0].very_hard_task(-42))
    except Exception:
        print('zły argument został złapany; pydantic zadziałał dobrze')



if __name__ == '__main__':
    main()


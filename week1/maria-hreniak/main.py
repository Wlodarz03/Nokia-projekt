from pydantic import BaseModel, Field, field_validator

class User(BaseModel):
    id: int
    name: str
    is_active: bool = True


class UserWithRules(BaseModel):
    name: str = Field(min_length=1)           # niepuste imię
    age: int = Field(ge=0, le=120)            # 0..120

    @field_validator("name", mode="before")
    @classmethod
    def strip_name(cls, v: str):
        # przytnij spacje przed walidacją
        return v.strip() if isinstance(v, str) else v


def demo_basic():
    print("== DEMO: User ==")
    u = User(id="42", name="Ala") #rzutowanie
    print(u)
    print(u.model_dump())
    print()


def demo_rules():
    print("== DEMO: UserWithRules ==")
    ok = UserWithRules(name="  Bob  ", age="18") #rzutowanie + strip + ograniczenia
    print(ok)
    try:
        bad = UserWithRules(name="   ", age=-1)
    except Exception as e:
        print("Błąd walidacji:", e)
    print()


if __name__ == "__main__":
    demo_basic()
    demo_rules()

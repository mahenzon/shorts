from typing import TypedDict


class Person(TypedDict):
    name: str
    age: int


person: Person = {
    "name": "Johm",
    "age": 123,
}

print(
    person["name"]
)

age = person["age"]
print(age + 123)

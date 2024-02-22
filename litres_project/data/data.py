import dataclasses


@dataclasses.dataclass
class Book:
    name: str
    author: str
    price: str
    url: str

@dataclasses.dataclass
class User:
    name: str
    email: str
    password: str

from app.database.models import Dog, Toy
from app.database.session import get_session


def add_toy(dog):
    toy = Toy(
        name=name,
        dog=dog
    )
    with get_session() as session:
        session.add(Toy)
        session.commit()


def add_dog(name, date_of_birth, height, weight):
    dog = Dog(
        name=name,
        date_of_birth=date_of_birth,
        height=height,
        weight=weight,
    )
    with get_session() as session:
        session.add(dog)
        session.commit()


def get_all_dogs():
    with get_session() as session:
        dogs = session.query(Dog).all()
    return [dog.name for dog in dogs]


def get_dog(name):
    with get_session() as session:
        dog = session.query(Dog).filter(Dog.name == name).one()
    return dog

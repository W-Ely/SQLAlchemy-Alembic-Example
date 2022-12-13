import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Dog(Base):
    __tablename__ = "dogs"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, index=True)
    date_of_birth = sa.Column(sa.Date)
    height = sa.Column(sa.Float)
    weight = sa.Column(sa.Float)
    toys = relationship("Toy", back_populates="dog")


class Toy(Base):
    __tablename__ = "toys"

    id = sa.Column(sa.Integer, primary_key=True)
    dog_id = sa.Column(sa.ForeignKey("dogs.id"))
    dog = relationship("Dog", back_populates="toys")

import sqlalchemy as sa
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Dog(Base):
    __tablename__ = "dogs"

    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    date_of_birth = sa.Column(sa.Date)
    height = sa.Column(sa.Integer)
    weight = sa.Column(sa.Numeric)

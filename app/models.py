from sqlalchemy.orm import declarative_base, Mapped, mapped_column, relationship
from sqlalchemy import String, DateTime, func, ForeignKey
from typing import List

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(30), unique=True)
    password: Mapped[str] = mapped_column(String(256))
    basket: Mapped[List['Picture']] = relationship(cascade='all')
    pictures: Mapped[str] = mapped_column(ForeignKey('pictures.id'), nullable=True)


class Picture(Base):
    __tablename__ = 'pictures'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    description: Mapped[str] = mapped_column(String(10000))
    uri: Mapped[str] = mapped_column(String(10000))
    # price: Mapped[int]
    collection: Mapped[List['Collection']] = relationship(back_populates='pictures', cascade='all')
    collection_id: Mapped[str] = mapped_column(ForeignKey('collections.id'))
    created_at: Mapped[str] = mapped_column(DateTime(), server_default=func.now())


class Collection(Base):
    __tablename__ = 'collections'
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(200))
    pictures: Mapped[List['Picture']] = relationship(back_populates='collection', cascade='all')

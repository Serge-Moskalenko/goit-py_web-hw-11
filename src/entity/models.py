from typing import Optional
from sqlalchemy import String, Date
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

class Base(DeclarativeBase):
    pass

class Contact(Base):
    __tablename__ = "contacts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    first_name: Mapped[str] = mapped_column(String(20), index=True)
    last_name: Mapped[str] = mapped_column(String(20), index=True)
    email: Mapped[str] = mapped_column(String(20), unique=True, index=True)
    phone: Mapped[str] = mapped_column(String(15))
    birthday: Mapped[Date] = mapped_column(Date)
    additional_info: Mapped[Optional[str]] = mapped_column(String(250), nullable=True)
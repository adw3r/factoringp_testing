import datetime

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Date
from sqlalchemy.orm import declarative_base, relationship, Mapped, mapped_column

Base = declarative_base()

class User(Base):
    """
    `id` - унікальний для кожного запису
    `login` - логін клієнта
    `registration_date` - дата реєстрації клієнта
    """
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    login: Mapped[str] = mapped_column(String(60), unique=True)
    registration_date: Mapped[datetime.date] = mapped_column(Date)

    credits: Mapped[list['Credit']] = relationship('Credit', back_populates='user')

class Credit(Base):
    """
    `id` - унікальний для кожного запису
    `user_id` - id клієнта з таблиці **Users**
    `issuance_date`- дата видачі кредиту
    `return_date` - крайня дата повернення кредиту
    `actual_return_date`- реальна дата повернення кредиту
    `body` - сума видачі
    `percent` - нараховані відсотки
    """
    __tablename__ = 'credits'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    user_id: Mapped[int] = mapped_column(Integer, ForeignKey('users.id'))
    user: Mapped[User] = relationship("User", back_populates="credits")

    issuance_date: Mapped[datetime.date] = mapped_column(Date)
    return_date: Mapped[datetime.date] = mapped_column(Date)
    actual_return_date: Mapped[datetime.date] = mapped_column(Date)
    body: Mapped[float] = mapped_column(Float)
    percent: Mapped[float] = mapped_column(Float)

    payment: Mapped['Payment'] = relationship('Payment', back_populates='credit')

class Category(Base):
    __tablename__ = 'categories'
    """
    `id` - унікальний для кожного запису
    `name` - назва
    """

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(60), unique=True)

    payment: Mapped['Payment'] = relationship('Payment', back_populates='category')
    plan: Mapped['Plan'] = relationship('Plan', back_populates='category')

class Payment(Base):
    __tablename__ = 'payments'
    """
    `id` - унікальний для кожного запису
    `sum` - сума платежу
    `payment_date` - дата платежу
    `credit_id` - id кредиту з таблиці **Credits**
    `type_id` == 'category_id' - id типу платежу (тіло/відсотки) з таблиці **Dictionary**
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    sum: Mapped[float] = mapped_column(Float)
    payment_date: Mapped[datetime.date] = mapped_column(Date)
    credit_id: Mapped[int] = mapped_column(Integer, ForeignKey('credits.id'))
    credit: Mapped[Credit] = relationship('Credit', back_populates='payment')

    category_id: Mapped[int] = mapped_column(Integer, ForeignKey('categories.id'))
    category: Mapped[Category] = relationship('Category', back_populates='payment')

class Plan(Base):
    __tablename__ = 'plans'
    """
    `id` - унікальний для кожного запису
    `period` - місяць планів (перше число місяця)
    `sum` - сума видачі/збору за планом
    `category_id` - id категорії з таблиці **Dictionary**
    """

    id: Mapped[int] = mapped_column(primary_key=True)
    period: Mapped[datetime.date] = mapped_column(Date)
    sum: Mapped[float] = mapped_column(Float)
    category_id: Mapped[int] = Column(Integer, ForeignKey('categories.id'))

    category: Mapped[Category] = relationship('Category', back_populates='plan')

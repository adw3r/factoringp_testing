

from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from src.database.models import User
from src.database.schemas import UserCreate

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user_by_id(self, user_id: int):
        result = await self.session.execute(select(User).filter(User.id == user_id))
        return result.scalars().first()

    async def create_user(self, user_data: UserCreate):
        new_user = User(**user_data.dict())
        self.session.add(new_user)
        await self.session.commit()
        await self.session.refresh(new_user)
        return new_user


class PlanRepo:
    pass

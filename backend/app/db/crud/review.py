from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Review

class ReviewCrud:
    # 제목 검색
    @staticmethod
    async def get_by_title(db:AsyncSession, title:str) -> Review | None:
        result = await db.execute(select(Review).filter(Review.title.like(f'%{title}%')))
        return result.scalars().all()

    # 내용 검색
    @staticmethod
    async def get_by_description(db:AsyncSession, description:str) -> Review | None:
        result = await db.execute(select(Review).filter(Review.description.like(f'%{description}%')))
        return result.scalars().all()

    # 작성된 시간 검색
    @staticmethod
    async def get_by_created(db:AsyncSession, created_from:datetime, created_to:datetime) -> Review | None:
        result = await db.execute(select(Review).filter(Review.created_at > created_from, Review.created_at < created_to))
        return result.scalars().all()

    # 전체 불러오기
    @staticmethod
    async def get_all(db:AsyncSession) -> Review | None:
        result = await db.execute(select(Review))
        return result.scalars().all()


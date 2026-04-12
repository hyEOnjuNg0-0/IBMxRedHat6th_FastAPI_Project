from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Review, Cocktail
from app.db.scheme.reviews import ReviewCreate

class ReviewCrud:
    # 리뷰 작성
    @staticmethod
    async def create_review(db: AsyncSession, review: ReviewCreate) -> Review | None:
        db_review = Review(**review.model_dump())
        db.add(db_review)
        await db.flush()
        return db_review

    # 칵테일 id로 검색
    @staticmethod
    async def get_by_id(db: AsyncSession, review_id:int) -> Review | None:
        result = await db.execute(select(Review).filter(Review.review_id==review_id))
        return result.scalar_one_or_none()

    # 칵테일 id로 검색
    @staticmethod
    async def get_by_cocktail_id(db: AsyncSession, cocktail_id:int) -> Review | None:
        result = await db.execute(select(Review).filter(Review.cocktail_id==cocktail_id))
        return result.scalar_one_or_none()

    # 회원 id로 검색
    @staticmethod
    async def get_by_user_id(db: AsyncSession, user_id: int) -> Review | None:
        result = await db.execute(select(Review).filter(Review.user_id==user_id))
        return result.scalars().all()

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

    # 리뷰 수정하기
    @staticmethod
    async def update_by_id(db:AsyncSession, review_id:int, review:Review) -> Review | None:
        db_review = await db.get(Review, review_id)
        if db_review:
            update_data = review.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(db_review, key, value)
            await db.flush()
            return db_review
        return None
from datetime import datetime

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.db.crud.review import ReviewCrud
from app.db.models import Review
from app.db.scheme.reviews import ReviewRead, ReviewCreate, ReviewCreateDB


class ReviewService:
    # 리뷰 작성
    @staticmethod
    async def create_review(db: AsyncSession, cocktail_id: int, user_id: int, review: ReviewCreate):
        # title, description을 DB에 저장
        created_review = ReviewCreateDB(
            title=review.title,
            description=review.description,
            user_id=user_id,
            cocktail_id=cocktail_id,
            created_at=datetime.now())

        try:
            db_review = await ReviewCrud.create_review(db, created_review)
            await db.commit()
            await db.refresh(db_review)
            return db_review

        except Exception as e:
            await db.rollback()
            print(e)
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="올바른 제목과 내용을 적어주세요")

    # 특정 술 리뷰 조회
    @staticmethod
    async def get_reviews_by_cocktail(db: AsyncSession, cocktail_id: int) -> Review | None:
        return await ReviewCrud.get_by_cocktail_id(db, cocktail_id)

    # 로그인한 회원의 리뷰 전체 조회
    @staticmethod
    async def get_my_reviews(db: AsyncSession, user_id: int) -> Review | None:
        return await ReviewCrud.get_by_user_id(db, user_id)

    # 리뷰 수정
    @staticmethod
    async def update_review(db: AsyncSession, review_id: int, review: ReviewRead) -> Review | None:
        db_review = await ReviewCrud.get_by_id(db, review_id)
        if not db_review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="일치하는 리뷰를 찾을 수 없습니다")

        updated_review = ReviewRead(title=review.title, description=review.description)

        try:
            db_review = await ReviewCrud.update_by_id(db, review_id, updated_review)
            await db.commit()
            await db.refresh(db_review)
            return db_review

        except Exception:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="올바른 제목과 내용을 적어주세요")

    # 리뷰 삭제
    @staticmethod
    async def delete_review(db: AsyncSession, review_id: int) -> dict:
        db_review = await ReviewCrud.get_by_id(db, review_id)
        if not db_review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="일치하는 리뷰를 찾을 수 없습니다")

        try:
            await db.delete(db_review)
            await db.commit()
            return {"message" : "리뷰가 성공적으로 삭제되었습니다."}

        except Exception as e:
            print(e)
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="올바른 제목과 내용을 적어주세요")
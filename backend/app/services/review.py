from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.db.crud.review import ReviewCrud
from app.db.models import Review
from app.db.scheme.reviews import ReviewRead, ReviewCreate


class ReviewService:
    # 리뷰 작성
    @staticmethod
    async def create_review(cocktail_id:int, db: AsyncSession, review: ReviewCreate):
        # title, description을 DB에 저장
        created_review = ReviewCreate(title=review.title, description=review.description)

        try:
            db_review = await ReviewCrud.create_review(db, created_review)
            await db.commit()
            await db.refresh(db_review)
            return db_review

        except Exception:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="올바른 제목과 내용을 적어주세요")

    # 리뷰 수정
    @staticmethod
    async def update_review(db: AsyncSession, review_id: int, review: ReviewRead) -> Review:
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
            await db.refresh(db_review)
            return {"message" : "리뷰가 성공적으로 삭제되었습니다."}

        except Exception:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="올바른 제목과 내용을 적어주세요")
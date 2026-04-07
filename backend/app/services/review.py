from sqlalchemy.ext.asyncio import AsyncSession
from fastapi import HTTPException, status
from app.db.crud.review import ReviewCrud
from app.db.models import Review
from app.db.scheme.reviews import ReviewRead


class ReviewService:
    @staticmethod
    async def get_review_by_id(db: AsyncSession, review_id: int, review: ReviewRead) -> Review:
        db_review = await ReviewCrud.get_by_id(db, review_id)
        if not db_review:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="게시글을 찾을 수 없습니다")

        updated_review = ReviewRead(title=review.title, description=review.description)

        try:
            db_review = await ReviewCrud.update_by_id(db, review_id, updated_review)
            await db.commit()
            await db.refresh(db_review)
            return db_review

        except Exception:
            await db.rollback()
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="올바른 제목과 내용을 적어주세요")

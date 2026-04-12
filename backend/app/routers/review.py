from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.scheme.reviews import ReviewRead
from app.services.review import ReviewService

router = APIRouter(prefix="/reviews", tags=["Review"])

'''리뷰 수정'''
@router.put("/{review_id}", response_model=ReviewRead)
async def update_review(review_id:int, review: ReviewRead, db: AsyncSession = Depends(get_db)):
    return await ReviewService.update_review(db, review_id, review)

'''리뷰 삭제'''
@router.delete("/{review_id}")
async def delete_review(review_id: int, db: AsyncSession = Depends(get_db)):
    return await ReviewService.delete_review(db, review_id)
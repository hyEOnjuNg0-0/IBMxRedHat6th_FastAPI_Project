from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from app.db.database import get_db
from app.db.scheme.reviews import ReviewRead
from app.services.review import ReviewService

router = APIRouter(prefix="/reviews", tags=["Review"])

'''리뷰 수정'''
@router.put("/{review_id}", response_model=ReviewRead)
async def update_review(review_id:int, review: ReviewRead, db: AsyncSession = Depends(get_db)):
    return await ReviewService.get_review_by_id(db, review_id, review)

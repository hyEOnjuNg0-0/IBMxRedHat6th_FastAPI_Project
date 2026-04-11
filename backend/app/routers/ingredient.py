from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.scheme.ingredients import IngredientRead, IngredientCreate
from app.db.database import get_db
from app.services import IngredientService


router=APIRouter(prefix="/ingredients", tags=["Ingredient"])

# 새 재료 등록
@router.post("", response_model=IngredientRead)
async def create_ingredient(
    ingredient: IngredientCreate,
    db: AsyncSession = Depends(get_db),
):
    return await IngredientService.create_ingredient(db, ingredient)
    

# 재료 삭제
@router.delete("/{ingredient_id}")
async def delete_ingredient(
    ingredient_id: int,
    db: AsyncSession = Depends(get_db),
):
    await IngredientService.delete_ingredient(db, ingredient_id)
    return {"message": "재료가 삭제되었습니다"}
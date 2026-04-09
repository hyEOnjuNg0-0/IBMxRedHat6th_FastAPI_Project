from fastapi import APIRouter, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.services import CocktailService, CocktailIngredientService
from app.db.scheme.cocktails import CocktailCreate, CocktailUpdate, CocktailListRead, CocktailDetail
from app.db.scheme.cocktail_ingredients import CocktailIngredientCreate
from app.db.scheme.ingredients import IngredientRead


router = APIRouter(prefix="/cocktails", tags=["Cocktail"])


# response_model : 클라이언트에게 최종적으로 보여줄 응답 데이터 구조
# 전체 칵테일 목록 조회
@router.get("", response_model=list[CocktailListRead])
@router.get("", response_model=list[CocktailListRead])
async def get_all_cocktails(db: AsyncSession = Depends(get_db)):
    return await CocktailService.get_all_cocktails(db)


# 새 칵테일 등록
@router.post("", response_model=CocktailDetail)
async def create_cocktail(
    cocktail: CocktailCreate,
    db: AsyncSession = Depends(get_db),
):
    return await CocktailService.create_cocktail(db, cocktail)


# 특정 칵테일 정보 상세 조회
@router.get("/{cocktail_id}", response_model=CocktailDetail)
async def get_cocktail(
    cocktail_id: int,
    db: AsyncSession = Depends(get_db),
):
    return await CocktailService.get_cocktail(db, cocktail_id)


# 특정 칵테일 정보 수정
@router.put("/{cocktail_id}", response_model=CocktailDetail)
async def update_cocktail(
    cocktail_id: int,
    cocktail_data: CocktailUpdate,
    db: AsyncSession = Depends(get_db),
):
    return await CocktailService.update_cocktail(
        db,
        cocktail_id,
        cocktail_data,
    )


# 특정 칵테일 삭제
@router.delete("/{cocktail_id}")
async def delete_cocktail(
    cocktail_id: int,
    db: AsyncSession = Depends(get_db),
):
    await CocktailService.delete_cocktail(db, cocktail_id)
    return {"message": "칵테일이 삭제되었습니다"}


# 특정 칵테일 재료 조회
@router.get("/{cocktail_id}/ingredients", response_model=list[IngredientRead])
async def get_ingredients_by_cocktail_id(
    cocktail_id: int,
    db: AsyncSession = Depends(get_db),
):
    return await CocktailIngredientService.get_ingredients_by_cocktail_id(db, cocktail_id)


# 특정 칵테일 재료 추가
@router.post("/{cocktail_id}/ingredients", response_model=CocktailIngredientRead)
async def add_cocktail_ingredient(
    cocktail_id: int,
    cocktail_ingredient: CocktailIngredientCreate,
    db: AsyncSession = Depends(get_db),
):
    return await CocktailIngredientService.create_cocktail_ingredient(
        db, 
        cocktail_id, 
        cocktail_ingredient.ingredient_id
        )


# 특정 칵테일 재료 제거
@router.delete("/{cocktail_id}/ingredients/{ingredient_id}")
async def delete_cocktail_ingredient(
    cocktail_id: int,
    ingredient_id: int,
    db: AsyncSession = Depends(get_db),
):
    await CocktailIngredientService.delete_cocktail_ingredient(db, cocktail_id, ingredient_id)
    return {"message": "칵테일 재료가 삭제되었습니다"}
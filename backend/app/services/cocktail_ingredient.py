from sqlalchemy.ext.asyncio import AsyncSession
from app.db.models import CocktailIngredient, Ingredient
from app.db.scheme.cocktail_ingredients import CocktailIngredientCreate
from app.db.crud import CocktailIngredientCrud, CocktailCrud
from fastapi import HTTPException

# crud는 db 쿼리, service는 비지니스 로직
class CocktailIngredientService:
    # 특정 칵테일에 새 재료 등록
    @staticmethod
    async def create_cocktail_ingredient(
        db:AsyncSession, 
        cocktail_id:int,
        ingredient_id:int) -> CocktailIngredient:
        try:
            new_cocktail_ingredient = await CocktailIngredientCrud.create(db, cocktail_id, ingredient_id)
            await db.commit()
            await db.refresh(new_cocktail_ingredient)
            return new_cocktail_ingredient
        except Exception:
            await db.rollback()
            raise

    # 특정 칵테일 재료 조회
    @staticmethod
    async def get_ingredients_by_cocktail_id(db: AsyncSession, cocktail_id: int) -> list[Ingredient]:
        cocktail = await CocktailCrud.get_by_id(db, cocktail_id)

        if not cocktail:
            raise HTTPException(status_code=404, detail="존재하지 않는 칵테일")

        return await CocktailIngredientCrud.get_ingredients_by_cocktail_id(db, cocktail_id)
    
    
    # 특정 칵테일 재료 삭제
    @staticmethod
    async def delete_cocktail_ingredient(db: AsyncSession, cocktail_id: int, ingredient_id: int) -> CocktailIngredient:
        cocktail_ingredient = await CocktailIngredientCrud.delete(db, cocktail_id, ingredient_id)

        if not cocktail_ingredient:
            raise HTTPException(404, "존재하지 않는 재료 관계")

        await db.commit()

    
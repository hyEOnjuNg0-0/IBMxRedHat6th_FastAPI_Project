from pydantic import BaseModel

class CocktailIngredientBase(BaseModel):
    cocktailIngredient_id:int

class CocktailIngredientCreate(CocktailIngredientBase):
    pass

class CocktailIngredientInDB(CocktailIngredientBase):
    ingredient_id:int
    cocktail_id:int

    class Config:
        from_attributes = True

class CocktailIngredientRead(CocktailIngredientInDB):
    pass

from pydantic import BaseModel

class CocktailIngredientCreate(BaseModel):
    ingredient_id: int

class CocktailIngredientRead(BaseModel):
    cocktail_id: int
    ingredient_id: int

    class Config:
        from_attributes = True
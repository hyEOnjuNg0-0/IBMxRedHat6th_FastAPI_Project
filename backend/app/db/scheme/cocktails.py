from pydantic import BaseModel


class IngredientSimple(BaseModel):
    ingredients_id: int
    ingredients_name: str

    class Config:
        from_attributes = True

class CocktailBase(BaseModel):
    cocktail_name:str

class CocktailCreate(CocktailBase):
    pass

class CocktailInDB(CocktailBase):
    cocktail_id:int

    class Config:
        from_attributes = True

class CocktailRead(CocktailInDB):
    ingredients: list[IngredientSimple] = []

from pydantic import BaseModel

class CocktailBase(BaseModel):
    cocktail_name:str

class CocktailCreate(CocktailBase):
    cocktail_base:str
    cocktail_detail:str

class CocktailInDB(CocktailBase):
    cocktail_id:int
    cocktail_base:str
    cocktail_detail:str

    class Config:
        from_attributes = True

class CocktailRead(CocktailInDB):
    pass

class CocktailDetailRead(CocktailInDB):
    pass

class CocktailUpdate(CocktailInDB):
    pass
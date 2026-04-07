from pydantic import BaseModel

class CocktailBase(BaseModel):
    cocktail_name:str

class CocktailCreate(CocktailBase):
    cocktail_base:str
    cocktail_detail:str
    pass

class CocktailInDB(CocktailBase):
    cocktail_id:int

    class Config:
        from_attributes = True

class CocktailRead(CocktailInDB):
    cocktail_name:str 

class CocktailDetailRead(CocktailInDB):
    cocktail_name:str
    cocktail_base:str
    cocktail_detail:str

class CocktailUpdate(CocktailInDB):
    cocktail_base:str
    cocktail_detail:str
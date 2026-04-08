from pydantic import BaseModel

class CocktailBase(BaseModel):
    cocktail_name:str

class CocktailCreate(CocktailBase):
    cocktail_base:str
    cocktail_detail:str

class CocktailDetail(CocktailBase):
    cocktail_id:int
    cocktail_base:str
    cocktail_detail:str
    cocktail_base:str
    cocktail_detail:str

    class Config:
        from_attributes = True

class CocktailRead(CocktailBase):
    pass

    class Config:
        from_attributes = True
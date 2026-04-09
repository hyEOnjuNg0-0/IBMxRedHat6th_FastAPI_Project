from pydantic import BaseModel

class CocktailBase(BaseModel):
    cocktail_name:str

class CocktailCreate(CocktailBase):
    cocktail_base:str
    cocktail_detail:str

class CocktailUpdate(BaseModel):
    cocktail_name:str | None = None    
    cocktail_base:str | None = None
    cocktail_detail:str | None = None

class CocktailListRead(CocktailBase):
    cocktail_id: int

    class Config:
        from_attributes = True


class CocktailDetail(CocktailListRead):
    cocktail_base: str
    cocktail_detail: str
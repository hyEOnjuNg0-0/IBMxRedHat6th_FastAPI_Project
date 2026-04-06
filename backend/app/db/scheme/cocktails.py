from pydantic import BaseModel

class CocktailBase(BaseModel):
    cocktail_name:str

class CocktailCreate(CocktailBase):
    pass

class CocktailUpdate(BaseModel):
    # 기주
    # 설명
    pass

class CocktailInDB(CocktailBase):
    cocktail_id:int

    class Config:
        from_attributes = True

class CocktailRead(CocktailInDB):
    cocktail_name : str 

class CocktailDetailRead(CocktailInDB):
    # 모든 정보
    pass
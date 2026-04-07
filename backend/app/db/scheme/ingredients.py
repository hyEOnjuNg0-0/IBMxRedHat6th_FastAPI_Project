from pydantic import BaseModel

class IngredientBase(BaseModel):
    ingredient_name:str

class IngredientCreate(IngredientBase):
    pass

class IngredientRead(IngredientBase):
    ingredient_id:int
    ingredient_name:str

    class Config:
        from_attributes = True
    
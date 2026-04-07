from pydantic import BaseModel

class IngredientBase(BaseModel):
    ingredient_name:str

class IngredientCreate(IngredientBase):
    pass

class IngredientRead(IngredientBase):
    ingredient_id:int

    class Config:
        from_attributes = True
    
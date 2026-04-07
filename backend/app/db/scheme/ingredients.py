from pydantic import BaseModel

class IngredientsBase(BaseModel):
    ingredient_name:str

class IngredientsCreate(IngredientsBase):
    pass

class IngredientsInDB(IngredientsBase):
    ingredient_id:int

    class Config:
        from_attributes = True

class IngredientsRead(IngredientsInDB):
    ingredient_name:str
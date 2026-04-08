from pydantic import BaseModel

class FavoritesCreate(BaseModel):
    Favorite_id:int

class FavoritesRead(BaseModel):
    user_id:int
    cocktail_id:int

    class Config:
        from_attributes = True

from pydantic import BaseModel

class FavoritesBase(BaseModel):
    Favorite_id:int

class FavoritesCreate(FavoritesBase):
    pass

class FavoritesInDB(FavoritesBase):
    user_id:int
    cocktail_id:int

    class Config:
        from_attributes = True

# class FavoritesRead(FavoritesInDB):
#     cocktail_id:int 
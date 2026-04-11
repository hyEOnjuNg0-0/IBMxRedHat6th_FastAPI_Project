from pydantic import BaseModel

class FavoriteRead(BaseModel):
    user_id: int
    cocktail_id: int

    class Config:
        from_attributes = True

# class FavoritesBase(BaseModel):
#     Favorite_id:int

# class FavoritesCreate(FavoritesBase):
#     pass

# class FavoritesInDB(FavoritesBase):
#     user_id:int
#     cocktail_id:int

#     class Config:
#         from_attributes = True


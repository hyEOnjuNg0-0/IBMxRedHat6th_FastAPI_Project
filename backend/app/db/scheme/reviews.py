from pydantic import BaseModel
from datetime import datetime

class ReviewBase(BaseModel):
    title:str
    description:str|None=None

class ReviewCreate(ReviewBase):
    pass

class ReviewInDB(ReviewBase):
    review_id:int
    user_id:int
    cocktail_id:int
    created_at:datetime

    class Config:
        from_attributes = True

class ReviewRead(ReviewBase):
    pass
#히히
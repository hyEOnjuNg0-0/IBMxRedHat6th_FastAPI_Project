from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import Cocktail
from app.db.scheme.cocktails import CocktailCreate, CocktailUpdate

class CocktailCrud:
    # 전체 칵테일 조회
    @staticmethod
    async def get_all(db:AsyncSession) -> list[Cocktail]:
        query = select(Cocktail).order_by(Cocktail.cocktail_id.desc())
        result=await db.execute(query)
        return result.scalars().all()
    
    # 특정 칵테일 정보 상세 조회
    @staticmethod
    async def get_by_id(db: AsyncSession, cocktail_id: int) -> Cocktail | None:
        result = await db.execute(select(Cocktail).where(Cocktail.cocktail_id == cocktail_id))
        return result.scalar_one_or_none()
    
    # 칵테일 생성
    # 요청으로 들어온 cocktail 데이터를 Cocktail ORM 객체로 만들어 DB에 넣는 함수
    # model_dump() : Pydantic 객체 -> dict
    @staticmethod
    async def create(db:AsyncSession, cocktail:CocktailCreate) -> Cocktail:
        new_cocktail = Cocktail(**cocktail.model_dump())
        db.add(new_cocktail)
        await db.flush()
        return new_cocktail
    
    # 특정 칵테일 정보 수정
    @staticmethod
    async def update(db: AsyncSession, cocktail_id: int, cocktail_data: CocktailUpdate) -> Cocktail | None:
        cocktail = await CocktailCrud.get_by_id(db, cocktail_id)

        if not cocktail:
            return None
        
        update_data = cocktail_data.model_dump(exclude_unset=True)

        for key, value in update_data.items():
            setattr(cocktail, key, value)  # cocktail.key = value

        await db.flush()
        return cocktail

    # 칵테일 삭제
    @staticmethod
    async def delete(db: AsyncSession, cocktail_id: int) -> Cocktail | None:
        cocktail = await CocktailCrud.get_by_id(db, cocktail_id)

        if not cocktail:
            return None

        await db.delete(cocktail)
        await db.flush()
        return cocktail

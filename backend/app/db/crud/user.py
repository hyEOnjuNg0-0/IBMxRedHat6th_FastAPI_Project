from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.db.models import User
from app.db.scheme.users import UserCreate, UserUpdate

# User 테이블과 관련된 CRUD 작업을 모아둔 클래스
class UserCrud:
    @staticmethod
    async def get_by_id(db: AsyncSession, user_id: int) -> User | None:
        result = await db.execute(select(User).filter(User.user_id == user_id))
        return result.scalar_one_or_none()

    @staticmethod
    async def create(db: AsyncSession, user: UserCreate) -> User:
        db_user = User(**user.model_dump())
        db.add(db_user)
        await db.flush()
        return db_user

    # UserUpdate는 scheme/users.py에 위치
    @staticmethod
    async def update_by_id(db: AsyncSession, user_id: int, user:UserUpdate) -> User|None:
        # db에서 사용자id로 검색하여 사용자 불러오기
        db_user = await db.get(User, user_id)
        # 일치하는 사용자가 있다면
        if db_user:
            # pydantic에서 명시된 필드만 추출해서 dict로 변환
            update_data = user.model_dump(exclude_unset=True)
            # update_data.items() : dict의 요소를 key-value 짝으로 하나씩 추출
            # key, value 두 개의 인자 : 언패킹, {key : value}가 각각 들어감
            for key, value in update_data.items():
                # db_user.key = value와 동일
                setattr(db_user, key, value)
            await db.flush()
            return db_user
        return None

    @staticmethod
    async def delete_by_id(db: AsyncSession, user_id: int) -> User | None:
        # 삭제 전 객체를 가져와서 삭제
        db_user = await db.get(User, user_id)
        if db_user:
            await db.delete(db_user)
            await db.flush()
            return db_user
        return None

    @staticmethod
    async def get_by_username(db: AsyncSession, username: str) -> User | None:
        result = await db.execute(select(User).filter(User.username == username))
        return result.scalar_one_or_none()

    @staticmethod
    async def get_by_email(db: AsyncSession, email: str) -> User | None:
        result = await db.execute(select(User).filter(User.email == email))
        return result.scalar_one_or_none()

    @staticmethod
    async def update_refresh_token_by_id(db:AsyncSession, user_id: int, refresh_token: str):
        db_user = await db.get(User, user_id)
        if db_user:
            db_user.refresh_token = refresh_token
            await db.flush()
        return db_user
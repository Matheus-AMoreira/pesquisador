import asyncpg
from typing_extensions import Optional


class Database:
    pool: Optional[asyncpg.Pool] = None

    async def connect(self, dsn: str):
        if self.pool is None:
            self.pool = await asyncpg.create_pool(dsn=dsn)

    async def disconnect(self):
        if self.pool:
            await self.pool.close()

    async def fetch(self, query: str, *args):
        if self.pool is None:
            raise RuntimeError("Database pool não foi iniciado.")
        async with self.pool.acquire() as conn:
            return await conn.fetch(query, *args)


db = Database()

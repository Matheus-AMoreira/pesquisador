from src.db.conexao import db


class OfertaRepository:
    @staticmethod
    async def buscar_ofertas():
        query = "SELECT * FROM view_ofertas_ia"
        records = await db.fetch(query)
        return records

from typing import List, Optional

from pydantic import BaseModel, Field


class OfertasSchema(BaseModel):
    """
    Retorno do banco com informações dos pacotes e suas ofertas, aqui tem localizção, preço e data
    """

    pacote_nome: str = Field(description="O nome do pacote que contem as ofertas")
    descricao: Optional[str] = Field(description="Breve descrição do pacote")
    oferta_nome: str = Field(
        description="O o nome da oferta a qual se refere ao nome do pacote"
    )
    pacote_tags: Optional[List[str]] = Field(
        description="Algumas tags básicas para entendimento do pacote"
    )
    hotel_nome: Optional[str] = Field(
        description="O nome do hotel ao qual a oferta garante"
    )
    transporte_nome_empresa: Optional[str] = Field(
        description="O nome da empresa de transporte"
    )
    transporte_meio: Optional[str] = Field(
        description="O meio pelo qual será feito a viagem"
    )
    cidade: Optional[str] = Field(
        description="A cidade onde ocorrerá a viagem que está ligado a localização do hotel"
    )
    estado: Optional[str] = Field(description="O estado ao qual a cidade pertence")

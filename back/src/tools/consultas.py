from langchain_core.tools import tool
from typing_extensions import List

from src.repository.ofertas import OfertaRepository
from src.schemas.ofertas import OfertasSchema


@tool
def search_pdf_documents():
    """
    Consulta de lista de documentos para auxiliar no atendimento, Função não implementada, avisar ao usuário
    """
    print("tentou ler pdf")


@tool
async def ofertas():
    """
    lista completa de pacotes e ofertas disponiveis, sendo que um pacote pode contem diferentes ofertas em datas e condições diferentes.
    Use essa feramenta para procurar por locais de viagems
    """
    print("tentou buscar oferta")

    lista_ofertas: List[OfertasSchema] = await OfertaRepository.buscar_ofertas()
    print(lista_ofertas)
    if not lista_ofertas:
        return "No momento não tem nenhum pacote disponivel."

    return lista_ofertas


@tool
def call_funcionario():
    """
    Caso o usuário tente sair do assunto de viagem,promoções e outros serviços da agência ou falte informação para satisfazer o usuário,
    um funcionário deverá ser chamada para resolver.
    """
    print("usuário foi chamado")
    return "Informe ao usuário de que um funcionário irá atende-lo e que deve ficar no aguardo "

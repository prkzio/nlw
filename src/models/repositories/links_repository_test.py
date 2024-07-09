import pytest
import uuid 
from src.models.settings.db_connection_handler import db_connection_handler
from .links_repository import Links

db_connection_handler.connect()
trip_id = str(uuid.uuid4())

#@pytest.mark.skip(reason="interacao com o banco")
def test_link():
    conn = db_connection_handler.get_connection()
    links = Links(conn)

    links_infos = {
        "id":str(uuid.uuid4()),
        "trip_id": trip_id,
        "link": "www.LinkTeste.com.br"
    }

    links.link(links_infos)

#@pytest.mark.skip(reason="interacao com o banco")
def test_links_from_trip():
    conn = db_connection_handler.get_connection()
    links = Links(conn)

    links = links.find_links_from_trip(trip_id)
    print()
    print(links)

from decimal import Decimal
from typing import List

from ninja import Schema


class artistname(Schema):
    name: str


class albumOut(Schema):
    name: str
    year: str
    artirst: artistname
    songs: List[str]


class artistOut(Schema):
    name: str
    albums: List[str]


class SongOut(Schema):
    name: str
    duration: str
    year: Decimal
    album: albumOut
    artirst: artistOut


class FourOFourOut(Schema):
    detail: str

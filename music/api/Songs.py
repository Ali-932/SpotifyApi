from typing import List

from ninja import Router,Form
from rest_framework import status
from music.schemas import SongOut, FourOFourOut,albumOut,artistOut
from music.models import song,album,artirst

songRouter = Router()


@songRouter.get('/songsOUT', response={
    status.HTTP_200_OK: List[SongOut]
    ,status.HTTP_404_NOT_FOUND:FourOFourOut})
def Songout(request):
    songs = song.objects.all()
    return status.HTTP_200_OK, songs


@songRouter.get('/Album_out',response={
    status.HTTP_200_OK: albumOut
    ,status.HTTP_404_NOT_FOUND:FourOFourOut})
def Albumout(request, name:str):
    albums=album.objects.get(name=name)
    songs=albums.song_album.values_list('name',flat=True)
    return status.HTTP_200_OK,{'name':albums.name,'year':albums.year,'artirst':albums.artirst,'songs':list(songs)}

@songRouter.get('/ArtiestOut',response={
    status.HTTP_200_OK:List[artistOut],
    status.HTTP_404_NOT_FOUND:FourOFourOut
})
def ArtiestOut(request):
    Artiest=artirst.objects.all()
    result = []
    for a in Artiest:
        result.append({
            'name':a.name,
            'albums':list(a.albums.values_list('name',flat=True))
        })
    print(result)

    return status.HTTP_200_OK,result
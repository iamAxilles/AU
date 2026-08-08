from fastapi import FastAPI, Query, Path
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
#from fastapi.staticfiles import StaticFiles

import json, httpx
from fastapi.requests import Request

from fastapi import APIRouter

from typing import Annotated, Union, Optional
from pydantic import BaseModel
from datetime import datetime

from encar import O
from water.airwater import run


cars = APIRouter(prefix="/cars")##



class Brands(BaseModel):
    bmw: Optional[str] = None
    benz: Optional[str] = None


#@api.get("/items")
#def read_item(q, b, c: Union[str, None] = None):
#    return { q, b, c }


@cars.get("/cars")
def Brands(b: Annotated[Brands, Query()]):

    match b.bmw:
        case '3':
            return 'bmw 3'
        case '5':
            return 'bmw 5'

    match b.benz:
        case 'CLS':
            return 'cls'
        case 'G':
            return 'G'


h = {
    'User-Agent': 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
    'Referer': 'https://www.encar.com/'
            }
# "Referer": 'https://ci.encar.com'
mozilla = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:152.0) Gecko/20100101 Firefox/152.0',
    'Referer': 'https://www.encar.com/'
}


async def raQ(go):
    async with httpx.AsyncClient(headers=h) as cl:
        resp = await cl.get(go)
        print(resp.status_code)
        return resp.json()

async def srQ(go):
    async with httpx.AsyncClient(headers=h) as cl:
        resp = await cl.get(go)
        print(resp.status_code)
        r = resp.json()
        return r['SearchResults']
#def reQue(get):
#    re = requests.get(get)
#    return re.json()

#imitaion
@cars.get("/bmw={model}-{k}/{p}")
async def bmw(model: str, k:str, p:int):

    # bmw3 = await raQ('http://localhost:8000/encar/bmw3')
    bmw3 = await run('http://localhost:8000/encar/bmw3')
    bmw32 = await raQ('http://localhost:8000/encar/bmw32')
    bmw33 = await raQ('http://localhost:8000/encar/bmw33')

    if model=='3'and k=='er'and p==1:
        return bmw3
    if model=='3'and k=='er'and p==2:
        return bmw32
    if model=='3'and k=='er'and p==3:
        return bmw33

    if model=='3'and p==1 and k=='G20':
        G20 = [g for g in bmw3 if'(G20)'in g["Model"]]
        return G20
    if model=='3'and p==2 and k=='G20':
        G20 = [g for g in bmw32 if'(G20)'in g["Model"]]
        return G20
    if model=='3'and p==3 and k=='G20':
        G20 = [g for g in bmw32 if'(G20)'in g["Model"]]
        return G20

    if model=='3'and p==1 and k=='F30':
        F30 = [f for f in bmw3 if'(F30)'in f["Model"]]
        return F30
    if model=='3'and p==2 and k=='F30':
        F30 = [f for f in bmw32 if'(F30)'in f["Model"]]
        return F30
    if model=='3'and p==3 and k=='F30':
        F30 = [f for f in bmw33 if'(F30)'in f["Model"]]
        return F30

    if model=='3'and p==1 and k=='E90':
        E90 = [e for e in bmw3 if'(E90)'in e["Model"]]
        return E90
    if model=='3'and p==2 and k=='E90':
        E90 = [e for e in bmw32 if'(E90)'in e["Model"]]
        return E90
    if model=='3'and p==3 and k=='E90':
        E90 = [e for e in bmw33 if'(E90)'in e["Model"]]
        return E90

    if model=='3'and k=='06':
        old = list(filter(lambda w:w["Model"]=='3시리즈', bmw3[:]))
        return old



@cars.get("/benz={model}-{k}/{p}")
async def benz(model: str, k:str, p:int):
    C = await raQ('http://localhost:8000/encar/benz=C')
    C2 = await raQ('http://localhost:8000/encar/benz=C2')
    C3 = await raQ('http://localhost:8000/encar/benz=C3')
    C4 = await raQ('http://localhost:8000/encar/benz=C4')
    C5 = await raQ('http://localhost:8000/encar/benz=C5')

    if model=='C'and k=='kl'and p==1:
        return C
    if model=='C'and k=='kl'and p==2:
        return C2
    if model=='C'and k=='kl'and p==3:
        return C3
    if model=='C'and k=='kl'and p==4:
        return C4
    if model=='C'and k=='kl'and p==5:
        return C5

    if model=='C'and p==1 and k=='W206':
        W206 = [w6 for w6 in C if'W206'in w6["Model"]]
        return W206
    if model=='C'and p==2 and k=='W206':
        W206 = [w6 for w6 in C2 if'W206'in w6["Model"]]
        return W206
    if model=='C'and p==3 and k=='W206':
        W206 = [w6 for w6 in C3 if'W206'in w6["Model"]]
        return W206
    if model=='C'and p==4 and k=='W206':
        W206 = [w6 for w6 in C4 if'W206'in w6["Model"]]
        return W206
    if model=='C'and p==5 and k=='W206':
        W206 = [w6 for w6 in C5 if'W206'in w6["Model"]]
        return W206

    if model=='C'and p==1 and k=='W205':
        W205 = [w5 for w5 in C if'W205'in w5["Model"]]
        return W205
    if model=='C'and p==2 and k=='W205':
        W205 = [w5 for w5 in C2 if'W205'in w5["Model"]]
        return W205
    if model=='C'and p==3 and k=='W205':
        W205 = [w5 for w5 in C3 if'W205'in w5["Model"]]
        return W205
    if model=='C'and p==4 and k=='W205':
        W205 = [w5 for w5 in C4 if'W205'in w5["Model"]]
        return W205
    if model=='C'and p==5 and k=='W205':
        W205 = [w5 for w5 in C5 if'W205'in w5["Model"]]
        return W205

    if model=='C'and p==1 and k=='W204':
        W204 = [w4 for w4 in C if'W204'in w4["Model"]]
        return W204
    if model=='C'and p==2 and k=='W204':
        W204 = [w4 for w4 in C2 if'W204'in w4["Model"]]
        return W204
    if model=='C'and p==3 and k=='W204':
        W204 = [w4 for w4 in C3 if'W204'in w4["Model"]]
        return W204
    if model=='C'and p==4 and k=='W204':
        W204 = [w4 for w4 in C4 if'W204'in w4["Model"]]
        return W204
    if model=='C'and p==5 and k=='W204':
        W204 = [w4 for w4 in C5 if'W204'in w4["Model"]]
        return W204

    if model=='C'and k=='2007':
        old = list(filter(lambda w:w["Model"]=='C-클래스', C[:]))
        return old



@cars.get("/audi/{model}")
def audi(model: str):
    match model:
        case 'A6 (C8)':
            return FileResponse("public/api/vehi/아우디/A6 (C8).json")
        case 'A7 (4K)':
            return FileResponse("public/api/vehi/아우디/A7 (4K).json")


lh = 'http://localhost:8000'

def pig(Z,page,size):
    start_ = (page - 1) * size
    end_ = start_ + size
    return Z[start_:end_]


@cars.get("/Mercedes={model}-{k}/{page}")
async def benz(model: str, k:str, page: int = Path(..., gt=0), size: int = Query(10, gt=0)):
    C = await run(lh+'/encar/benz=C')

    if model=='C'and k=='klasse':
        return pig(C,page,size)

    if model=='C'and k=='W206':    
        W206 = [w6 for w6 in C if'W206'in w6["Model"]]
        return pig(W206,page,size)


manf = '%EC%89%90%EB%B3%B4%EB%A0%88%28GM%EB%8C%80%EC%9A%B0' 
mo = '%ED%8A%B8%EB%9E%99%EC%8A%A4._.Model.%EB%8D%94%2B%EB%89%B4%2B%ED%8A%B8%EB%9E%99%EC%8A%A4' 
sr = '%7CModifiedDate%7C0%7C20'


# @cars.get("/Chevy={model}-{k}/{page}")
# async def chevy(model: str, k:str, page: int = Path(..., gt=0), size: int = Query(10, gt=0)):
#     TB = await raQ(lh+'/encar/chevy=trailblazer')
#     # TB = await run(lh+'/encar/chevy=trailblazer')

#     Trax = await run('https://api.encar.com/search/car/list/premium?count=true&q=(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.%EC%89%90%EB%B3%B4%EB%A0%88(GM%EB%8C%80%EC%9A%B0_)._.(C.ModelGroup.%ED%8A%B8%EB%9E%99%EC%8A%A4._.Model.%EB%8D%94+%EB%89%B4+%ED%8A%B8%EB%9E%99%EC%8A%A4.))))&sr=%7CModifiedDate%7C0%7C20')
#                     # https://api.encar.com/search/car/list/premium?count=true&q=(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.쉐보레(GM대우_)._.(C.ModelGroup.트랙스._.Model.더+뉴+트랙스.))))&sr=|ModifiedDate|0|20

    
#     if model=='Trailblazer'and k=='gm':
#         return pig(TB,page,size)

#     if model=='Trailblazer'and k=='20': #  кузов с 20г

#         XX = [x20 for x20 in TB if x20["Year"] < 202300]
#         return pig(XX,page,size)

#     if model=='Trailblazer'and k=='23':

#         XXIII = [x20 for x20 in TB if x20["Year"] > 202300]
#         return pig(XXIII,page,size)




@cars.get("/Chevy={model}-{k}/{p}")
async def trax(model: str, k:str, p:int, idd: str | None = None):
    trax1 = await run('https://api.encar.com/search/car/list/premium?count=true&q=(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.%EC%89%90%EB%B3%B4%EB%A0%88(GM%EB%8C%80%EC%9A%B0_)._.(C.ModelGroup.%ED%8A%B8%EB%9E%99%EC%8A%A4._.Model.%EB%8D%94+%EB%89%B4+%ED%8A%B8%EB%9E%99%EC%8A%A4.))))&sr=%7CModifiedDate%7C0%7C20')

    if model=='Trax'and k=='gm'and p==1:
        return trax1


    # Все в одном запросе: http://localhost:8000/cars/Chevy=Trax-gm/1?idd=42334160
    # if model == "Trax" and k == "gm" and p == 1:
    #     if idd is None:
    #         return 'trax1'

    #     one = [d for d in trax1 if d.get("Id") == idd]
    #     return one 

    # искать 1 айди
    # if model=='trax'and k=='gm'and p==1:
        #       one = [d for d in trax1["SearchResults"] if d.get("Id") == idd]
        #       one = list(filter(lambda d:d["Id"]==idd, trax1['SearchResults']))

        #       results = trax1.get("SearchResults", [])
        #       one = next((d for d in results if d.get("Id") == idd), None)
            
        #     return trax1


#for i in range(len(a)):
#    b = (a[i]["Model"])
#    if '(G20)' in b:
#         print(b)

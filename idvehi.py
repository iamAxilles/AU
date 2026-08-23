# -*- coding: utf-8 -*-
from fastapi import APIRouter
from fastapi.responses import FileResponse, HTMLResponse, JSONResponse

import requests, json
from konlpy.tag import Kkma

from encar import F
from jsonCars import O, raQ, h
from typing import List

from water.airwater import run

# from water.waid import waid
from water.waid4 import waid4

import httpx, base64, asyncio

from fastapi.encoders import jsonable_encoder



vehi = APIRouter(prefix="/vehi")


#async def ReQ(m,i):
#    re = requests.get(m)
#    js = re.json()
#
#    a = list(filter(lambda d:d["Id"]==i, data[:]))
#    return a


@vehi.get('/router')
def hello():
    return {"":"Hello Router"}




@vehi.get("/BMW={model}-{iddd}")
def car3bmw(model: str, iddd: str):
    if '3시리즈' in model:
        return list(filter(lambda d:d["Id"]==iddd, O('public2/api/vehi/bmw/3.json')[:]))

    elif '5시리즈' in model:
        re = requests.get('http://127.0.0.1:33/veh/?bmw=5', headers=h)
        js = re.json()

        carid = list(filter(lambda d:d["Id"]==iddd, js[:]))
        return carid



@vehi.get("/benz&{mod}/{iddd}")
def car3(mod: str, iddd: str):
    if mod == 'CLS-C257':
        re = requests.get('/vehs/benz/CLS-C257')
        re = re.json()

        i = list(filter(lambda d:d["Id"]==iddd, re['SearchResults'][:]))
        return i

    elif mod == 'G-클래스 W463b':
        response = requests.get('/벤츠/G-클래스 W463b')
        data = response.json()

        a = list(filter(lambda d:d["Id"]==iddd, data['SearchResults'][:]))
        return a



@vehi.get("/아우디&{mod}/{iddd}")
def vehi_audi(mod: str, iddd: str):
    if mod == 'A6 (C8)':
        response = requests.get('http://127.0.0.1:8000/아우디/A6 (C8)')
        data = response.json()

        a = list(filter(lambda d:d["Id"]==iddd, data['SearchResults'][:]))
        return a

    elif mod == 'A7 (4K)':
        response = requests.get('http://127.0.0.1:8000/아우디/A7 (4K)')
        data = response.json()

        a = list(filter(lambda d:d["Id"]==iddd, data['SearchResults'][:]))
        return a


lh = 'http://localhost:8000'

@vehi.get("/Chevy={model}-{iddd}")#response_model=List[str]
async def chevy(model: str, iddd: str):

    if 'Trailblazer' in model:
        re = await raQ(lh+'/encar/chevy=trailblazer')

        # re = O('public2/api/vehi/chevy/trailblazer250.json')
        # re = await waid(lh+'/encar/chevy=trailblazer')

        i = list(filter(lambda d:d["Id"]==iddd, re))
        # w = await waid(i)
        # one = [d for d in re if d.get("Id") == iddd]
        return i
        # return await waid(i)

        # JSONResponse(jsonable_encoder(w))
        # json_str = json.dumps(w, indent=4, default=str)
        # return json_str

    if 'Trax' in model:
        # re = await raQ('http://localhost:8000/vehi/Chevy=Trax-gm/1')
                      # https://api.encar.com/search/car/list/premium?count=true&q=(And.Hidden.N._.(C.CarType.Y._.(C.Manufacturer.쉐보레(GM대우_)._.(C.ModelGroup.트랙스._.Model.더+뉴+트랙스.))))&sr=|ModifiedDate|0|20

        u = f'https://api.encar.com/v1/readside/vehicle/{iddd}'

        # r = requests.get(ulr, headers=h)
        # one = car["advertisement"]["price"]

        # i = list(filter(lambda d:d["Id"]==iddd, re))
        # one = next((d for d in re["SearchResults"] if d.get("Id") == iddd), None)
        # one = [d for d in re['SearchResults'] if d.get("Id") == iddd]

        # p = await rePh(f'https://ci.encar.com/carsdata/cars/inspection/{iddd}_photoPerform1.jpg')

        # one = [d for d in re['SearchResults'] if d.get("Id") == iddd]

        # one = [d for d in trax1json if isinstance(d, dict) and d.get("Id") == iddd]
        # one = [d for d in trax1json if d.get("Id") == iddd]
        # return await waid(one)
        return await waid4(u)



async def rePh(ph):
    async with httpx.AsyncClient(headers=h) as cl:
        resp = await cl.get(ph)
        return resp.json()




@vehi.get("/list", response_model=List[str])
async def get_items():
    results = []

    for i in range(1, 6):
        results.append(f"item_{i}")

    return results

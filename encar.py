from fastapi import FastAPI, Query, Path
from typing import Optional
#from fastapi.responses import JSONResponse


import json

from fastapi import APIRouter

encar = APIRouter(prefix="/encar")


def O(F):
    with open(F, 'r') as jf:
        d = json.load(jf)
        return d["SearchResults"]


@encar.get("/bmw{n}")
async def bmw(n:str):
    match n:
        case "3":
            return O('public2/api/vehi/bmw/3.json')
        case "32":
            return O('public2/api/vehi/bmw/32.json')
        case "33":
            return O('public2/api/vehi/bmw/33.json')

        case "5":
            return O('public2/api/vehi/bmw/5.json')


@encar.get("/benz={n}")
async def bmw(n:str):
    match n:
        case "C":
            return O('public2/api/vehi/benz/C.json')
        case "C2":
            return O(f'public2/api/vehi/benz/C{2}.json')
        case "C3":
            return O(f'public2/api/vehi/benz/C{3}.json')
        case "C4":
            return O(f'public2/api/vehi/benz/C{4}.json')
        case "C5":
            return O(f'public2/api/vehi/benz/C{5}.json')


@encar.get("/chevy={m}")
async def chevy(m:str):
    match m:
        case "trailblazer":
            return O('public2/api/vehi/chevy/trailblazer250.json')
        case "trail":
            A = O('public2/api/vehi/chevy/trailblazer250.json')
            # XX = [x20 for x20 in A if x20["Year"]]
            for item in A[:]:
                photos = item.get("Photos")
                result = [p["location"] for p in photos if p.get("type") in {"001", "007"}]
                return result















# Мок базы данных книг
books_db = [
{"title": "Python Crash Course", "author": "Eric Matthes", "year": 2019},
{"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015},
{"title": "Clean Code", "author": "Robert C. Martin", "year": 2008},
{"title": "The Pragmatic Programmer", "author": "Andrew Hunt, David Thomas", "year": 1999},
# Добавьте больше книг при необходимости
]
@encar.get("/books/") # books/?page=1&size=4&sort_by=year
async def read_books(page: int = Query(1, gt=0), size: int = Query(10, gt=0), sort_by: Optional[str] = None):
# Применяем пагинацию
    start_index = (page - 1) * size
    end_index = start_index + size
    paginated_books = books_db[start_index:end_index]
# Применяем сортировку, если указана
    if sort_by:
        paginated_books = sorted(paginated_books, key=lambda x: x.get(sort_by, 0))
    return {"page": page, "size": size, "sort_by": sort_by, "books": paginated_books}

# neq – искомое значение не равно переданному;
# gt – больше переданного;
# gte – больше или равно переданному;
# in – все записи, которые сходятся с переданными;
# isnull – фильтруемое поле пустое(null);
# lt -меньше переданного;
# lte - меньше или равно переданному;
# not_in/nin - все записи, которые не сходятся с переданными;
# like/ilike – поиск по подстроке.
# https://habr.com/ru/articles/714570/

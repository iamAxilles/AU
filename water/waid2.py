import asyncio
import httpx
from io import BytesIO
from PIL import Image
import json

h = {
        "User-Agent": 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
        # "Host": 'ci.encar.com'
        "Referer": 'https://ci.encar.com'
                }

async def waid2(ULR):

    async def watermarked_from_url(ULR):
        async with httpx.AsyncClient(headers=h) as client:
            
            r = await client.get(ULR, timeout=10)
            r.raise_for_status()

            BASE_PHOTO_URL = "https://ci.encar.com/carpicture"

            payload = r.json()
            price = payload["advertisement"]["price"]

            photos = payload.get("photos", [])

            photos_sorted = sorted(photos, 
            key=lambda p: int(p["code"]) if p.get("code") is not None else 0)

        photo_urls = [
            (p.get("code"), f"{BASE_PHOTO_URL}{p['path']}")
            for p in photos_sorted
            if p.get("path")
        ]


        return {
            "price": price,
            "photos": photo_urls
        }

    price = await watermarked_from_url(ULR)

    return price
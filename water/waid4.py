import asyncio, httpx
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import json, base64


async def waid4(ULR):
    
    def watermark(img: Image.Image, opacity=0.6, font_size=100):
        overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        try:
            font = ImageFont.truetype("public2/css/font/Danj.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        r, g, b = (60, 60, 90)
        alpha = int(255 * max(0, min(1, opacity)))
        draw.text((200, 200), "SK™Automobile", fill=(r, g, b, alpha), font=font)
        out = Image.alpha_composite(img, overlay)

        buf = BytesIO()
        out.convert("RGB").save(buf, format="WEBP", quality=20, method=2)
        # out.save('output_.webp')

        b64 = base64.b64encode(buf.getvalue()).decode("ascii")
        return f"data:image/webp;base64,{b64}"


        # 


    h = {
        "User-Agent": 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
        # "Host": 'ci.encar.com'
        "Referer": 'https://ci.encar.com'
                }

    BASE_PHOTO_URL = "https://ci.encar.com/carpicture"

    async def watermarked_from_url(ULR):
        # sem = asyncio.Semaphore(concurrency=20)
        async with httpx.AsyncClient(headers=h) as client:
            print(h)
            r = await client.get(ULR,timeout=10)
            r.raise_for_status()

            payload = r.json()
            price = payload["advertisement"]["price"]  

            photos = payload.get("photos", [])
            photos_sorted = sorted(
                photos,
                key=lambda p: int(p["code"]) if p.get("code") is not None else 0)

            add = '?impolicy=heightRate'
            full_urls = [BASE_PHOTO_URL+p["path"]+add for p in photos_sorted]


            async def worker(photo_url):
                pr = await client.get(photo_url, timeout=10)
                pr.raise_for_status()

                img = Image.open(BytesIO(pr.content)).convert("RGBA")
                return await asyncio.to_thread(watermark, img)

            results = await asyncio.gather(*(worker(u) for u in full_urls))
            return price, ['car']+results


    return await watermarked_from_url(ULR)








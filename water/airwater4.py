#!/aenv/bin/python3
import httpx, base64, json
import pprint, requests

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

import asyncio

def watermark(base: Image.Image, opacity=0.7, font_size=16): #100

    overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)

    # try:
    font = ImageFont.truetype("public2/css/font/Times.ttf", font_size)
    # except IOError:
    # font = ImageFont.load_default()

    r, g, b = (60, 60, 90)
    alpha = int(255 * max(0, min(1, opacity)))
    draw.text((12, 35), 'SK™Automobile', fill=(r, g, b, alpha), font=font)
    #125,250
    out = Image.alpha_composite(base, overlay)

    buffer = BytesIO()
    out.convert("RGB").save(buffer, format="webp", quality=90, method=2)
    # out.save('output_.webp')

    b64 = base64.b64encode(buffer.getvalue()).decode("ascii")
    return f"data:image/webp;base64,{b64}"


async def fetch_image(client, url):
    r = await client.get(url)
    r.raise_for_status()
    return r.content

async def process_item(client, item):
    photo_path = item.get('Photo')
    if not photo_path:
        return None

    photo_url = f'https://ci.encar.com/carpicture{photo_path}001.jpg?impolicy=heightRate&rh=192&cw=320&ch=192&cg=Center&wtmk=https://&wtmkg=S&wtmkw=7&wtmkh=3'
    photo_url2 = f'https://ci.encar.com/carpicture{photo_path}007.jpg?impolicy=heightRate&rh=192&cw=320&ch=192&cg=Center&wtmk=https://&wtmkg=S&wtmkw=7&wtmkh=3'

    try:
        img_bytes, img2_bytes = await asyncio.gather(
            fetch_image(client, photo_url),
            fetch_image(client, photo_url2),
        )

        img = Image.open(BytesIO(img_bytes)).convert("RGBA")
        img2 = Image.open(BytesIO(img2_bytes)).convert("RGBA")

        return {
            "Id": item.get("Id"),
            "Badge": item.get("Badge"),
            "ModifiedDate": item.get("ModifiedDate"),
            # "Manufacturer": google(item.get("Manufacturer", "")),
            # "Model": item.get("Model"),
            # "ModelEn": google(item.get("Model", "")),
            "Price": item.get("Price"),
            "Mileage": item.get("Mileage"),
            "Year": item.get("Year"),
            "image_data": watermark(img),
            "image_data2": watermark(img2),
            # "BadgEn": google(item.get("Badge", "")),
            
        }
    except Exception as e:
        return {"error": str(e), "path": photo_path}

h = {
        "User-Agent": 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
        # "Host": 'ci.encar.com'
        "Referer": 'https://fem.encar.com/'
                }

async def run(LLL):
    # 
    async with httpx.AsyncClient(headers=h) as client:
        print(h)
        response = await client.get(LLL)
        data = response.json()

        items = data.get('SearchResults',[])
        # items = data.get('SearchResults', [])[:20]

        tasks = [process_item(client, item) for item in items]
        results = await asyncio.gather(*tasks)

        marks = [r for r in results if r is not None]
        print(len(marks))
        return marks



#-----------------------------------------------------------------------








import httpx, json, base64, asyncio, requests
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont

g = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
h = {
        "User-Agent": 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
        # "Host": 'ci.encar.com'
        "Referer": 'https://ci.encar.com'
                }


async def waid(n):
    def watermark(img: Image.Image, opacity=0.8, font_size=100):
        if img.mode != "RGBA":
            img = img.convert("RGBA")

        overlay = Image.new("RGBA", img.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        try:
            font = ImageFont.truetype("public2/css/font/Danj.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        r, g, b = (60, 60, 90)
        alpha = int(255 * max(0, min(1, opacity)))
        draw.text((300, 30), "SK™Automobile", fill=(r, g, b, alpha), font=font)
        out = Image.alpha_composite(img, overlay)

        buf = BytesIO()
        out.convert("RGB").save(buf, format="WEBP", quality=100)
        # out.save('output_.webp')

        b64 = base64.b64encode(buf.getvalue()).decode("ascii")
        return f"data:image/webp;base64,{b64}"


    car = []

    for i in n:

        ulr = f'https://api.encar.com/v1/readside/inspection/vehicle/{i['Id']}'
        r = requests.get(ulr, headers=h)
        # r.raise_for_status()
        # p = r.status_code
        print(i['Id'])

        photo_path = i['Photo']
        fuel = i['FuelType']
        badge = i['Badge']
        selltype = i['SellType']
        # card1 = f'https://ci.encar.com/carsdata/cars/inspection/{idd}_photoPerform1.jpg'
        print(selltype)

        
        car.append({ fuel, badge, selltype })
        car.append({ i['Id'], r })

        photos = []
        for c in range(1,10):
    #
            photo_url = f'http://ci.encar.com/carpicture{photo_path}00{c}.jpg?impolicy=heightRate'
            # print(photo_url)
            photos.append(
            photo_url
            )

    #     for c in range(10,25):
    # #
    #         photo_url = f'http://ci.encar.com/carpicture{photo_path}0{c}.jpg?impolicy=heightRate'
    #         print(photo_url)
    #         photos.append(
    #         photo_url
    #         )

        # print(photos)

    # async def fetch_one(client: httpx.AsyncClient, url: str, timeout_s=1):
    #     r = await client.get(url, timeout=timeout_s)
    #     r.raise_for_status()
    #     print(r.status_code)
    #     return url, r.content

    # https://dzen.ru/a/aJ4z-z8-oS7T3B82 семафор
    async def watermarked_from_urls(urls, concurrency=10):
        sem = asyncio.Semaphore(concurrency)

        async with httpx.AsyncClient(headers=h) as client:
            async def worker(url):
                async with sem:
                    r = await client.get(url, timeout=1)
                    r.raise_for_status()
                    print(r.status_code)
                    
                img = Image.open(BytesIO(r.content))
                return watermark(img)

            results = await asyncio.gather(*(worker(u) for u in urls))


        return results

    # async def fetch(client: httpx.AsyncClient, url: str):
    #     response = await client.get(url)
    #     return response.status_code
    #
    # async def ma(p):
    #     async with httpx.AsyncClient() as client:
    #         tasks = [fetch(client, url) for url in p]
    #         results = await asyncio.gather(*tasks)
    #
    #     print("Status codes:", results)

    # even_checks = list(map(watermark, datas))


    async def fetch_one(ulr):
        with httpx.Client() as client:
            r = client.get(ulr, timeout=20)
            return r.json()


    # cart = await fetch_one(card1)
    # car.append({ cart })

    # done = await watermarked_from_urls(photos)
    # done = ['car']+done

    return car





# async def Asy(LLL):
#     async with httpx.AsyncClient(headers=g) as client:
#         try:
#             img_res = await client.get(LLL)
#
#             if img_res.status_code != 200:
#                 continue
#
#             img = Image.open(BytesIO(img_res.content)).convert("RGBA")
#
#         except Exception as e:
#             return json.dumps({"error": f"Connection failed: {e}"})
#
#         finally:
#             print(LLL)
#
#     return watermark(LLL)






# results = []
#
# for i in range(1, 6):
#     results.append(f"item_{i}")
#
# return results

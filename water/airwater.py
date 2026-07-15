#!/aenv/bin/python3
import httpx, base64, json
import pprint, requests

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont


async def run(LLL):
    def watermark(base: Image.Image, opacity=0.85, font_size=100):

        overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        try:
            font = ImageFont.truetype("public2/css/font/Danj.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        r, g, b = (60, 60, 90)
        alpha = int(255 * max(0, min(1, opacity)))
        draw.text((125, 250), 'SK™Automobile', fill=(r, g, b, alpha), font=font)

        out = Image.alpha_composite(base, overlay)

        buffer = BytesIO()
        out.convert("RGB").save(buffer, format="webp")
        # out.save('output_.webp')

        b64 = base64.b64encode(buffer.getvalue()).decode("ascii")
        return f"data:image/jpeg;base64,{b64}"


    def google(text: str) -> str:
        url = (
            "https://translate.googleapis.com/translate_a/single"
            "?client=gtx&sl=ko&tl=en&dt=t&q="
            + requests.utils.quote(text)
        )

        data = requests.get(url).json()
        return "".join(part[0] for part in data[0])

#-----------------------------------------------------------------------

    marks = []

    g = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
    h = {
        "User-Agent": 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
        # "Host": 'ci.encar.com'
        "Referer": 'https://ci.encar.com'
                }

    async with httpx.AsyncClient(headers=g) as client:
        try:
            response = await client.get(LLL)
            data = response.json()

        except Exception as e:
            return json.dumps({"error": f"Connection failed: {e}"})

        for item in data[:25]:
            try:
                photo_path = item.get('Photo')
                if not photo_path:
                    continue

                photo_url = f'http://ci.encar.com/carpicture{photo_path}001.jpg?impolicy=heightRate'
                photo_url2 = f'http://ci.encar.com/carpicture{photo_path}007.jpg?impolicy=heightRate'

                img_res = await client.get(photo_url)
                img_res2 = await client.get(photo_url2)

                if img_res.status_code != 200:
                    continue

                img = Image.open(BytesIO(img_res.content)).convert("RGBA")
                img2 = Image.open(BytesIO(img_res2.content)).convert("RGBA")

                base64_img = watermark(
                    img
                )
                base64_img2 = watermark(
                    img2
                )


                marks.append({
                    "Id": item.get("Id"),
                    "Manufacturer": google(item.get("Manufacturer", "")),
                    "Model": item.get("Model"),
                    "ModelEn": google(item.get("Model", "")),
                    "Price": item.get("Price"),
                    "Mileage": item.get("Mileage"),
                    "Year": item.get("Year"),
                    "image_data": base64_img,
                    "image_data2": base64_img2,
                    # "Badge": item.get('Badge'),
                    "BadgEn": google(item.get("Badge", "")),
                    "ModifiedDate": item.get('ModifiedDate')
                })

            except Exception as e:
                marks.append({"error": str(e), "path": photo_path})

    #pp = pprint.PrettyPrinter(indent=2, width=30, compact=True)
    ##return pp.pprint(marks)

    #return json.dumps(marks, indent=2)
    return marks




# def watermark(img_obj: Image.Image, text: str, pos, opacity=0.35, font_size=100):
#     # Ensure RGBA so we can composite transparency
#     base = img_obj.convert("RGBA")
#
#     overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
#     draw = ImageDraw.Draw(overlay)
#
#     try:
#         font = ImageFont.truetype("public2/css/font/Danj.ttf", font_size)
#     except IOError:
#         font = ImageFont.load_default()
#
#     r, g, b = (180, 0, 0)
#     alpha = int(255 * max(0, min(1, opacity)))
#     draw.text(pos, text, fill=(r, g, b, alpha), font=font)
#
#     out = Image.alpha_composite(base, overlay)
#
#     buffer = BytesIO()
#     out.convert("RGB").save(buffer, format="JPEG")  # JPEG has no alpha; remove if you want PNG
#     b64 = base64.b64encode(buffer.getvalue()).decode("ascii")
#     return f"data:image/jpeg;base64,{b64}"

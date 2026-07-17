#!/aenv/bin/python3
import httpx, base64, json
import pprint, requests

from io import BytesIO
from PIL import Image, ImageDraw, ImageFont


async def wad2(LLL):
    def watermark(base: Image.Image, opacity=0.95, font_size=100):

        overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        try:
            font = ImageFont.truetype("public2/css/font/Danj.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        r, g, b = (60, 60, 90)
        alpha = int(255 * max(0, min(1, opacity)))
        draw.text((300, 30), 'SK™Automobile', fill=(r, g, b, alpha), font=font)

        out = Image.alpha_composite(base, overlay)

        buffer = BytesIO()
        out.convert("RGB").save(buffer, format="webp")
        out.save('output_.webp')

        b64 = base64.b64encode(buffer.getvalue()).decode("ascii")
        return f"data:image/jpeg;base64,{b64}"

#-----------------------------------------------------------------------

    marks = []

    g = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}

    async with httpx.AsyncClient(headers=g) as client:
        try:
            response = await client.get(LLL)
            data = response.json()

        except Exception as e:
            return json.dumps({"error": f"Connection failed: {e}"})

        for item in data[:5]:
            try:
                photo_path = item.get('Photo')
                if not photo_path:
                    continue

                for c in range(1,3):
                    photo_url = f'http://ci.encar.com/carpicture{photo_path}00{c}.jpg?impolicy=heightRate'

                img_res = await client.get(photo_url)

                if img_res.status_code != 200:
                    continue

                img = Image.open(BytesIO(img_res.content)).convert("RGBA")

                base64_img = watermark(
                    img
                )


                marks.append({

                    "image_data": base64_img

                })

            except Exception as e:
                marks.append({"error": str(e), "path": photo_path})

    #pp = pprint.PrettyPrinter(indent=2, width=30, compact=True)
    ##return pp.pprint(marks)

    #return json.dumps(marks, indent=2)
    return marks

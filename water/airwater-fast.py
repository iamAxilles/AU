import asyncio
import base64
import json
from io import BytesIO

import httpx, requests
from PIL import Image, ImageDraw, ImageFont


async def run(LLL, max_dim=640, webp_quality=45, font_size=30):
    def watermark(base: Image.Image, opacity=0.85, font_size=30):
        # Resize early to reduce CPU + output size
        if base.width > base.height:
            new_w = max_dim
            new_h = int(base.height * (max_dim / base.width))
        else:
            new_h = max_dim
            new_w = int(base.width * (max_dim / base.height))
        base = base.resize((new_w, new_h), Image.Resampling.LANCZOS).convert("RGBA")

        overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
        draw = ImageDraw.Draw(overlay)

        try:
            font = ImageFont.truetype("public2/css/font/Danj.ttf", font_size)
        except IOError:
            font = ImageFont.load_default()

        r, g, b = (60, 60, 90)
        alpha = int(255 * max(0, min(1, opacity)))

        # Keep watermark relative-ish to image size
        x = int(base.width * 0.25)
        y = int(base.height * 0.75)
        draw.text((x, y), "SK™Automobile", fill=(r, g, b, alpha), font=font)

        out = Image.alpha_composite(base, overlay)

        buffer = BytesIO()
        # Faster + smaller: WebP quality lower + method 0/1 (lower is faster)
        out.save(
            buffer,
            format="WEBP",
            quality=webp_quality,
            method=1,
            optimize=True,
        )

        b64 = base64.b64encode(buffer.getvalue()).decode("ascii")
        return f"data:image/webp;base64,{b64}"

    def google(text: str) -> str:
        url = (
            "https://translate.googleapis.com/translate_a/single"
            "?client=gtx&sl=ko&tl=en&dt=t&q="
            + requests.utils.quote(text)
        )

        data = requests.get(url).json()
        return "".join(part[0] for part in data[0])

    marks = []

    headers = {
        "User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"
    }

    timeout = httpx.Timeout(connect=10.0, read=10.0, write=10.0, pool=5.0)

    async with httpx.AsyncClient(headers=headers, timeout=timeout) as client:
        try:
            response = await client.get(LLL)
            response.raise_for_status()
            data = response.json()
        except Exception as e:
            return json.dumps({"error": f"Connection failed: {e}"})

        # Slightly faster: run fewer downloads concurrently (network usually bottleneck)
        # If you want more concurrency, tell me your expected load/limits.
        for item in data[:5]:
            photo_path = item.get("Photo")
            if not photo_path:
                continue

            try:
                photo_url1 = f"http://ci.encar.com/carpicture{photo_path}001.jpg?impolicy=heightRate"
                photo_url2 = f"http://ci.encar.com/carpicture{photo_path}007.jpg?impolicy=heightRate"

                r1, r2 = await asyncio.gather(
                    client.get(photo_url1),
                    client.get(photo_url2),
                )

                if r1.status_code != 200 or r2.status_code != 200:
                    continue

                img1 = Image.open(BytesIO(r1.content))
                img2 = Image.open(BytesIO(r2.content))

                # Convert/encode inside watermark with resizing
                base64_img = watermark(img1, font_size=font_size)
                base64_img2 = watermark(img2, font_size=font_size)

                marks.append({
                    "image_data": base64_img,
                    "image_data2": base64_img2,
                    "Id": item.get("Id"),
                    "Manufacturer": google(item.get("Manufacturer", "")),
                    "Model": item.get("Model"),
                    "ModelEn": google(item.get("Model", "")),
                    "Price": item.get("Price"),
                    "Mileage": item.get("Mileage"),
                    "Year": item.get("Year"),
                    # "Badge": item.get('Badge'),
                    "BadgEn": google(item.get("Badge", "")),
                    "ModifiedDate": item.get('ModifiedDate')
                })

            except Exception as e:
                marks.append({"error": str(e), "path": photo_path})

    return marks

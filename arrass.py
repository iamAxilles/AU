import httpx, base64, asyncio
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
import logging

YRi = "http://ci.encar.com/carpicture/carpicture03/pic4173/41737419_003.jpg?impolicy=heightRate"

URLS = [
    "http://ci.encar.com/carpicture/carpicture03/pic4173/41737419_001.jpg?impolicy=heightRate",
    "http://ci.encar.com/carpicture/carpicture03/pic4173/41737419_002.jpg?impolicy=heightRate",

]

async def fetch(client: httpx.AsyncClient, url: str) -> int:
    response = await client.get(url)
    return response.status_code

async def main():
    async with httpx.AsyncClient() as client:
        tasks = [fetch(client, url) for url in URLS]
        results = await asyncio.gather(*tasks)

    print("Status codes:", results)

    def watermark_batch(images: list[Image.Image], opacity=0.95, font_size=100):
        """
        Apply the SK™Automobile watermark to a list of images.
        Returns a list of base64 data URIs (webp), in the same order as input.
        """
        text = 'SK™Automobile'
        r, g, b = (60, 60, 90)
        alpha = int(255 * max(0, min(1, opacity)))

        # Load font once, reused for every image
        try:
            font = ImageFont.truetype("public2/css/font/Danj.ttf", font_size)
        except IOError:
            logging.warning("Danj.ttf not found, falling back to default font")
            font = ImageFont.load_default()

        MAR = []

        for idx, base in enumerate(images):
            try:
                base = base.convert("RGBA")
                overlay = Image.new("RGBA", base.size, (0, 0, 0, 0))
                draw = ImageDraw.Draw(overlay)

                margin = 20
                bbox = draw.textbbox((0, 0), text, font=font)
                x = base.size[0] - (bbox[2] - bbox[0]) - margin
                y = margin
                draw.text((x, y), text, fill=(r, g, b, alpha), font=font)

                out = Image.alpha_composite(base, overlay)

                buffer = BytesIO()
                out.convert("RGB").save(buffer, format="webp")
                out.save('output_.webp')
                b64 = base64.b64encode(buffer.getvalue()).decode("ascii")
                MAR.append(f"data:image/webp;base64,{b64}")

            except Exception as e:
                logging.error(f"Failed to watermark image at index {idx}: {e}")
                MAR.append(None)  # or re-raise, depending on how you want failures handled

        return MAR

    # watermark_batch(tasks)

if __name__ == "__main__":
    asyncio.run(main())

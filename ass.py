# https://www.python-httpx.org/async/
import trio
import httpx
photo_path = 'huesos'
h = {
    "User-Agent": 'Mozilla/5.0 (compatible; YandexBot/3.0; +http://yandex.com/bots)',
    # "Host": 'encar',
    "Referer": f'https://ci.encar.com/carpicture{photo_path}001.jpg?'
            }
g = {"User-Agent": "Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)"}
async def main():
    async with httpx.AsyncClient(headers=h) as client:
        # https://api.redirect.li/v1/useragent

        response = await client.get('https://showheaders.com/headers.php', timeout=0.5)
        print(response.text, response)



if __name__ == "__main__":
    trio.run(main)


import aiohttp
import asyncio
import time
import requests


async def fetch(url):
	async with aiohttp.ClientSession() as session:
		async with session.get(url) as response:
			return await response.text()


async def main():
	url1 = "https://docs.aiohttp.org/en/stable/"
	url2 = "https://books.toscrape.com/"
	url3 = "https://projobivoire.com/"
	start = time.time()
	resultats = await asyncio.gather(fetch(url1),fetch(url2),fetch(url3))
	end = time.time()

	print(f"Temps exec async = {end - start}")

	start = time.time()
	resultat1 = requests.get(url1)
	resultat2 = requests.get(url2)
	resultat3 = requests.get(url3)
	end = time.time()

	print(f"Temps exec sync = {end - start}")


asyncio.run(main())
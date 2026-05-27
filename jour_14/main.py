from bs4 import BeautifulSoup
import requests
import json

def get_page(url):
	try:
		response = requests.get(url)
		response.raise_for_status()
	except requests.exceptions.HTTPError as e: #error 4xx ou 5xx
		print(f"Erreur serveur: {e}")
		return {}
	except requests.exceptions.RequestException as e:
		print(f"Erreur reseau: {e}")
		return {}
	else:
		return response.text


def get_livres(page):
	soup = BeautifulSoup(page, 'html.parser')
	products = soup.find_all("article", class_="product_pod")

	livres = []
	for product in products:
		title_tag = product.select_one("h3 a")
		title = title_tag.get('title') if title_tag else "Titre Inconnu"
		price_tag = product.find("p", class_="price_color")
		price = price_tag.text.strip().replace('Â£','') if price_tag else "Prix inconnu"

		livres.append({"titre":title, "prix":price})

	return livres

def store_livres(livres):
	with open("livres.json","w") as f:
		json.dump(livres,f)


if __name__ == '__main__':
	url = "https://books.toscrape.com"
	page = get_page(url)

	if not page:
		print("Impossible de recuperer la page")
	else:
		livres = get_livres(page)
		store_livres(livres)

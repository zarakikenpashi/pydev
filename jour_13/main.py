import requests

def fetch_users(url):
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
		return response.json()


if __name__ == '__main__':
	url = "https://jsonplaceholder.typicode.com/users"
	users = fetch_users(url)

	if not users:
		print("Impossible de recuperer les users")
	else:
		for user in users:
			print(f"name: {user.get('name')}, email: {user.get('email')}")

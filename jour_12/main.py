import time

class Chronometre:
	def __enter__(self):
		self.start = time.time()
		return self


	def __exit__(self, exc_type, exc_val, exc_tb):
		self.end = time.time()
		print(f"TEMPS D'EXC: {self.end - self.start}")
		return True






if __name__== "__main__":
	with Chronometre() as c:
		raise ValueError("erreur test")
		print("bonjour le monde")

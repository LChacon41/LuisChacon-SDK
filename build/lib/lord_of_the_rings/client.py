import requests

class LordOfTheRingsClient:
    base_url = "https://the-one-api.dev/v2"

    def __init__(self, bearer_token):
        self.headers = {'Authorization': f'Bearer {bearer_token}'}

    def get_movie(self, movie_id=None):
        url = f"{self.base_url}/movie"
        if movie_id:
            url = f"{self.base_url}/movie/{movie_id}"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code != 200:
            raise LordOfTheRingsError(response.status_code, response.text)
        return response.json()

    def get_movie_quote(self, movie_id):
        url = f"{self.base_url}/movie/{movie_id}/quote/"
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            raise LordOfTheRingsError(response.status_code, response.text)
        return response.json()
    
    def get_book(self, book_id=None):
        url = f"{self.base_url}/book"
        if book_id:
            url = f"{self.base_url}/book/{book_id}"
        
        response = requests.get(url, headers=self.headers)
        
        if response.status_code != 200:
            raise LordOfTheRingsError(response.status_code, response.text)
        return response.json()

    def get_book_chapter(self, book_id):
        url = f"{self.base_url}/book/{book_id}/chapter/"
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            raise LordOfTheRingsError(response.status_code, response.text)
        return response.json()

    def get_quote(self, quote_id=None):
        url = f"{self.base_url}/quote"
        if quote_id:
            url = f"{self.base_url}/quote/{quote_id}"
        
        response = requests.get(url, headers=self.headers)

        if response.status_code != 200:
            raise LordOfTheRingsError(response.status_code, response.text)
        return response.json()
    
class LordOfTheRingsError(Exception):
    """Exception raised for errors related to the API."""

    def __init__(self, status_code, error_message):
        self.status_code = status_code
        self.error_message = error_message

    def __str__(self):
        return f"LordOfTheRingsError: {self.status_code} - {self.error_message}"

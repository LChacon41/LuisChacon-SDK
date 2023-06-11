import unittest
from lord_of_the_rings import LordOfTheRingsClient, LordOfTheRingsError

class LordOfTheRingsAPITestCase(unittest.TestCase):
    def setUp(self):
        # Initialize the LordOfTheRingsClient with a test bearer token
        self.client = LordOfTheRingsClient("PMfbTRb3mAnDcB7VoHer")

    def test_get_movie(self):
        # Test retrieving movie information without specifying movie_id
        movies = self.client.get_movie()
        self.assertIsInstance(movies, dict)
        self.assertGreater(len(movies), 0)

        # Test retrieving movie information with a valid movie_id
        movie_id = "5cd95395de30eff6ebccde5c"
        movie = self.client.get_movie(movie_id)
        self.assertIsInstance(movie, dict)
        self.assertEqual(movie["docs"][0]["_id"], movie_id)

        # Test retrieving movie information with an invalid movie_id
        invalid_movie_id = "invalid-movie-id"
        with self.assertRaises(LordOfTheRingsError):
            self.client.get_movie(invalid_movie_id)

    def test_get_movie_quote(self):
        # Test retrieving movie quotes for a valid movie_id
        movie_id = "5cd95395de30eff6ebccde5c"
        quotes = self.client.get_movie_quote(movie_id)
        self.assertIsInstance(quotes, dict)
        self.assertGreater(len(quotes), 0)

        # Test retrieving movie quotes for an invalid movie_id
        invalid_movie_id = "invalid-movie-id"
        with self.assertRaises(LordOfTheRingsError):
            self.client.get_movie_quote(invalid_movie_id)

    def test_get_quote(self):
        # Test retrieving quotes without specifying quote_id
        quotes = self.client.get_quote()
        self.assertIsInstance(quotes, dict)
        self.assertGreater(len(quotes), 0)

        # Test retrieving quote information with a valid quote_id
        quote_id = "5cd96e05de30eff6ebcceb4e"
        quote = self.client.get_quote(quote_id)
        self.assertIsInstance(quote, dict)
        self.assertEqual(quote["docs"][0]["_id"], quote_id)

        # Test retrieving quote information with an invalid quote_id
        invalid_quote_id = "invalid-quote-id"
        with self.assertRaises(LordOfTheRingsError):
            self.client.get_quote(invalid_quote_id)

if __name__ == '__main__':
    unittest.main()

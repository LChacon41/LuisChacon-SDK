from lord_of_the_rings import LordOfTheRingsClient

bearer_token = "PMfbTRb3mAnDcB7VoHer"

lotr_client = LordOfTheRingsClient(bearer_token)

# Example usage:
# Gets all movies information.
movies_data = lotr_client.get_movie()
print(movies_data)

# The Fellowship Of The Ring : 5cd95395de30eff6ebccde5c

# Gets quotes from LOTR:The Fellowship Of The Ring using its movie_id
movie_data = lotr_client.get_movie_quote(movie_id="5cd95395de30eff6ebccde5c")
print(movie_data)

# Gets all quotes from the movies.
quote_data = lotr_client.get_quote()
print(quote_data)

# Gets a specific quote.
quotes_data = lotr_client.get_quote(quote_id="5cd96e05de30eff6ebcceb4e")
quotes_docs = quotes_data["docs"][0]
print(quotes_docs["dialog"])

# Gets all books information.
books_data = lotr_client.get_book()
print(books_data)

# The Fellowship Of The Ring Book : 5cf5805fb53e011a64671582

# Gets all chapters from the book LOTR:The Fellowship Of The Ring
book_data = lotr_client.get_book_chapter(book_id="5cf5805fb53e011a64671582")
print(book_data)

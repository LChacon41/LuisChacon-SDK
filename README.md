# Lord of the Rings SDK

Python SDK for the Lord of the Rings API

## Installation

To install the Lord of the Rings SDK, you can use pip:

    pip install lord_of_the_rings_sdk.gz

# USAGE

Here's an example of how to use the Lord Of The Rings SDK:

    from lord_of_the_rings.lord_of_the_rings import LordOfTheRingsClient

    bearer_token = "user_provided_bearer_token"

    lotr_client = LordOfTheRingsClient(bearer_token)

    # Example :
    # Create a client instance with your bearer token
    client = LordOfTheRingsClient('your-bearer-token')

    # Retrieve movie information
    movies = client.get_movie()
    print(movies)

    # Retrieve quotes for a specific movie
    movie_quotes = client.get_movie_quote('movie-id')
    print(movie_quotes)

    # Retrieve book information
    books = client.get_book()
    print(books)

    # Retrieve chapters for a specific book
    book_chapters = client.get_book_chapter('book-id')
    print(book_chapters)

    # Retrieve quote information
    quotes = client.get_quote()
    print(quotes)

Make sure to replace "user_provided_bearer_token" with the actual bearer token you obtain from the Lord of the Rings API.

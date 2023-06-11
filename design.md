# Lord of the Rings SDK Design

## Overview

The Lord of the Rings SDK provides a Python interface to interact with the Lord of the Rings API. It allows developers to retrieve movie information, quotes, book information, and book chapters.

## SDK Structure

The SDK consists of the following main components:

- `lord_of_the_rings.py`: This module contains the `LordOfTheRingsClient` class, which encapsulates the API interactions. It provides methods to retrieve movie, quote, book, and chapter data from the Lord of the Rings API.

- `setup.py`: This file is used for packaging the SDK as a Python package. It includes the necessary metadata and dependencies.

- `README.md`: This file provides installation instructions, usage examples, and other information about the SDK.

- `design.md`: This file (the current file) provides an overview of the SDK's design, its components, and their interactions.

## Usage

To use the Lord of the Rings SDK in your Python project, follow these steps:

1. Install the SDK by running `pip install lord_of_the_rings.gz`.

2. Import the `LordOfTheRingsClient` class from the `lord_of_the_rings` module.

3. Create an instance of the `LordOfTheRingsClient` class with your bearer token.

4. Use the available methods of the client to interact with the Lord of the Rings API and retrieve the desired data.

## Error Handling

The SDK includes an `LordOfTheRingsError` class to handle errors related to the API. It is raised when an API request returns a non-200 status code. The error class contains the status code and error message received from the API.

## Contributions

Contributions to the Lord of the Rings SDK are welcome. If you find any issues or want to enhance the SDK, feel free to open a pull request on the GitHub repository.

Here are some examples of how to use the Lord of the Rings SDK:

from lord_of_the_rings.lord_of_the_rings import LordOfTheRingsClient

# Initialize the Lord of the Rings client with the bearer token
bearer_token = "your_bearer_token_here"
lotr_client = LordOfTheRingsClient(bearer_token)

# Retrieve all movies
movies = lotr_client.get_movie()
print(movies)

# Retrieve a specific movie by ID
movie_id = "5cd95395de30eff6ebccde5a"
movie = lotr_client.get_movie(movie_id)
print(movie)

# Retrieve all quotes
quotes = lotr_client.get_quote()
print(quotes)

# Retrieve a specific quote by ID
quote_id = "5cd96e05de30eff6ebcceb4e"
quote = lotr_client.get_quote(quote_id)
print(quote)
